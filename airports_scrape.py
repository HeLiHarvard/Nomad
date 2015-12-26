from selenium import webdriver
import time
import random
import numpy as np

path_to_chromedriver = './chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://www.planeflighttracker.com/2014/02/top-100-european-airports-flightradar24.html'
browser.get(url)

#post-body-1590213145563085613 > center > table > tbody > tr:nth-child(2) > td:nth-child(4)

airports = ['JFK', 'LAX', 'ORD', 'ATL', 'DFW', 'SFO']

for i in xrange(2, 102):
  new_airport = browser.find_element_by_css_selector('#post-body-1590213145563085613 > center > table > tbody > tr:nth-child(%s) > td:nth-child(4)' % str(i))
  airports.append(new_airport.text)

trips = {}

for airport in airports:
  trips[airport] = [port for port in airports if port != airport]

count = 0
fcount = 0
f = 0

for src in trips:
  for dest in trips[src]:
    if count % 10 == 0:
      if f:
        f.close()
      fcount += 1
      f = open('journeys/%s' % fcount, 'wb')
    f.write('%s,%s\n' % (src,dest)) 
    count += 1

f.close()
