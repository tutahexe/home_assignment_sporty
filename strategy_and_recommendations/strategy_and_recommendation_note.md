# Strategy & Recommendations

## Selected tests for automation
Test selection was relatively straightforward because the scope of this task limited the number of tests, so I focused on covering the most critical paths.
For the UI, I chose to verify the end-to-end flow of a user placing a bet, as this represents one of the core functionalities of the product.
For the BE, I decided to validate that the system properly prevents unauthorized bet placements.

## What you intentionally left as manual only and why
Rebet flow (T-04) - this test depends on network loss and recovery, which is might be unstable when it comes to CI/CI.

## Your top 2–3 recommendations if this project were to scale
* Improve Test Framework Architecture:
  * Rework steps layer(add Page layer) 
  * Reporting for future CI/CD integration
  * Move configuration to env variables
* Introduce Performance and Load Testing:
  * Include performance as part of regular sprint activities (since product can have many concurrent users) 
  * Simulate realistic peak traffic scenarios (since product can have a huge load during some sport events)
* Security audit
  * Perform periodic security audits 
  * Perform penetration testing of the API.