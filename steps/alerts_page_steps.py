from behave import *

@when('I click on the JS Alert button')
def step_impl(context):
    context.alerts_page.click_javascripts_alert()

@when('I accept the alert')
def step_impl(context):
    context.alerts_page.accept_alert()
@then('I should see the text "{alert_text}"')
def step_impl(context, alert_text):
    context.alerts_page.check_alert_results_text(alert_text)
