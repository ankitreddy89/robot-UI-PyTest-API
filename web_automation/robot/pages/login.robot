*** Settings ***
Library     SeleniumLibrary
Variables    ../locators/locators.py
Variables    ../data/test_data.py

*** Keywords ***
Wait For The Username Field To Be Visible
	Wait Until Element is Visible    ${email}   timeout=15

Input Username
    Input Text    ${username_text_field}    ${username}

Input Password
    Input Text    ${password_text_field}    ${password}

Click Login
    Click Button    ${login_button}