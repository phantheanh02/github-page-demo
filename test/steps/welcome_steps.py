from behave import when, then

import examples_allure_behave


@when("calling examples_allure_behave.get_message")
def step_impl(context):
    context.message = examples_allure_behave.get_message()


@then("the greeting message with the project's name is created")
def step_impl(context):
    assert context.message == "Hello from examples.allure-behave!"
