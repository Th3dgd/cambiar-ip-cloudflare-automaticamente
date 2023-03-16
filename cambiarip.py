import requests
import json

#---------------------------------------#
#---Esta-script-fue-creada-por-Th3dgd---#
#---------------------------------------#

ip_address = requests.get('http://httpbin.org/ip').json()['origin']
#---datos-para-conectarse-a-la-API-de-cloudflare---#

#recuerda cambiar los siguientes datos.

zona_id = "<ZONE ID CLOUDFLARE>" #cuando pongas tu id de zona recuerda borrar los <> para que quede asi: zona_id = "fkhjksuyiiusixi8yasdjkha"

codigo_api = "<TOKEN DE API CLOUDFLARE>" #cuando pongas tu api recuerda borrar los <> para que quede asi: codigo_api = "fkhjksuyiiu1998asdokkzp"

nombre_de_registro = "example.wrykun.com" #aqui ira tu zona a modificar recuerda cambiarla

#--------------------------------------------------#

#---Poner-los-datos-proporcinados-para-conectarse-a-la-API-en-una-variable-junto-con-la-URL---#
url = f"https://api.cloudflare.com/client/v4/zones/{zona_id}/dns_records?type=A&name={nombre_de_registro}" 
#---------------------------------------------------------------------------------------------#

#---headers-para-enviar-hacia-la-api---#
headers = {
    "Authorization": f"Bearer {codigo_api}", #API key
    "Content-Type": "application/json"
}

#---envia-los-datos-mediante-get---#
response = requests.get(url, headers=headers)
#----------------------------------#

#---trae-los-datos-desde-cloudflare---#
dns_records = response.json()["result"]
ip = dns_records[0]["content"] #trae la IP que esta en cloudflare
id_registro = dns_records[0]["id"] #trae el id del registro
#-------------------------------------#

#---revisa-si-la-ip-cambio-si-es-asi-la-modifica---#
if ip!=ip_address:

    url = f"https://api.cloudflare.com/client/v4/zones/{zona_id}/dns_records/{id_registro}"

    headers = {
        "Authorization": f"Bearer {codigo_api}",
        "Content-Type": "application/json"
    }
    #modifica los datos de cloudflare
    data = { 
        "type": "A", #el tipo del registro
        "name": nombre_de_registro, #le pone un nombre a el registro
        "content": ip_address, #actualiza la ip del registro
        "ttl": 1, #establece el ttl en automatico
        "proxied": True #dice que el proxy de cloudflare estara habilitado (cambialo a "False" sin comillas si quieres que no este habilitado)
    }

    #envia los datos a la api de cloudflare
    response = requests.put(url, headers=headers, data=json.dumps(data))

    #muestra un texto informando que la IP se cambio, y te dice por cual.
    print("Las ip se cambio a: "+str(ip_address))
else:
    #si las ip son iguales se mostrara un texto diciendo que es asi.
    print("Las ip siguien siendo iguales.")
#--------------------------------------------------#

#---------------------------------------#
#---Esta-script-fue-creada-por-Th3dgd---#
#---------------------------------------#
