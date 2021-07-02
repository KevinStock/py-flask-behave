import requests
from behave import *


@given('the URL with {name}')
def step_impl(context, name):
    context.name = name
    context.url = "http://backend:5000/hello/" + context.name


@when('we consume the endpoint')
def step_impl(context):
    context.response = requests.session().get(context.url)


@then('json response is retrieved with right data and 200 as status code')
def step_impl(context):
    print(context.url)
    assert context.response.status_code == 200, "Response code is difference: %s" % context.response.status_code + \
                                                "Error: " + str(context.response.content)
    json_response = context.response.json()
    assert json_response['name'] == context.name, 'Data is not the expected one: %s' % json_response['name']
