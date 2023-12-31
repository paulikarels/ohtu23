*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

*** Test Cases ***
Login With Incorrect Password
# ...
    Input Credentials  kalle  ellak321
    Output Should Contain    Invalid username or password

Login With Nonexistent Username
# ...
    Input Credentials  ellak  ellak321
    Output Should Contain    Invalid username or password

    