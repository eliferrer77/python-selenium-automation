from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Launch Amazon website')
def launch_amazon(context):
    context.driver.get('https://www.amazon.com')

@when ('Click on cart')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/cart/view.html?']").click()

@then ('Verify empty cart')
def verify_empty_cart(context):
    expected_results ='Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'