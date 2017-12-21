#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

with open('tabula-NomesAdmit.csv', 'r') as csvin, open('nomes_clean.csv','w+') as csvout:
    writer = csv.writer(csvout)
    nome_pequeno = 'asdasdasdasdassdassdasdasd'
    m = 0; f = 0
    for row in csv.reader(csvin):
        if row[0] == '':
            pass
        elif row[0] == 'GÉNERO':
            pass
        else:
            row[0], row[1] = row[1], row[0]
            if row[1] == 'Femininos':
                row[1] = 'Feminino'
                f += 1
            elif row[1] == 'Masculinos':
                row[1] = 'Masculino'
                m += 1
            if len(row[0]) < len(nome_pequeno):
                nome_pequeno = row[0]
            writer.writerow(row[0:2])

print('M:',m,'; F:', f, '; Nome mais pequeno:', nome_pequeno)