import requests
from bs4 import BeautifulSoup

'''
Europa --> Austria --> nemox.net
http://nemox.net/traceroute/index.pl?t=facebook.com
'''
def main(numDominio):
    if numDominio == 1:
        page = requests.get("http://nemox.net/traceroute/index.pl?t=google.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('europagoogle.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
    if numDominio == 2:
        page = requests.get("http://nemox.net/traceroute/index.pl?t=youtube.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('europayoutube.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
    if numDominio == 3:
        page = requests.get("http://nemox.net/traceroute/index.pl?t=facebook.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('europafacebook.txt', 'w')
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
