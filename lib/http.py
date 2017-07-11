# -*- coding: utf-8 -*-

import requests

class Http(object):

    def __init__(self,url,path,metodo,payload,headers={},verifyCertificade=True):
        self.url = url
        self.path = path
        self.metodo = metodo
        self.payload = payload
        self.headers = headers
        self.verify = verifyCertificade

    def addHeader(self,headers):
        self.headers = headers

    def sendData(self):

        try:
            r = requests.post(url=self.url + self.path, data=self.payload, headers=self.headers, verify=self.verify)
            statusCode = r.status_code
            body = r.text
        except Exception as e:
            statusCode = None
            body = e.message

        return statusCode, body