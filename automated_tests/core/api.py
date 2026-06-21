import requests


class API:
    def __init__(self, base_url, user):
        self.base_url = base_url
        self.user = user

    def reset_balance(self):
        url = self.base_url + "api/reset-balance"
        response = requests.post(
            url,
            headers={
                "x-user-id": f"{self.user}",
            },
        )
        assert response.status_code == 200

    def get_balance(self):
        response = requests.get(
            f"{self.base_url}api/balance",
            headers={
                "x-user-id": f"{self.user}",
            },
        )

        assert response.status_code == 200
        return response.json().get("balance")

    def get_last_upcoming_match(self):
        response = requests.get(
            f"{self.base_url}api/matches",
            headers={
                "x-user-id": f"{self.user}",
            },
        )

        assert response.status_code == 200
        return response.json()[-1]["id"]

    def place_bet(self, match_id, amount):
        payload = {
            "matchId": match_id,
            "selection": "HOME",
            "stake": round(amount + 1, 2),
        }

        response = requests.post(
            f"{self.base_url}api/place-bet",
            headers={
                "x-user-id": f"{self.user}",
            },
            json=payload,
        )

        return response.status_code, response.json()["message"]
