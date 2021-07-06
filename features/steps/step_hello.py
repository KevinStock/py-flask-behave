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
    #positive test
    assert context.response.status_code == 200, "Response code is different: %s" % context.response.status_code
    #negative test
    #assert context.response.status_code == 404, "Response code is different: %s" % context.response.status_code

    #positive test
    json_response = context.response.json()
    #negative test
    #json_response = {'greeting': 'empty', 'name': 'empty'}
    assert json_response['name'] == context.name, 'Data is not the expected one: %s' % json_response['name']
