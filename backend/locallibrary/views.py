import json
import requests
import os
import subprocess

from django.http import HttpResponse
from bs4 import BeautifulSoup


"""
Para la universidad si hay problemas de proxyDict
https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module#8287752

"""

"""
    rawResponse
traceroute: Warning: Multiple interfaces found; using 134.117.14.35 @ hme0
traceroute to 172.217.1.174 (172.217.1.174), 30 hops max, 40 byte packets
 1  unix-gate.physics.carleton.ca (134.117.14.1)  99.131 ms  1.011 ms  0.775 ms
 2  10.50.254.3 (10.50.254.3)  0.554 ms  1.282 ms  0.631 ms
 3  10.30.34.1 (10.30.34.1)  1.238 ms 10.30.33.1 (10.30.33.1)  0.561 ms 10.30.34.1 (10.30.34.1)  0.563 ms
 4  10.30.53.1 (10.30.53.1)  28.513 ms  0.826 ms  0.732 ms
 5  134.117.254.242 (134.117.254.242)  0.880 ms  0.961 ms  0.816 ms
 6  10.30.58.1 (10.30.58.1)  1.038 ms  1.135 ms  0.951 ms
 7  * * *
 8  * * *
 9  *
"""

def ws1(request, host):
    print("America del Norte")
    print("Canada")
    print("physics.carleton.ca")
    print(request,' ', host)
    print("Espere...")
    # america AmericaNorte

    # http_proxy = "http://10.20.4.15:3128"
    # https_proxy = "https://10.20.4.15:3128"
    # ftp_proxy = "ftp://10.20.4.15:3128"
    #
    # proxyDict = {
    # "http" : http_proxy,
    # "https" : https_proxy,
    # "ftp" : ftp_proxy
    # }
    # r = requests.get(url, headers=headers, proxies=proxyDict)
    page = requests.get('http://traceroute.physics.carleton.ca/cgi-bin/traceroute.pl?target=' + host)
    soup = BeautifulSoup(page.content, 'html.parser')
    rawResponse = soup.find_all('pre')[0].get_text()
    # archivo = open('AmericaNorte.txt', 'w')
    # print("Generando Archivo ...")
    # archivo.write(rawResponse)
    # archivo.close()
    print('rawResponse', rawResponse)

    lines = rawResponse.split('\n')
    lines = lines[3:] # remove no info lines
    data = []
    for line in lines:
        line = line.split('  ')
        # print('line', line)
        if line[1].startswith('*'):
            continue
        node = {}
        node['num'] = line[0].replace(' ','')
        host = line[1].split(' ')
        node['hostname'] = host[0]
        node['ip'] = host[1][1:-1]
        try:
            node['ttl1'] = line[2]
        except IndexError:
            node['ttl1'] = False

        try:
            node['ttl2'] = line[3]
        except IndexError:
            node['ttl2'] = False

        try:
            node['ttl3'] = line[4]
        except IndexError:
            node['ttl3'] = False

        data.append(node)
    # print(data)
    #data = {'foo': 'bar', 'hello': 'world'}
    archivo = open('AmericaNorte.txt', 'w')
    print("Generando Archivo ...")
    archivo.write(rawResponse)
    archivo.close()
    print("Archivo Generado!")
    return HttpResponse(json.dumps(data), content_type='application/json')


