from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


pico_y_placa_days = {}
weekdays = []
plate_digits = []


def scrap_pyphoy_page(city_to_search):

    try:
        driver = webdriver.Firefox()
        driver.get("http://www.pyphoy.com/")

        city = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, city_to_search))
        )
        city.click()
        print(f"✅ Clicked on city: {city_to_search}")

        wait_til_url_change(driver, driver.current_url)
        
        particular = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Particulares')))
        particular.click()
        print(f"✅ Clicked on Particulares")

      
        wait_for_particulares_to_load(driver)
        more_days = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'particulares?dias=')]"))
        )
        more_days.click()
        print(f"✅ Clicked on Ver más días")
        
        time_tags = driver.find_elements(By.TAG_NAME, 'Time')
        yellow_divs = driver.find_elements(By.CLASS_NAME, 'shadow-yellow-400')
        


        for div in yellow_divs:
            plate_digits.append(div.text)
            # print(f'{div.text}\n\n')

       
        for tag in time_tags:
            weekdays.append(tag.text)
            # print(f'{tag.text}\n\n')
            
        pico_y_placa_days = dict(zip(weekdays, plate_digits))
        
        for date, days in pico_y_placa_days.items():
            print(f'{date} - {days}\n')
            

        input("⏸️ Press Enter to close the browser...")
        driver.quit()
        
    except Exception as e:
        print(f'🚨 Error: {e}')



def wait_til_url_change(driver, old_url):
    WebDriverWait(driver, 10).until(EC.url_changes(old_url))


def wait_for_particulares_to_load(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'No aplica')]")))
        print(f"✅ Particulares page loaded")
    except Exception as e:
        print(f"🚨 Error esperando carga de 'Particulares': {e}")


