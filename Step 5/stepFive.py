# Author: © Juan Zamudio 2016
# Date: October 8, 2016
# Code2040-Tech-Assessment: Step Five
#
# Makes a POST request with personal API token to receive strings of
# date stamp and interval. Then parses date stamp string. Adds interval
# to workable date stamp object to create new date stamp object. Turns
# this datestamp object into a string with a specified string format.
# Send this new string along with the token in a JSON dictionary to the
# validation url via POST request.

import requests
import json
import dateutil.parser
from datetime import datetime, timedelta

# API token
myToken = {'token':'1affd2045f325a53eece718f96429a70'}

# POST request to receive date stamp and time interval
r = requests.post('http://challenge.code2040.org/api/dating', params=myToken)

# Request reponse saved as JSON dictionary
data = r.json()

print r.text # Print response

oldDateString = data["datestamp"] # Get datestamp from dictionary
interval = data["interval"] # Get interval from dictionary

# Parse the datestamp and obtain workable object to add timedelta
oldDate = dateutil.parser.parse(oldDateString)

# Format of original string
format = '%Y-%m-%dT%H:%M:%SZ'

# The new date after interval has been added to old datestamp
newDate = oldDate + timedelta(seconds = interval)

# The new date converted to a string with format of the original string
newDateString = str(newDate.strftime(format))

print interval # Print interval (timedelta)
print oldDateString # Print string of old date
print oldDate # Print workable date stamp object of old date
print newDate # Print workable date stamp object of new date
print newDateString # Print string of new date

# JSON dictionary of token and new datestamp string
jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'datestamp': newDateString}

# POST request to validation URL with JSON dictionary
validate = requests.post('http://challenge.code2040.org/api/dating/validate',
    params=jsonReturn)

# Print request validation reponse
print validate.text
