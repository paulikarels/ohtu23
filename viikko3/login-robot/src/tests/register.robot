*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
# ...
    Input Credentials  ellak    321ellak
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
# ...
    Input Credentials  kalle  321ellak
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
# ...
    Input Credentials  ka  321ellak
    Output Should Contain  Username too short. Minimum of 3 characters.

Register With Enough Long But Invald Username And Valid Password
# ...
    Input Credentials  ka  321ellak
    Output Should Contain  Username too short. Minimum of 3 characters.

Register With Valid Username And Too Short Password
# ...
    Input Credentials  ellak  ellak1
    Output Should Contain  Password too short.

Register With Valid Username And Long Enough Password Containing Only Letters
# ...
    Input Credentials  ellak  ellakiswrong
    Output Should Contain  Password only contains letters.


*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
    