import requests
from bs4 import BeautifulSoup

'''
Oceania --> Australia --> Hafey.org
http://www.hafey.org/cgi-bin/bgplg?cmd=traceroute&req=facebook.com
'''
def main(numDominio):
    if numDominio == 1:
        page = requests.get("http://www.hafey.org/cgi-bin/bgplg?cmd=traceroute&req=google.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('oceaniagoogle.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
    if numDominio == 2:
        page = requests.get("http://www.hafey.org/cgi-bin/bgplg?cmd=traceroute&req=youtube.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('oceaniayoutube.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
    if numDominio == 3:
        page = requests.get("http://www.hafey.org/cgi-bin/bgplg?cmd=traceroute&req=facebook.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('oceaniafacebook.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
if __name__ == '__main__':
    print("1.google.com")
    print("2.youtube.com")
    print("3.facebook.com")
    numDominio = int(input('Ingresa el numero del Dominio: '))
    main(numDominio)
