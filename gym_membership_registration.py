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

# Button text to search for when registration opens
# TODO: Update this with the actual button text when you know it
REGISTRATION_BUTTON_TEXT = "BUTTON_TEXT_HERE"  # e.g., "Anmelden", "Jetzt buchen", etc.

# Set to True to click any button that appears when "nicht buchbar" disappears (fallback mode)
FALLBACK_TO_ANY_BUTTON = True

print("Starting Chrome browser...")
# Set up Selenium WebDriver (Chrome with automatic driver management)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    # Login
    print(f"Navigating to login page: {login_url}")
    driver.get(login_url)
    
    print("Waiting for login form...")
    time.sleep(3)  # Give page time to load
    
    # Print page source for debugging
    print("Looking for form fields...")
    
    # Find all input fields
    input_fields = driver.find_elements(By.TAG_NAME, "input")
    print(f"Found {len(input_fields)} input fields")
    
    email_field = None
    password_field = None
    submit_button = None
    
    # Identify fields by type and attributes
    for field in input_fields:
        field_type = field.get_attribute("type")
        field_name = field.get_attribute("name")
        field_id = field.get_attribute("id")
        
        print(f"Field: type={field_type}, name={field_name}, id={field_id}")
        
        # Look for email/text field
        if field_type in ["text", "email"] and email_field is None:
            email_field = field
            print(f"  -> Using as email field")
        
        # Look for password field
        elif field_type == "password" and password_field is None:
            password_field = field
            print(f"  -> Using as password field")
        
        # Look for submit button
        elif field_type == "submit" and submit_button is None:
            submit_button = field
            print(f"  -> Using as submit button")
    
    # If no email field found, try the first text input
    if email_field is None:
        print("Warning: No email field found, trying first input...")
        email_field = input_fields[0] if input_fields else None
    
    # Fill in the form
    if email_field:
        email_field.clear()
        email_field.send_keys(email)
        print("✓ Email entered")
    else:
        raise Exception("Could not find email field!")
    
    if password_field:
        password_field.clear()
        password_field.send_keys(password)
        print("✓ Password entered")
    else:
        raise Exception("Could not find password field!")
    
    # Submit the form
    if submit_button:
        submit_button.click()
        print("✓ Login button clicked")
    else:
        # Try submitting the form by pressing Enter
        print("No submit button found, trying Enter key...")
        password_field.send_keys(Keys.RETURN)
        print("✓ Form submitted with Enter key")
    
    time.sleep(3)  # Wait for login to complete
    print(f"Current URL after login: {driver.current_url}")
    
    # Step 1: Click "Kursanmeldung" link
    print("\nStep 1: Looking for 'Kursanmeldung' link...")
    try:
        kursanmeldung_link = wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Kursanmeldung"))
        )
        print(f"✓ Found 'Kursanmeldung' link")
        kursanmeldung_link.click()
        time.sleep(2)
        print(f"✓ Clicked 'Kursanmeldung', current URL: {driver.current_url}")
    except Exception as e:
        print(f"Error finding 'Kursanmeldung' link: {e}")
        raise
    
    # Step 2: Click "Fitness- und Kraftstudio" link
    print("\nStep 2: Looking for 'Fitness- und Kraftstudio' link...")
    try:
        # Try different variations of the text
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
        else:
            raise Exception("Could not find 'Fitness- und Kraftstudio' link")
    except Exception as e:
        print(f"Error finding 'Fitness- und Kraftstudio' link: {e}")
        raise
    
    # Step 3: Click "Info und Buchung" button for "KraftraumCARD" (not Nebenzeiten)
    print("\nStep 3: Looking for 'Info und Buchung' button for 'KraftraumCARD'...")
    try:
        # Look for the table row containing "KraftraumCARD" but NOT "Nebenzeiten"
        # Then find the "Info und Buchung" button in that row
        info_buchung_found = False
        
        # Strategy: Find all table rows, identify the one with "KraftraumCARD" without "Nebenzeiten"
        # and click the Info und Buchung button in that row
        try:
            # Find all rows in the table
            rows = driver.find_elements(By.TAG_NAME, "tr")
            print(f"  Found {len(rows)} table rows")
            
            for row in rows:
                row_text = row.text
                # Check if this row contains "KraftraumCARD" but not "Nebenzeiten"
                if "KraftraumCARD" in row_text and "Nebenzeiten" not in row_text:
                    print(f"  ✓ Found KraftraumCARD row (without Nebenzeiten): {row_text[:100]}")
                    
                    # Find the "Info und Buchung" button/link in this specific row
                    try:
                        # Try to find input, button, or link with "Info und Buchung" text in this row
                        info_button = row.find_element(By.XPATH, ".//input[@value='Info und Buchung'] | .//button[contains(text(), 'Info und Buchung')] | .//a[contains(text(), 'Info und Buchung')]")
                        print(f"  ✓ Found 'Info und Buchung' button in this row")
                        info_button.click()
                        time.sleep(2)
                        print(f"✓ Clicked 'Info und Buchung' for KraftraumCARD, current URL: {driver.current_url}")
                        info_buchung_found = True
                        break
                    except Exception as e:
                        print(f"  Could not find button in this row: {e}")
                        continue
            
            if not info_buchung_found:
                raise Exception("Could not find 'Info und Buchung' button for KraftraumCARD row")
                
        except Exception as e:
            print(f"Error in table search: {e}")
            raise
            
    except Exception as e:
        print(f"Error finding 'Info und Buchung' button: {e}")
        raise
    
    print("\n✓ Successfully navigated to KraftraumCARD booking page!")
    print(f"Final URL: {driver.current_url}\n")
    
    # Polling for registration button
    print("Starting to poll for registration button...")
    print(f"Looking for button with text: '{REGISTRATION_BUTTON_TEXT}'")
    print(f"Will check every 0.5 seconds for 2 hours")
    start_time = time.time()
    timeout = 2 * 60 * 60  # 2 hours in seconds
    iteration = 0

    while time.time() - start_time < timeout:
        iteration += 1
        elapsed = time.time() - start_time
        print(f"Iteration {iteration} - Elapsed: {elapsed:.1f}s - Checking for registration button...")
        
        try:
            # Refresh the page to check for updates
            driver.refresh()
            time.sleep(0.3)  # Give page a moment to load
            
            # Check if the "nicht buchbar" message is still present
            page_text = driver.find_element(By.TAG_NAME, "body").text
            if "nicht buchbar" in page_text.lower():
                print(f"  Course still not bookable (waiting for registration period)")
                time.sleep(0.5)
                continue
            
            # Registration period has started! Look for buttons
            print(f"  ✓ Registration period started! ('nicht buchbar' message is gone)")
            
            # Look for the registration button with the specific text
            buttons = driver.find_elements(By.TAG_NAME, "button")
            links = driver.find_elements(By.TAG_NAME, "a")
            inputs = driver.find_elements(By.TAG_NAME, "input")
            
            all_elements = buttons + links + inputs
            
            # First, try to find button with the specific text you provided
            found_specific = False
            if REGISTRATION_BUTTON_TEXT != "BUTTON_TEXT_HERE":
                for element in all_elements:
                    try:
                        element_text = element.text if element.text else ""
                        element_value = element.get_attribute("value")
                        if element_value:
                            element_text += " " + element_value
                        
                        # Check if the element contains the registration button text
                        if REGISTRATION_BUTTON_TEXT.lower() in element_text.lower():
                            print(f"✓ Registration button/link found with specific text: '{element_text}'")
                            element.click()
                            print("✓ Registration button clicked!")
                            time.sleep(3)  # Wait to see result
                            print("Registration successful! Closing browser...")
                            driver.quit()
                            exit(0)
                    except Exception as e:
                        # Skip elements that can't be interacted with
                        pass
            
            # Fallback: If specific text not found or not set, click any clickable button/link
            if FALLBACK_TO_ANY_BUTTON:
                print(f"  Looking for any registration button as fallback...")
                for element in all_elements:
                    try:
                        element_text = element.text if element.text else ""
                        element_value = element.get_attribute("value")
                        if element_value:
                            element_text += " " + element_value
                        
                        # Look for common registration-related terms
                        registration_keywords = ["anmeld", "buch", "register", "sign up", "eintrag"]
                        if any(keyword in element_text.lower() for keyword in registration_keywords):
                            print(f"✓ Registration button/link found (fallback): '{element_text}'")
                            element.click()
                            print("✓ Registration button clicked!")
                            time.sleep(3)  # Wait to see result
                            print("Registration successful! Closing browser...")
                            driver.quit()
                            exit(0)
                    except Exception as e:
                        # Skip elements that can't be interacted with
                        pass
                
                print(f"  Warning: 'nicht buchbar' is gone but no registration button found!")
            
        except Exception as e:
            print(f"Error on iteration {iteration}: {e}")
        
        time.sleep(0.5)

    print("Registration button not found in 2 hours.")
    driver.quit()

except Exception as e:
    print(f"Fatal error: {e}")
    driver.quit()
    raise