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
target_url = "https://onlineanmeldung.hochschulsport.uni-heidelberg.de/oa_oeff/info.php"
login_url = "https://onlineanmeldung.hochschulsport.uni-heidelberg.de/oa_oeff/login.php"

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
    
    # Navigate to target URL
    print(f"Navigating to target page: {target_url}")
    driver.get(target_url)
    time.sleep(2)
    
    # Polling for registration button
    print("Starting to poll for registration button...")
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
            
            # Try to find registration button by text
            buttons = driver.find_elements(By.TAG_NAME, "button")
            links = driver.find_elements(By.TAG_NAME, "a")
            inputs = driver.find_elements(By.TAG_NAME, "input")
            
            all_elements = buttons + links + inputs
            
            for element in all_elements:
                try:
                    element_text = element.text.lower() if element.text else ""
                    element_value = element.get_attribute("value")
                    if element_value:
                        element_text += " " + element_value.lower()
                    
                    if any(word in element_text for word in ["register", "anmelden", "sign up", "buchung", "anmeldung", "buchen"]):
                        print(f"✓ Registration button/link found: {element_text}")
                        element.click()
                        print("✓ Registration button clicked!")
                        time.sleep(3)  # Wait to see result
                        print("Registration successful! Closing browser...")
                        driver.quit()
                        exit(0)
                except Exception as e:
                    # Skip elements that can't be interacted with
                    pass
        except Exception as e:
            print(f"Error on iteration {iteration}: {e}")
        
        time.sleep(0.5)

    print("Registration button not found in 2 hours.")
    driver.quit()

except Exception as e:
    print(f"Fatal error: {e}")
    driver.quit()
    raise