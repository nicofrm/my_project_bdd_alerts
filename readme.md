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
Create following files:  
feature files = are descriptive files that contain BDD scenarios  
page files = are files that contain all elements which are interacting with web pages  
step definition files = are those files that make the connection between feature files and page files  

After we have above packages created, we have the following steps:  
   - create the browser file (the browser file has the extension .py and is done at the package level with BDD)
   - create the Base_Page page that contains methods generally valid for all pages (click, type, etc.)
   - create the environment file and put Browser, base_page in the context
   - create the features file where we detail the test scenarios
   - when we know the scenarios, we know the steps, so we create the steps file
   - after creating the steps, create the page, with elements and methods
   - return to the environment file and add the page to the context  

## 2. Libraries used:
from selenium.webdriver.common.by import By  
from behave import *  
from browser import Browser  
from seleniumbase import Driver

## 3. Running the tests
- can be done by running each scenario at a time using tags (example: --tags=T1)
- can be done by running all the scenarios from feature file, following command will be performed:
              behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
   

## 4. Test results 
Through running the test suites we have obtained a number of three executed tests, two passed and two failed. The tests that were passed were the following:
test_sorting_by_price_descending
test_check_sign_in_not_possible_when_user_and_pass_empty
The test that was failed was test_check_search_results The test was failed because the title of the search results products was not always in correspondence to the search criteria For testing purposes we can consider this as a correct result since the test was properly designed to validate that all the products have the search criteria in the title In real life, this might be an expected behaviour because the search criteria might coincide with some product parameters, even if the search criteria is not in the title, in which case we would have to clarify the expected behaviour with a business analyst

## 5. Performance indicators:
   - in order to make the code more efficient the most suitable selectors were found in order to be able to identify the web elements in consequence, id or link text selectors were used as means of identification, except 
     when the specifics of a web element required otherwise Also, CSS selector was preferred to XPATH selector since it is usually faster. Nevertheless, whenever we needed to search for an element that was not able to be 
    found with CSS selector XPATH selector was used
   - in order to make the execution more efficient we have used elements like break in order to avoid unnecessary loop execution and also tried to make variable assignment only when needed, reducing variable reassignment 
     to a minimum
   - also, the usage of a sleep instruction was reduced as much as possible and as a general trend the waits are to be preferred to the sleep instruction
