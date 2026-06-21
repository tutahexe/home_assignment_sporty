import requests

def reset_balance():
        url = "https://qae-assignment-tau.vercel.app/api/reset-balance"
        custom_headers = {
            "x-user-id":"candidate-3CybiJF8xy",
        }
        response = requests.post(url, headers=custom_headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.status_code, response.text)

reset_balance()