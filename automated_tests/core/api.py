import requests


class API:

    def __init__(self, base_url, user):
        self.base_url = base_url
        self.user = user

    def reset_balance(self):
            url = self.base_url+"api/reset-balance"
            custom_headers = {
                "x-user-id":f"{self.user}",
            }
            response = requests.post(url, headers=custom_headers)
            if response.status_code == 200:
                print(response.text)
            else:
                print(response.status_code, response.text)