def ws2(request, host):
    print("America del sur")
    print("Brazil")
    print("")
    print(request,' ', host)
    print("Espere...")
    # america AmericaSur

    # http_proxy = "http://10.20.4.15:3128"
    # https_proxy = "https://10.20.4.15:3128"
    # ftp_proxy = "ftp://10.20.4.15:3128"
    #
    # proxyDict = {
    # "http" : http_proxy,
    # "https" : https_proxy,
    # "ftp" : ftp_proxy
    # }
    page = requests.get('http://ping.unesp.br/cgi-bin/traceroute.pl?target=' + host + '&function=traceroute')
    soup = BeautifulSoup(page.content, 'html.parser')
    rawResponse = soup.find_all('pre')[0].get_text()
    print('rawResponse', rawResponse)
    lines = rawResponse.split('\n')
    lines = lines[3:-2] # remove no info lines
    data = []
    for line in lines:
        line = line.split('  ')
        # print('line', line)
        if line[1].startswith('*'):
            continue
        node = {}
        node['num'] = line[0].replace(' ','')
        host = line[1].split(' ')
        node['hostname'] = host[0]
        node['ip'] = host[1][1:-1]
        try:
            node['ttl1'] = line[2]
        except IndexError:
            node['ttl1'] = False

        try:
            node['ttl2'] = line[3]
        except IndexError:
            node['ttl2'] = False

        try:
            node['ttl3'] = line[4]
        except IndexError:
            node['ttl3'] = False
        data.append(node)
    archivo = open('AmericaSur.txt', 'w')
    print("Generando Archivo ...")
    archivo.write(rawResponse)
    archivo.close()
    print("Archivo Generado!")
    return HttpResponse(json.dumps(data), content_type='application/json')


def ws3(request, host):
    print("Asia")
    print("China")
    print("ihep.ac.cn")
    print(request,' ', host)
    print("Espere...")
    # asia

    # http_proxy = "http://10.20.4.15:3128"
    # https_proxy = "https://10.20.4.15:3128"
    # ftp_proxy = "ftp://10.20.4.15:3128"
    #
    # proxyDict = {
    # "http" : http_proxy,
    # "https" : https_proxy,
    # "ftp" : ftp_proxy
    # }
    page = requests.get('http://v-www.ihep.ac.cn/cgi-bin/traceroute.pl?target=' + host + '&function=traceroute')
    soup = BeautifulSoup(page.content, 'html.parser')
    rawResponse = soup.find_all('pre')[0].get_text()
    print('rawResponse', rawResponse)
    lines = rawResponse.split('\n')
    lines = lines[3:-2] # remove no info lines
    data = []
    for line in lines:
        line = line.split('  ')
        # print('line', line)
        if line[1].startswith('*'):
            continue
        node = {}
        node['num'] = line[0].replace(' ','')
        host = line[1].split(' ')
        node['hostname'] = host[0]
        node['ip'] = host[1][1:-1]
        try:
            node['ttl1'] = line[2]
        except IndexError:
            node['ttl1'] = False

        try:
            node['ttl2'] = line[3]
        except IndexError:
            node['ttl2'] = False

        try:
            node['ttl3'] = line[4]
        except IndexError:
            node['ttl3'] = False
        data.append(node)
    archivo = open('Asia.txt', 'w')
    print("Generando Archivo ...")
    archivo.write(rawResponse)
    archivo.close()
    print("Archivo Generado!")
    return HttpResponse(json.dumps(data), content_type='application/json')


def ws4(request, host):
    print("Europa")
    print("Austria")
    print("nemox.net")
    print(request,' ', host)
    print("Espere...")
    # europa

    # http_proxy = "http://10.20.4.15:3128"
    # https_proxy = "https://10.20.4.15:3128"
    # ftp_proxy = "ftp://10.20.4.15:3128"
    #
    # proxyDict = {
    # "http" : http_proxy,
    # "https" : https_proxy,
    # "ftp" : ftp_proxy
    # }
    page = requests.get('http://nemox.net/traceroute/index.pl?t=' + host)
    soup = BeautifulSoup(page.content, 'html.parser')
    rawResponse = soup.find_all('pre')[0].get_text()
    print('rawResponse', rawResponse)
    lines = rawResponse.split('\n')
    lines = lines[1:-1] # remove no info lines
    data = []
    for line in lines:
        line = line.split('  ')
        # print('line', line)
        if line[1].startswith('*'):
            continue
        node = {}
        node['num'] = line[0].replace(' ','')
        host = line[1].split(' ')
        node['hostname'] = host[0]
        node['ip'] = host[1][1:-1]
        try:
            node['ttl1'] = line[2]
        except IndexError:
            node['ttl1'] = False

        try:
            node['ttl2'] = line[3]
        except IndexError:
            node['ttl2'] = False

        try:
            node['ttl3'] = line[4]
        except IndexError:
            node['ttl3'] = False
        data.append(node)
    archivo = open('Europa.txt', 'w')
    print("Generando Archivo ...")
    archivo.write(rawResponse)
    archivo.close()
    print("Archivo Generado!")
    return HttpResponse(json.dumps(data), content_type='application/json')


