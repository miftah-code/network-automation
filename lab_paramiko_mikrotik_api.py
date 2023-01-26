import routeros_api
import json


#ip address mikrotik
host="103.1.1.1"
#koneksi ke mikrotik

connection=routeros_api.RouterOsApiPool(host,username="admin",password="idnmantab",plaintext_login=True)

api=connection.get_api()
#menentukan path dan mengambil hasil
list_ipadd=api.get_resource("ip/address/")
show_ipadd=list_ipadd.get()
#menampilkan hasil
print(json.dumps(show_ipadd,indent=3))
#close koneksi
connection.disconnect()
