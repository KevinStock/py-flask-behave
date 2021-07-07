Feature: Get from rest api a json response
Scenario Outline: Fetch from rest api a json response
    Given the URL with <frm> and <to> 
    When we consume the distance endpoint
    Then distance json response is retrieved with <distance> distance and 200 as status code

    Examples:
        | frm | to | distance |
        | 63109 | 63139 | 1.792 |