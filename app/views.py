from flask import render_template, flash, redirect, request
from app import app
from .forms import AirportsForm
import requests
import json

URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyAZV-zJJ1GG8Mglx7y64wQ9_Kfc0sKHapE'

@app.route('/')
@app.route('/index')
def index():
  form = AirportsForm()
  user = {'nickname': 'He'} # fake user
  return render_template('index.html',
                         title='Home',
                         user=user,
                         form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
  attr_dict = dict(request.form)
  del attr_dict['csrf_token']
  form = AirportsForm(request.form)
  if request.method == 'POST' and form.validate():
    airports = form.places.data
    dates = form.dates.data
    formatted_dates = [date[-4:]+'-'+date[:2]+'-'+date[3:5] for date in dates]
    prices = []
    results = []
    for i in range(len(airports)-1):
      origin = airports[i]
      dest = airports[i+1]
      data = \
        {
          'request': {
            'passengers': {
              'adultCount': 1
            },
            'slice': [
              {
                'origin': origin,
                'destination': dest,
                'date': formatted_dates[i]
              },
            ]
          }
        }
      headers = {'Content-Type': 'application/json'}
      response = requests.post(URL, data=json.dumps(data), headers=headers)
      results.append(response.json())
      prices.append(results[-1]['trips']['tripOption'][0]['pricing'][0]['saleTotal'])
    user = {'nickname': 'He'} # fake user
    return render_template('results.html',
                           title='Results',
                           user=user,
                           prices=prices,
                           airports=airports,
                           dates=dates)
  return redirect('/index')
