*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
# ...
    Set Username  ellak
    Set Password  ellak321
    Set Password Confirmation  ellak321
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
# ...
    Set Username  ka
    Set Password  ellak321
    Set Password Confirmation  ellak321
    Submit Credentials
    Register Should Fail With Message  Username too short. Minimum of 3 characters.
  
Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# ...
    Set Username  ellak
    Set Password  ellakiswrong
    Set Password Confirmation  ellakiswrong
    Submit Credentials
    Register Should Fail With Message  Password has to be 8 characters and has to contains something else other than letters.

Register With Nonmatching Password And Password Confirmation
# ...
    Set Username  ellak
    Set Password  ellak321
    Set Password Confirmation  ellak3210
    Submit Credentials
    Register Should Fail With Message  Non matching passwords


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open