# -*- coding: utf-8 -*-
print('holi')

from flask import Flask, request, render_template, jsonify
import requests
import logging
##  flask is the "package" or the "library" (?)...  then the words after "import" are what they call "modules"
app = Flask(__name__)  ## the __name__ thing helps later with something like finding the full path directory (i.e. for when linking to other pictures, db's. etc, in the diretory, that will be used in the webpage)

# Diccionario



@app.route('/home11')
def home11():
    return render_template('home11.html')
    # return 'Este es la plantilla base (home11)'

@app.route('/word11/<words_suministradas_por_client>')
def word11(words_suministradas_por_client):
    # outputstring = 'la palabra enviada por el client (browser) fue: '
    # variableoutput = words_suministradas_por_client
    # return outputstring + variableoutput
    db_palabras = {
        'perro': 'un animal',
        'gato': 'hace miau'
    }
    mi_params = {
        'word': words_suministradas_por_client,
        'definition': db_palabras.get(words_suministradas_por_client, 'key no encontrada')
    }
    return render_template('word11.html', **mi_params)

def function_mi_params(words_suministradas_por_client):
    db_palabras = {
        'perro': 'un animal',
        'gato': 'hace miau'
    }
    mi_params = {
        'word': words_suministradas_por_client,
        'definition': db_palabras.get(words_suministradas_por_client, 'key no encontrada')
    }
    return mi_params

@app.route('/api/word12/<words_suministradas_por_client>')
def api_word12(words_suministradas_por_client):
    mi_params_processed = function_mi_params(words_suministradas_por_client)
    return jsonify(mi_params_processed)

def function_mi_params_jsonify(words_suministradas_por_client):
    respuesta = requests.get('https://991360be.ngrok.io/definition/' + words_suministradas_por_client)
    respuesta = respuesta.json()
    mi_params = {
        'word': words_suministradas_por_client,
        'definition': respuesta.get('definition')
    }
    return mi_params



if __name__ == '__main__':
    app.run(debug = True)
