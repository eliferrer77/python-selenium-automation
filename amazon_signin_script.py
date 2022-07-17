from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()

expected_results ='Sign-In'

actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'

print('Test Case Passed')

driver.find_element(By.XPATH, "//label[@for='ap_email']")

driver.quit()

