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
- Python 3.12+ required
- Create virtual environment
```python -m venv venv```  <br />
- Activate virtual environment 
```.\venv\Scripts\activate```  <br />
>If you need more details on venv - please check official documentation https://docs.python.org/uk/3.14/library/venv.html
- All necessary packages can be installed with command  ```pip install -r requirements.txt```
- UI test uses API request to reset balance before each test, so manual reset is not required

## Credentials
```.\automated_tests\pytest.ini``` is used as configuration file for this framework.
Before test execution should be updated:
- base_url
- user

## Test execution:
- Go to automated_tests directory: <br />
```cd .\automated_tests\```  <br />
- Run tests with following command: <br />
```pytest```
### Note:
>Both automated tests will fail because they are blocked by reported issues (please find in testing_results)