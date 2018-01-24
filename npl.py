#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
import json
import requests


SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'
# 注意：在测试时请更换为您的API Token
headers = {'X-Token': 'YOUR_API_TOKEN'}

s = ['他是个傻逼', '美好的世界']
data = json.dumps(s)
resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))

print(resp.text)
