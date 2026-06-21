# Project structure:

- manual_tests - finished tasks for part A:
  - test_plan - test plan with coverage matrix and designed 6 TC according to the assignment requirements
  - testing_results - results after manual testing, including bug reports
- automated_tests - contains finished tasks for part B:
  - tests - automated tests for UI and API
  - core - structures for UI and API fixtures
  - steps - helpers with steps and locators
- requirements.txt - contains all required libraries
- strategy_and_reccomendations - finished task for part C: description on made decisions and further recommendations

# How to run automation:
* Install all necessary packages ```pip install -r requirements.txt```

# Test execution
- Go to automated_tests directory: <br />
```cd .\automated_tests\```  <br />
- Run tests with following command: <br />
```pytest```
