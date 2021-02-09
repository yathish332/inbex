# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:11:49 2021

@author: LENOVO
"""


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())