import requests
from bs4 import BeautifulSoup

'''
Asia --> China --> www.ihep.ac.cn version 7.0
http://v-www.ihep.ac.cn/cgi-bin/traceroute.pl?target=youtube.com&function=traceroute
'''
def main(numDominio):
    if numDominio == 1:
        page = requests.get("http://v-www.ihep.ac.cn/cgi-bin/traceroute.pl?target=google.com&function=traceroute")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('asiagoogle.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
    if numDominio == 2:
        page = requests.get("http://v-www.ihep.ac.cn/cgi-bin/traceroute.pl?target=youtube.com&function=traceroute")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('asiayoutube.txt', 'w')
        archivo.write(rutas)
        archivo.close()
        lista=rutas.split('\n')
        lista.pop(0)
        objelementos = [objeto.split(' ') for objeto in lista]
        print(objelementos)
    if numDominio == 3:
        page = requests.get("http://v-www.ihep.ac.cn/cgi-bin/traceroute.pl?target=facebook.com&function=traceroute")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.find_all('pre')[0].get_text())
        print()
        rutas = soup.find_all('pre')[0].get_text()
        archivo = open('asiafacebook.txt', 'w')
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
