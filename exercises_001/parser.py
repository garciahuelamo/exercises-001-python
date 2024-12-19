from flask import Flask, request, jsonify
import json

json_data = '{"name" : "Angela", "age" : 26, "city" : "Madrid"}' #Cadena en JSON

python_object = json.loads(json_data) #json.loads -> para pasar de JSON a Python

print(python_object)

json_object = json.dumps(python_object) #json.dumps -> para pasar de Python a JSON

print(json_object)

