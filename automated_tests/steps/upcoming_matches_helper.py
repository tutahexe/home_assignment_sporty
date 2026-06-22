from selenium.webdriver.common.by import By


class UpcomingMatchesHelper:
    def __init__(self, ui):
        self.ui = ui

    def open_bet_slip_for_first_upcoming_match(self):
        self.ui.wd.find_element(
            By.XPATH,
            "//*[text()='UPCOMING']/../../following-sibling::div[@class='oddsGrid']/button",
        ).click()

    def expected_payout_value_for_first_upcoming_match_for_stake(self, stake):
        odds = self.ui.wd.find_element(
            By.XPATH,
            "//*[text()='UPCOMING']/../../following-sibling::div[@class='oddsGrid']/button/span[2]",
        ).text
        return f"€{float(odds) * stake:.2f}"

    def add_stake_amount_to_bet_slip(self, stake):
        bet_slip_input = self.ui.wd.find_element(By.ID, "bet-slip-stake-input")
        bet_slip_input.clear()
        bet_slip_input.send_keys(stake)

    def click_place_bet_button(self):
        self.ui.wd.find_element(By.ID, "bet-slip-place-bet").click()

    def get_payout_modal_title(self):
        return self.ui.wd.find_element(By.XPATH, "//*[@class='modalTitle']").text

    def get_payout_modal_stake_value(self):
        return self.ui.wd.find_element(By.ID, "modal-success-stake").text

    def get_payout_modal_payout_value(self):
        return self.ui.wd.find_element(By.ID, "modal-success-payout").text

    def close_payout_modal(self):
        self.ui.wd.find_element(By.ID, "modal-success-close").click()

    def get_user_balance_label(self):
        return self.ui.wd.find_element(
            By.XPATH, "//*[@id='header-balance']/span[2]"
        ).text
