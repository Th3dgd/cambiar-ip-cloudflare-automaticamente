# Cambiar IP de Cloudflare automáticamente
Un script sencillo para cambiar la IP de Cloudflare automáticamente mediante su API. Sirve para que, si no tienes una IP fija, se cambie automáticamente si es necesario. Solo se tiene que automatizar la ejecución de la script con algún programa para Linux o el Programador de tareas de Windows.
Se necesita lo siguiente:
* Python
* Librería requests y json

# Funcionamiento
Es muy sencillo. Solo tienes que cambiar los datos que te indica la script y listo. Los datos son:
ZONE ID DE CLOUDFLARE,
TOKEN DE API DE CLOUDFLARE,
example.wrykun.com

Y la data a enviar:
    data = { 
        "type": "A", # el tipo del registro
        "name": "api.wrykun.com", # le pone un nombre al registro
        "content": ip_address, # actualiza la IP del registro
        "ttl": 1, # establece el TTL automáticamente
        "proxied": True # indica que el proxy de Cloudflare estará habilitado (cámbialo a "False" sin comillas si quieres que no esté habilitado)
    }
    
Espero que les sirva esta script que creé para automatizar el cambio de IP si cambia. Esto sirve si no tienes una IP fija y tu IP cambia casi siempre.
