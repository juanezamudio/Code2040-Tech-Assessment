import requests
import json
import dateutil.parser
from datetime import datetime, timedelta

myToken = {'token':'1affd2045f325a53eece718f96429a70'}
r = requests.post('http://challenge.code2040.org/api/dating', params=myToken)
data = r.json()

print r.text

oldDateString = data["datestamp"]
interval = data["interval"]

oldDate = dateutil.parser.parse(oldDateString)

format = '%Y-%m-%dT%H:%M:%SZ'
newDate = oldDate + timedelta(seconds = interval)
newDateString = str(newDate.strftime(format))

print interval
print oldDateString
print oldDate
print newDate
print newDateString

jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'datestamp': newDateString}

validate = requests.post('http://challenge.code2040.org/api/dating/validate',
    params=jsonReturn)

print validate.text
