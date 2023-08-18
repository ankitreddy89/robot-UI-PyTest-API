*** Settings ***
Documentation     Dexcom interview challenge
Library           SeleniumLibrary
Resource    ../pages/login.robot
Resource    ../pages/clarity.robot

*** Variables ***
${url}  https://clarity.dexcom.com/
${browser}  chrome

*** Test Cases ***
Verify Successful Login
	[Documentation]    This test case verifies that the user is able to successfully login
	Open Browser    ${url}  ${browser}
	Wait For The Home Users Button To Be Visible
	Click 'Dexcom Clarity For Home Users'
	Input Username
	Input Password
	Click Login

