#!/usr/bin/python3
# -*- coding: utf-8 -*-

from http.client import HTTPConnection as http_con
import wikipedia as wk

wk.set_lang('pt')

# a = http_con('http://natura.di.uminho.pt/~jj/musica/musica.html:80')
# a.request('POST', '/jjbin/musica-cgi')

pg = wk.page("")
pg.content