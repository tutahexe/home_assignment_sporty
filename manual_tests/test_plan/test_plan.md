# Tests plan

## Description
This test plan consists of 6 to cover most functionality described in FRS.
In classic test design we are creating test to cover only single check.
But since I'm limited with amount of tests I decided to design them in more practical way to cover all AC.
Some tests are made a little bit abstract to prevent pesticide paradox.

## Coverage matrix
To make it more visual, please find below the coverage matrix.

| Test \ AC | Match list | Bet slip | Place bet interaction | Success receipt | Error modal | Filters |
|:---------:|:----------:|:--------:|:---------------------:|:---------------:|:-----------:|:-------:|
|   T-01    |    Yes     |   Yes    |          Yes          |       Yes       |     No      |   No    |
|   T-02    |    Yes     |   Yes    |          Yes          |       No        |     No      |   No    |
|   T-03    |    Yes     |   Yes    |          Yes          |       Yes       |     No      |   No    |
|   T-04    |    Yes     |   Yes    |          Yes          |       Yes       |     Yes     |   No    |
|   T-05    |    Yes     |   Yes    |          No           |       No        |     No      |   No    |
|   T-06    |    Yes     |    No    |          No           |       No        |     No      |   Yes   |

## Tests
### **ID**: T-01 <br />
**Title**: Bet placement End to End <br />
**Priority**: Critical <br />
**Risk Rationale**: Bet placement is the core business flow of the application. User should always be able to go through the happy pass<br />
**Steps**:
- Precondition: Login as user with more than 100 euro on balance to application
- Go to the Upcoming Football Matches page
- Click on random winner button for first available upcoming match
- Set value between 1 and 100 into the stake field
- Hit Place bet button
- Review receipt popup

**Expected Result**: 
- Receipt contains: Bet ID, Match details, Selection, Stake, Odds at placement, Potential payout, Placement timestamp
- Bet has placed successfully
- After receipt is closed balance reflects current value and user is returned to main flow without active selection

### **ID**: T-02 <br />
**Title**: User is not able to put bet with insufficient funds <br />
**Priority**: Critical  <br />
**Risk Rationale**: Validation of available balance is critical for preventing financial inconsistencies and unauthorized transactions <br />
**Steps**:
- Precondition: Login as user with 20 euro balance
- Open Bet slip for any available match
- Enter 25 euro to the stake field

**Expected Result**:
- Insufficient balance error message is displayed
- Place bet button is disabled<br />

### **ID**: T-03 <br />
**Title**: Stakes and potential payout is calculated properly <br />
**Priority**: Critical <br />
**Risk Rationale**: Incorrect calculations can lead to financial problems and loss of user trust<br />
**Steps**:
- As precondition: Login as user with 20 euro balance
- Click on random winner button for first available upcoming match
- Enter 10 euro to the 'Stake' field
- Draw your attention to the Odds in 'Bet slip' form
- Draw your attention to the Potential Payout value
- Draw your attention to the Match Winner value
- Click 'Place bet' button
- Draw your attention to the Stake value
- Draw your attention to the Odds value
- Draw your attention to the Potential payout value
- Draw your attention to the Match Winner value

**Expected Result**:
- Stakes on all forms equal to 10 euro
- Odds across all forms are equal
- Potential payout is calculated as 10 euro * odds
- Match Winner value corresponds to selected

### **ID**: T-04 <br />
**Title**: User is able to rebet after error during Bet slip processing <br />
**Priority**: Critical  <br />
**Risk Rationale**: Users may experience temporary connectivity issues, it's essential for software to handle possible errors<br />
**Steps**: <br />
- Precondition: Login as user with more than 100 euro on balance to application
- Open Bet slip for any available match
- Enter 25 euro to the 'Stake' field
- Disable internet via developer console 
- Click 'Place bet' button
- Once 'Something wrong' popup is displayed, enable internet via developer console
- Click 'Rebet' button

**Expected Result**:
- Bet has placed successfully
- After receipt is closed - balance reflects current value

### **ID**: T-05 <br />
**Title**: New odd replaces previous selection for already selected Bet Slip <br />
**Priority**: High <br />
**Risk Rationale**: The bet slip must accurately reflect the latest selection to prevent unintended bets <br />
**Steps**:
- As precondition: Login as user with 20 euro balance
- Click on random winner button for first available upcoming match
- Enter 10 euro to the 'Stake' field
- Draw your attention to the Odds in 'Bet slip' form
- Draw your attention to the Potential Payout value
- Click on 'Draw' button for the same match
- Enter 11 euro to the 'Stake' field
- Click on random winner button for any other available upcoming match

**Expected Result**:
- Bet slip form is updated
- Stakes field is empty
- Odds updated according to draw value

### **ID**: T-05 <br />
**Title**: User is able to filter Upcoming football matches <br />
**Priority**: Medium  <br />
**Risk Rationale**: Incorrect filtering can negatively affect usability. Despite lower priority this test was included to make sure that all AC are covered <br />
**Steps**:
- As precondition: Login as user
- Open Date filter
- Set start date as current date
- Set end date as current date + 120 days
- Click 'Apply button'
- Open odds filter
- Set minimum Odd as 4
- Set maximum Odd as 5
- Click 'Apply button'

**Expected Result**:
- In 'Upcoming Football Matches' you can see only upcoming matches filtered by date range and odds
