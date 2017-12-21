from http.client import HTTPConnection as http_con
import wikipedia

a = http_con('http://natura.di.uminho.pt/~jj/musica/musica.html:80')

a.request('POST', '/jjbin/musica-cgi')

