def test_user_is_able_to_make_bet_on_upcoming_football_match(ui):
    """E2e should include critical path for business.
    In case of this test task critical path means let user go through the list of matches and successfully make a bet.
    Despite good practice is to have one assert per test, from my experience e2e tests are run with each build,
    highly maintained so having checks for every critical point improves build quality through CI."""

    ui.go_to_home_page()
    ui.upcoming_matches.open_bet_slip_for_first_upcoming_match()
    ui.upcoming_matches.add_stake_amount_to_bet_slip(100)
    ui.upcoming_matches.click_place_bet_button()
    assert ui.upcoming_matches.get_payout_modal_title() == "Bet Placed Successfully!"
    assert ui.upcoming_matches.get_payout_modal_stake_value() == "€100.00"
    assert (
        ui.upcoming_matches.get_payout_modal_payout_value()
        == ui.upcoming_matches.expected_payout_value_for_first_upcoming_match_for_stake(100)
    )
    ui.upcoming_matches.close_payout_modal()
    assert ui.upcoming_matches.get_user_balance_label() == "Balance: €20.00"
