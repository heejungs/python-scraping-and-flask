from flask import Flask as F
from flask import render_template
from covid_people import person_covid
from covid_ko import call_data_info
import requests
import json
app = F(__name__)

@app.route('/items')
def items():
    msg = call_data_info()
    return render_template('covid_ko.html',msg=msg)

@app.route('/')
def index():
    msg = person_covid()
    return render_template('covid_people.html',msg=msg)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
