import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

email = "tomer.peker@stud.uni-heidelberg.de"
password = "Computer1!"
login_url = "https://onlineanmeldung.hochschulsport.uni-heidelberg.de/oa_oeff/login.php"

# Keywords to search for
REGISTRATION_BUTTON_TEXTS = [
    "Die Buchung des Kurses ist verbindlich",
    "Buchung ist verbindlich",
    "Kurs verbindlich buchen",
    "Verbindlich anmelden",
    "Jetzt verbindlich buchen",
    "Zur verbindlichen Buchung",
    "Platz buchen",
    "Anmelden",
    "Buchen"
]

FALLBACK_KEYWORDS = ["anmeld", "buch", "register", "sign up", "eintrag", "verbindlich"]

print("Starting Chrome browser...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    # Login
    print(f"Navigating to login page: {login_url}")
    driver.get(login_url)
    
    print("Waiting for login form...")
    time.sleep(3)
    
    # Find all input fields
    input_fields = driver.find_elements(By.TAG_NAME, "input")
    print(f"Found {len(input_fields)} input fields")
    
    email_field = None
    password_field = None
    submit_button = None
    
    for field in input_fields:
        field_type = field.get_attribute("type")
        
        if field_type in ["text", "email"] and email_field is None:
            email_field = field
        elif field_type == "password" and password_field is None:
            password_field = field
        elif field_type == "submit" and submit_button is None:
            submit_button = field
    
    # Fill in the form
    if email_field:
        email_field.clear()
        email_field.send_keys(email)
        print("✓ Email entered")
    
    if password_field:
        password_field.clear()
        password_field.send_keys(password)
        print("✓ Password entered")
    
    if submit_button:
        submit_button.click()
        print("✓ Login button clicked")
    
    time.sleep(3)
    print(f"Current URL after login: {driver.current_url}")
    
    # Step 1: Click "Kursanmeldung" link
    print("\nStep 1: Looking for 'Kursanmeldung' link...")
    kursanmeldung_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Kursanmeldung"))
    )
    print(f"✓ Found 'Kursanmeldung' link")
    kursanmeldung_link.click()
    time.sleep(2)
    print(f"✓ Clicked 'Kursanmeldung', current URL: {driver.current_url}")
    
    # Step 2: Click "Fitness- und Kraftstudio" link
    print("\nStep 2: Looking for 'Fitness- und Kraftstudio' link...")
    fitness_link = None
    for text_variant in ["Fitness- und Kraftstudio", "Fitness", "Kraftstudio"]:
        try:
            fitness_link = wait.until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, text_variant))
            )
            print(f"✓ Found link with text containing '{text_variant}'")
            break
        except:
            continue
    
    if fitness_link:
        fitness_link.click()
        time.sleep(2)
        print(f"✓ Clicked 'Fitness- und Kraftstudio', current URL: {driver.current_url}")
    
    # Step 3: Click "Info und Buchung" button for "KraftraumCARD"
    print("\nStep 3: Looking for 'Info und Buchung' button for 'KraftraumCARD'...")
    rows = driver.find_elements(By.TAG_NAME, "tr")
    print(f"  Found {len(rows)} table rows")
    
    for row in rows:
        row_text = row.text
        if "KraftraumCARD" in row_text and "Nebenzeiten" not in row_text:
            print(f"  ✓ Found KraftraumCARD row (without Nebenzeiten)")
            
            try:
                info_button = row.find_element(By.XPATH, ".//input[@value='Info und Buchung'] | .//button[contains(text(), 'Info und Buchung')] | .//a[contains(text(), 'Info und Buchung')]")
                print(f"  ✓ Found 'Info und Buchung' button in this row")
                info_button.click()
                time.sleep(2)
                print(f"✓ Clicked 'Info und Buchung' for KraftraumCARD, current URL: {driver.current_url}")
                break
            except Exception as e:
                print(f"  Could not find button in this row: {e}")
                continue
    
    print("\n✓ Successfully navigated to KraftraumCARD booking page!")
    print(f"Final URL: {driver.current_url}\n")
    
    # Get page content
    page_html = driver.page_source
    page_text = driver.find_element(By.TAG_NAME, "body").text
    
    # Save to file
    with open("/Users/tomerpeker/Usful Scripts/target_page.html", "w", encoding="utf-8") as f:
        f.write(page_html)
    print("✓ Page HTML saved to 'target_page.html'")
    
    with open("/Users/tomerpeker/Usful Scripts/target_page_text.txt", "w", encoding="utf-8") as f:
        f.write(page_text)
    print("✓ Page text saved to 'target_page_text.txt'")
    
    # Scan for keywords
    print("\n" + "="*70)
    print("SCANNING FOR REGISTRATION KEYWORDS")
    print("="*70)
    
    page_text_lower = page_text.lower()
    
    print("\nChecking specific button texts:")
    found_any = False
    for button_text in REGISTRATION_BUTTON_TEXTS:
        if button_text.lower() in page_text_lower:
            print(f"  ⚠️  FOUND: '{button_text}'")
            found_any = True
        else:
            print(f"  ✓ NOT found: '{button_text}'")
    
    print("\nChecking fallback keywords:")
    for keyword in FALLBACK_KEYWORDS:
        count = page_text_lower.count(keyword)
        if count > 0:
            print(f"  ⚠️  FOUND '{keyword}': {count} occurrences")
            # Show context
            start_idx = page_text_lower.find(keyword)
            context_start = max(0, start_idx - 30)
            context_end = min(len(page_text), start_idx + len(keyword) + 30)
            context = page_text[context_start:context_end]
            print(f"      Context: ...{context}...")
            found_any = True
        else:
            print(f"  ✓ NOT found: '{keyword}'")
    
    print("\n" + "="*70)
    if found_any:
        print("⚠️  WARNING: Some keywords were found on the current page!")
        print("This might indicate the button is already visible or keywords need adjustment.")
    else:
        print("✓ GOOD: None of the registration keywords were found.")
        print("This confirms the button is not yet visible on the page.")
    print("="*70)
    
    # Keep browser open for inspection
    print("\nBrowser will stay open for 30 seconds for inspection...")
    time.sleep(30)
    
    driver.quit()

except Exception as e:
    print(f"Fatal error: {e}")
    import traceback
    traceback.print_exc()
    driver.quit()
    raise
