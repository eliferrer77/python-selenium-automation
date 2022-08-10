from selenium.webdriver.common.by import By
from behave import given, when, then





@then ('Verify empty cart')
def verify_empty_cart(context):
    expected_results ='Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'

@when('Open Cart Page')
def cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")

@then('Verify cart has {number_of_items} item(s)')
def item_in_cart(context, number_of_items):
    expected_results = number_of_items
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span#nav-cart-count').text
    assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'