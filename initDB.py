# -*- coding: utf-8 -*-

from lib.http import Http

print u"Criando usuário de aplicação"


usr = Http(url='http://localhost:5050',path='/user/add',metodo='post',payload={"username":"appusr","nome":"Usuario do aplicativo","password":"123456"},
           headers={},
           verifyCertificade=False)
record = usr.sendData()
print record
