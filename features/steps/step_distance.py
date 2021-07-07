import requests
from behave import *

@given('the URL with {frm} and {to}')
def step_impl(context, frm, to):
    context.frm = frm
    context.to = to
    context.url = "http://backend:5000/distance/" + context.frm + "/" + context.to

@when('we consume the distance endpoint')
def step_impl(context):
    context.response = requests.session().get(context.url)

@then('distance json response is retrieved with {distance} distance and 200 as status code')
def step_impl(context, distance):
    #positive test
    assert context.response.status_code == 200, "Response code is different: %s" % context.response.status_code
    #negative test
    #assert context.response.status_code == 404, "Response code is different: %s" % context.response.status_code

    #positive test
    json_response = context.response.json()
    assert json_response['distance'] == float(distance), 'Data is not the expected one: %s' % json_response['name']