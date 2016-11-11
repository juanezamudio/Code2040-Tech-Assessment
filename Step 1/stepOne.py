# Author: © Juan Zamudio 2016
# Date: September 5, 2016
# Code2040-Tech-Assessment: Step One
#
# Makes a POST request with personal API token and github repository
# to connect to the registration endpoint

import requests

# Make POST request to register to endpoint with token and github repository
r = requests.post('http://challenge.code2040.org/api/register',
    data = {'token':'1affd2045f325a53eece718f96429a70',
        'github': 'https://github.com/juanezamudio/Code2040-Tech-Assessment.git'})

# Print the request response
print r.text