def ws5(request, host):
    print("Oceania")
    print("Australia")
    print("hafey.org")
    print(request,' ', host)
    print("Espere...")
    # oceania
    # http_proxy = "http://10.20.4.15:3128"
    # https_proxy = "https://10.20.4.15:3128"
    # ftp_proxy = "ftp://10.20.4.15:3128"
    #
    # proxyDict = {
    # "http" : http_proxy,
    # "https" : https_proxy,
    # "ftp" : ftp_proxy
    # }
    page = requests.get('http://www.hafey.org/cgi-bin/bgplg?cmd=traceroute&req=' + host)
    soup = BeautifulSoup(page.content, 'html.parser')
    rawResponse = soup.find_all('pre')[0].get_text()
    print('rawResponse', rawResponse)
    archivo = open('Oceania.txt', 'w')
    print("Generando Archivo ...")
    archivo.write(rawResponse)
    archivo.close()
    print("Archivo Generado!")
    lines = rawResponse.split('\n')
    lines = lines[1:-3] # remove no info lines
    data = []
    for line in lines:
        line = line.split('  ')
        # print('line', line)
        if line[1].startswith('*'):
            continue
        node = {}
        node['num'] = line[0].replace(' ','')
        host = line[1].split(' ')
        node['hostname'] = host[0]
        node['ip'] = host[1][1:-1]
        try:
            node['ttl1'] = line[2]
        except IndexError:
            node['ttl1'] = False

        try:
            node['ttl2'] = line[3]
        except IndexError:
            node['ttl2'] = False

        try:
            node['ttl3'] = line[4]
        except IndexError:
            node['ttl3'] = False
        data.append(node)
    return HttpResponse(json.dumps(data), content_type='application/json')
# https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
# https://github.com/AgenciaImplementacion/remote-execution/blob/master/main.py#L60
def local(request):
    print("Local")
    print(request)
    print("Espere...")
    # http://localhost:8000/local?host=google.com
    host = request.GET.get('host')
    p = subprocess.Popen(['traceroute', host], cwd='/tmp', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    rawResponse = p.stdout.read().decode('utf-8') #.replace('\n', '')
    print('rawResponse', rawResponse)
    archivo = open('Local.txt', 'w')
    print("Generando Archivo ...")
    archivo.write(rawResponse)
    archivo.close()
    print("Archivo Generado!")
    lines = rawResponse.split('\n')
    lines = lines[1:-1] # remove no info lines
    data = []
    for line in lines:
        line = line.split('  ')
        # print('line', line)
        if line[1].startswith('*'):
            continue
        node = {}
        node['num'] = line[0].replace(' ','')
        host = line[1].split(' ')
        node['hostname'] = host[0]
        node['ip'] = host[1][1:-1]
        try:
            node['ttl1'] = line[2]
        except IndexError:
            node['ttl1'] = False

        try:
            node['ttl2'] = line[3]
        except IndexError:
            node['ttl2'] = False

        try:
            node['ttl3'] = line[4]
        except IndexError:
            node['ttl3'] = False
        data.append(node)
    #data = {'foo': 'bar', 'hello': 'world'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def hello(request):
    return HttpResponse("<h1>Hola Heroku!</h1>")
