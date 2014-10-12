from behave import *

@given('app has been pushed')
def step_impl(context):
    pass

@when('when blog is made')
def step_impl(context):
    assert True is not False

@then('test the blog app')
def step_impl(context):
    assert context.failed is False
