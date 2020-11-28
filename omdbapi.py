# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:25:07 2020

@author: lakna
"""
import json
import pandas as pd
import requests

x = {'Content-Type': 'application/json'}
url ='http://www.omdbapi.com/?i=tt3896198&apikey=9fc8c547'
response = requests.get(url, headers = x)
if response.status_code == 200:
    thedict = json.loads(response.content.decode('utf-8'))
else:
    "response failed"
    