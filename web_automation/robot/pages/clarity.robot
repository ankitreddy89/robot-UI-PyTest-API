*** Settings ***
Library     SeleniumLibrary
Variables    ../locators/locators.py
Variables    ../data/test_data.py

*** Keywords ***
Wait For The Home Users Button To be Visible
    Wait Until Element Is Visible    ${home_users_button}   timeout=15

Click 'Dexcom Clarity For Home Users'
    Click Link    ${home_users_button_link}