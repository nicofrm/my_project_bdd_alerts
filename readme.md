# Test Framework - Automation Testing

## 1. Test Setup
### a) Install libraries
pip install selenium  
pip install html-testRunner  
pip install seleniumbase  
pip install behave  
pip install behave-html-testRunner  
Install plugins: gherkin, cucumber and behave.ini

### b) Define test structure
Create following filed:  
feature files = are descriptive files that contain BDD scenarios  
page files = are files that contain all elements which are interacting with web pages  
step definition files = are those files that make the connection between feature files and page files  

## 2. Libraries used:
from selenium.webdriver.common.by import By  
from behave import *  
from browser import Browser  
from seleniumbase import Driver
