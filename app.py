from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_directions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/maps")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))

   
    try:
        directions_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Directions')]")))
        directions_button.click()
    except Exception as e:
        print(f"Error clicking directions button: {e}")
        driver.quit()
        return

    
    source_box = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class='tactile-searchbox-input'])[1]")))
    source_box.clear()
    source_box.send_keys("Vidhana Soudha")
    source_box.send_keys(Keys.RETURN)
    time.sleep(3) 
   
    destination_box = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class='tactile-searchbox-input'])[2]")))
    destination_box.clear()
    destination_box.send_keys("Presidency College Bangalore")
    destination_box.send_keys(Keys.RETURN)
    time.sleep(5) 

    
    driver.save_screenshot("google_maps_directions.png")
    print("Screenshot saved as google_maps_directions.png")
    driver.quit()

if __name__ == "__main__":
    get_directions()
