import requests

def fit_track():
    url = "YOUR_API_FROM_FITBIT_BY_NOCODEAPI"
    params = {}
    r = requests.get(url = url, params = params)
    result = r.json()
    print(result)
    steps = result['steps_count'][0]['value']
    calories = result['calories_expended'][0]['value']
    return steps, calories