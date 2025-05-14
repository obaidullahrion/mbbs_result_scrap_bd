import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

downloadfolder = "~/Downloads"
path = 'chromedriver.exe'   
driver = webdriver.Chrome(service=Service(path))

link = "https://result.dghs.gov.bd/mbbs/"
i = 0
roll = 3700547

# Open a file in append mode to save the results
output_file = "results.txt"

print('#######APPLICATION STARTED#######')

with open(output_file, "a", encoding="utf-8") as file:
    while True:
        try:


            driver.get(link)

            # Wait for the roll input box to load
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="roll2"]'))) 
            clickroll = driver.find_element(By.XPATH, '//*[@id="roll2"]')
            clickroll.send_keys(roll)
            time.sleep(0.5)

            # Wait for the submit button to load
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search_box"]/div/button'))) 
            submit = driver.find_element(By.XPATH, '//*[@id="search_box"]/div/button')
            submit.click()
            time.sleep(1)

            # Extract name and mark
            name_element = driver.find_element(By.XPATH, '//*[@id="rockartists"]/tbody/tr[2]/td')
            mark_element = driver.find_element(By.XPATH, '//*[@id="rockartists"]/tbody/tr[3]/td')

            name = name_element.text
            mark = mark_element.text

            print(f"Roll: {roll}, Name: {name}, Mark: {mark}")

            # Save to file
            file.write(f"{roll},{name},{mark}\n")
            file.flush()  # Ensure data is written to the file

            roll += 1

        except Exception as e:
            print(e)
            print('Error occurred. Restarting...')
            time.sleep(10)
            roll += 1

# Close the driver
driver.quit()
