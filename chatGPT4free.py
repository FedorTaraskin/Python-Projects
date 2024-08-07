from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Path to your GeckoDriver (update with your actual path)
DRIVER_PATH = r"D:\Program Files\geckoDriver\geckodriver.exe"

# Set up Firefox options (optional)
options = webdriver.FirefoxOptions()
options.headless = False  # Set to True if you want to run headless

# Initialize the WebDriver for Firefox
driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)

try:
	driver.get('URL_of_the_website')

	# Wait for the text box to be available and input text
	text_box = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, 'text_box_id'))
	)
	text_box.send_keys('Your input text')

	# Find and click the button
	button = driver.find_element(By.ID, 'button_id')
	button.click()

	# Wait for the result to be displayed
	result = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, 'result_id'))
	)

	# Copy the displayed text
	displayed_text = result.text
	print(f'Displayed Text: {displayed_text}')

except TimeoutException:
	print("Timeout while waiting for an element.")
except NoSuchElementException:
	print("An element was not found.")
finally:
	driver.quit()
