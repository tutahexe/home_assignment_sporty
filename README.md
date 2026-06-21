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
## Installation
* Python 3.12+ required
* All necessary packages can be installed with command  ```pip install -r requirements.txt```
* UI test uses API request to reset balance before each test, so manual reset is not required

## Credentials
Update URL and user in .\automated_tests\pytest.ini

## Test execution:
- Go to automated_tests directory: <br />
```cd .\automated_tests\```  <br />
- Run tests with following command: <br />
```pytest```<br />
### Note:
Both automated tests will fail because they are blocked by reported issues (please find in testing_results)