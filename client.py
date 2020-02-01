import requests

# api-endpoint
URL = "https://www.bovada.lv/services/sports/event/v2/events/A/description/basketball/college-basketball"
PARAMS = {}

r = requests.get(url = URL, params = PARAMS)
# extracting data in json format
data = r.json()
