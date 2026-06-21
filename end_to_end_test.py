from selenium import webdriver
from selenium.webdriver.common.by import By

from api import reset_balance

reset_balance()

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://qae-assignment-tau.vercel.app/?user-id=candidate-3CybiJF8xy")
odds_button = driver.find_element(By.ID, "odds-mls-inter-miami-lafc-2026-06-20-away")
#odds_button_real = driver.find_element(By.XPATH, "//*[text()='UPCOMING']/../../following-sibling::div[@class='oddsGrid']/button")
#payout_modal_odd_value = driver.find_element(By.ID, "modal-success-odds")
#payout_modal_body = driver.find_element(By.XPATH, "//*[text()='UPCOMING']/../../following-sibling::div[@class='oddsGrid']/button")

odds_button.click()
bet_slip_input = driver.find_element(By.ID, "bet-slip-stake-input")
bet_slip_input.clear()
bet_slip_input.send_keys("100")
place_button = driver.find_element(By.ID, "bet-slip-place-bet")
place_button.click()
payout_modal_title = driver.find_element(By.XPATH, "//*[@class='modalTitle']")
payout_modal_stake_value = driver.find_element(By.ID, "modal-success-stake")
payout_modal_payout_value = driver.find_element(By.ID, "modal-success-payout")
assert payout_modal_title.text == "Bet Placed Successfully!"
assert payout_modal_stake_value.text == "€100.00"
assert payout_modal_payout_value.text == "€200.00", f"Payout amount is {payout_modal_payout_value.text}"
payout_modal_close = driver.find_element(By.ID, "modal-success-close")
user_balance = driver.find_element(By.XPATH, "//*[@id='header-balance']/span[2]")
assert user_balance.text == "€100.00", f"Balance amount is {user_balance.text}"
driver.close()
