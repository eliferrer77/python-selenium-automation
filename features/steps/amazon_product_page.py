from selenium.webdriver.common.by import By
from behave import given, when, then

@then ('Results for coffee shown')
def verify_search_results(context):
    expected_results ='"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'

@when ('Click on Product')
def click_on_product(context):
    context.driver.find_element(By.XPATH, "//div [@cel_widget_id='MAIN-SEARCH_RESULTS-2']" ).click()

@when('Click on Add to Cart button')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#add-to-cart-button').click()




