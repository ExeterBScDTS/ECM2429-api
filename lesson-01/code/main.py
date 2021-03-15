import requests
import datetime

uri = 'https://api.nasa.gov/neo/rest/v1/feed'

todays_date = datetime.datetime.today().isoformat()[0:10]

print("Today is ", todays_date)

params = {'api_key':'DEMO_KEY','start_date':todays_date}

r = requests.get(uri, params=params)

# To see the status code, print r
# print(r)
#
# To see the return data, or error message, print r.text
# print(r.text)

if r:
    t = r.json()
    # near_earth_objects is a dictionary
    for a in t['near_earth_objects']:
        print(a)
        objs = t['near_earth_objects'][a]
        for obj in objs:
            print("  id:", obj['id'], "  name:", obj['name'])
            close_approach = obj['close_approach_data'][0]
            print("  close approach date", close_approach['close_approach_date_full'])
            print("  miss_distance", close_approach['miss_distance']['kilometers'],"km")
