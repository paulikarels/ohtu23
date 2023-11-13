*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
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

Login After Successful Registration
# ...
    Set Username  ellak
    Set Password  ellak321
    Set Password Confirmation  ellak321
    Submit Credentials
    Go To Login Page
    Set Username  ellak
    Set Password  ellak321
    Submit Login
    Login Should Succeed

Login After Failed Registration
# ...
    Set Username  ellak
    Set Password  ellakiswrong
    Set Password Confirmation  ellakiswrong
    Submit Credentials
    Register Should Fail With Message  Password has to be 8 characters and has to contains something else other than letters.
    Go To Login Page
    Login Page Should Be Open
    Set Username  ellak
    Set Password  ellakiswrong
    Submit Login
    Login Should Fail With Message  Invalid username or password