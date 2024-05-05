import requests

def fit_track():
    url = "https://v1.nocodeapi.com/priyathamkonda_21/fit/AcVQwVzCLIuGIfHl/aggregatesDatasets?dataTypeName=steps_count,calories_expended&timePeriod=today"
    params = {}
    r = requests.get(url = url, params = params)
    result = r.json()
    print(result)
    steps = result['steps_count'][0]['value']
    calories = result['calories_expended'][0]['value']
    return steps, calories