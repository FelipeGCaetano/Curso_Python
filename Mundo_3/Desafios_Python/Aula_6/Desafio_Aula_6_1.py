import urllib 
import urllib.request
import urllib.error

try:
    http = str(input('Digite a URL de um site para ver se está acessivel: '))
    site = urllib.request.urlopen(http)
except urllib.error.URLError:
    print('\033[31mNão consigo acessar esse site\033[m')
else:
    print('Consigo acessar esse site')
