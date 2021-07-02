Feature: Get from rest api a json response
Scenario Outline: Fetch from rest api a json response
    Given the URL with <name> 
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code

    Examples:
        | name |
        | John  |
        | Kevin |
        | Michael |