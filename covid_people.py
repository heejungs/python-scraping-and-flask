import requests
import json

def person_covid():
    url = "https://apiv2.corona-live.com/updates.json?timestamp=1613547340934"
    response = requests.get(url = url)
    html = json.loads(response.text)
    return html
