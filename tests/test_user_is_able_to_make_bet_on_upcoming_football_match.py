def test_user_happy_pass(ui):
    ui.go_to_home_page()
    ui.upcoming_matches.open_bet_slip_for_first_upcoming_match()
    ui.upcoming_matches.add_stake_amount_to_bet_slip(100)
    ui.upcoming_matches.click_place_bet_button()
    assert ui.upcoming_matches.get_payout_modal_title() == "Bet Placed Successfully!"
    assert ui.upcoming_matches.get_payout_modal_stake_value() == "€100.00"
    assert ui.upcoming_matches.get_payout_modal_payout_value() == "€245.00"
    ui.upcoming_matches.close_payout_modal()
    assert ui.upcoming_matches.get_user_balance_label() == "Balance: €20.00"