def test_user_is_not_able_to_make_bet_with_insufficient_funds(api):
    """API should cover the most critical part of the application.
    Everything that affects money always is a top priority.
    Since we have a positive test via UI, I've decided to add negative test via API.
    This scenario verifies that users can't abuse system by making bets with insufficient funds."""

    match_id = api.get_last_upcoming_match()
    first_bet_response_status_code, first_bet_response_message = api.place_bet(
        match_id, 100
    )
    assert first_bet_response_status_code == 200
    assert first_bet_response_message == "Bet placed successfully"
    assert api.get_balance() == 20
    second_bet_response_status_code, second_bet_message = api.place_bet(match_id, 100)
    assert second_bet_response_status_code == 422
    assert "insufficient funds" in second_bet_message
