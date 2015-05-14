import requests
import json


url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyAZV-zJJ1GG8Mglx7y64wQ9_Kfc0sKHapE'

airports = [raw_input('Enter the starting airport: ')]
dates = [raw_input('Enter the starting date (YYYY-MM-DD): ')]
#durations = [0]
 
while True:
  new_ap = raw_input('Enter a new destination airport: ')
  final = raw_input('Is this your final destination [y/n]? ').lower()[0] 
  if final == 'n':
    airports.append(new_ap)
    #durations.append(int(raw_input('Enter how many days you will stay there \
    #                                (0 if leaving the same day): ')))
    dates.append(raw_input('Enter the day you leave this destination (YYYY-MM-DD): '))
  else:
    break

#airports = ['BOS', 'ORD', 'SFO'] #, 'MSP', 'TUS']
results = {}

for i in xrange(len(airports)):
  origin = airports[i]
  results[origin] = {}
  dests = airports[:i] + airports[i+1:]
  for dest in dests:
    data = \
      { 
        "request": {
          "passengers": {
            "adultCount": 3
          },
          "slice": [
            {
              "origin": origin,
              "destination": dest,
              "date": "2015-05-24"
            },
            {
              "origin": dest,
              "destination": origin,
              "date": "2015-08-16"
            }
          ]
        }
      }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers) 
    results[origin][dest] = response.json()

"""
for i in xrange(len(airports)):
  origin = airports[i]
  results[origin] = {}
  dests = airports[:i] + airports[i+1:]
  for dest in dests:
    data = \
      { 
        "request": {
          "passengers": {
            "adultCount": 3
          },
          "slice": [
            {
              "origin": origin,
              "destination": dest,
              "date": "2015-05-24"
            },
            {
              "origin": dest,
              "destination": origin,
              "date": "2015-08-16"
            }
          ]
        }
      }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers) 
    results[origin][dest] = response.json()
""" 
"""
data = \
  { 
    "request": {
      "passengers": {
        "adultCount": 1
      },
      "slice": [
        {
          "origin": "BOS",
          "destination": "LAX",
          "date": "2015-05-24"
        },
        {
          "origin": "LAX",
          "destination": "BOS",
          "date": "2015-08-16"
        }
      ]
    }
  }
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

result = response.json()
"""
