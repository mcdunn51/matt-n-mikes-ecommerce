import requests
import json, os
# import pycurl

# authentication = requests.post(r'http://127.0.0.1:5000/getToken')
# print(authentication.text)
# json_data = open('example.json', 'r').read()
# OrderSubmit = requests.post(r'http://127.0.0.1:5000/pushOrder', data=json_data)
# print(OrderSubmit.text)
# authentication = requests.get(r'http://192.168.20.118:8000/o/token/')

IP = '192.168.20.89:8000'
token = 'RzazVFDkRrWvJzpUCUyBsoabf5cQQS'

try:
    test = 'Productlist endpoint'
    print(r'http://' + str(IP) + r'/Productlist/?access_token='+str(token)+r'&format=json')
    authentication = requests.get(r'http://' + str(IP) + r'/Productlist/?access_token='+str(token)+r'&format=json')
    print('  <<< PASS: completed testing with %s >>> \n' % test)
except Exception as e:
    print('  <<< FAIL: completed testing with %s >>> \n %s' % (test, e))

try:
    test = 'Productlist with ID filter endpoint'
    print(r'http://' + str(IP) + r'/Productlist/64681/?access_token='+str(token)+r'&format=json')
    authentication = requests.get(r'http://' + str(IP) + r'/Productlist/64681/?access_token='+str(token)+r'&format=json')
    print('  <<< PASS: completed testing with %s >>> \n' % test)
except Exception as e:
    print('  <<< FAIL: completed testing with %s >>> \n %s' % (test, e))