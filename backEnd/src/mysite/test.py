import requests
import json, os
# import pycurl

# authentication = requests.post(r'http://127.0.0.1:5000/getToken')
# print(authentication.text)
# json_data = open('example.json', 'r').read()
# OrderSubmit = requests.post(r'http://127.0.0.1:5000/pushOrder', data=json_data)
# print(OrderSubmit.text)
# authentication = requests.get(r'http://192.168.20.118:8000/o/token/')

token = 'vOQ18Acqx6ru7pqUEDLIoGaC2JL40S'

try:
    test = 'Productlist endpoint'
    print('<<< Testing %s >>>' % test)
    authentication = requests.get(r'http://192.168.20.118:8000/Productlist/?access_token='+str(token)+r'&format=json')
    print('  <<< PASS: completed testing with %s >>>' % test)
except:
    print('  <<< FAIL: completed testing with %s >>>' % test)

try:
    test = 'Productlist with ID filter endpoint'
    print('<<< Testing %s >>>' % test)
    authentication = requests.get(r'http://192.168.20.118:8000/Productlist/8291/?access_token='+str(token)+r'&format=json')
    print('  <<< PASS: completed testing with %s >>>' % test)
except:
    print('  <<< FAIL: completed testing with %s >>>' % test)