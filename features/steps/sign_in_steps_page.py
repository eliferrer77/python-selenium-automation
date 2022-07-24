from selenium.webdriver.common.by import By
from behave import given, when, then

@then ('Verify Sign in page opened')
def verify_sign_in(context):
    expected_results = 'Sign-In'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'