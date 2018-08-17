#encoding: utf-8

#Aqui ficam todos os imports
import requests
from bs4 import BeautifulSoup
import re
from flask import Flask,jsonify, request


#Função para contar as palavras na url especificada
def conta_palavra(url, palavra):
    r = requests.get(url, allow_redirects=False)#requisitando url
    soup = BeautifulSoup(r.content, 'html.parser')#BS parseando o html
    #Insere na tupla a palavra quando ela é encontrada
    qtd_palavra = soup.find(text=lambda text: text and palavra in text)
    return len(qtd_palavra)#retorna o tamanho da tupla

#declaração de algumas variaveis que serão utilizadas futuramente
app = Flask("webCrawler")
dicionario = {}
cont = 0

@app.route('/crawler/<procurar>',methods=['GET'])


def principal(procurar):
    for url in request.args.getlist('url'):
        dicionario[url] = conta_palavra(url,procurar)
    return jsonify(dicionario)

app.run()
