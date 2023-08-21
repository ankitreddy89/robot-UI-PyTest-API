import requests

from api_automation.pytest.constants import *


def test_login():
    response = requests.get("https://clarity.dexcom.com/")
    assert response.status_code == 200

    url = "https://uam1.dexcom.com/identity/connect/authorize?client_id=" + CLIENT_ID + \
          "&prompt&redirect_uri=" + REDIRECT_URI + "&response_type=code&scope=offline_access"

    response = requests.get(url=url)
    url = response.url

    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "idsrv.xsrf": response.cookies.items()[0][1]
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)

    params = {{'client_id': CLIENT_ID,
               'client_secret': '',
               'grant_type': 'authorization_code',
               'redirect_uri': REDIRECT_URI,
               'code': response.url.split("code=")[1].split("&state")[0]
               }}

    requests.post("https://api.dexcom.com/v2/oauth2/token", params=params, headers=headers)

    access_token = ""  # Access Token can be retrieved from the response above #

    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}

    response = requests.post("https://clarity.dexcom.com/api/subject/1681277794575765504/analysis_session",
                             headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data.get("session_id") is not None
