#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv, enchant

d = enchant.Dict("pt_PT")

with open('tabula-NomesAdmit.csv', 'r') as csvin, open('nomes-registados-2016.csv', 'r') as csvin2, open('nomes_clean.csv','w') as csvout:
    writer = csv.writer(csvout, delimiter=',')
    nomes = [] # Para tratar de repetidos
    nome_pequeno = 'asdasdasdasdassdassdasdasd'
    m = 0; f = 0
    for row in csv.reader(csvin):
        if row[0] == '' or row[0] == 'GÉNERO' or len(row[1]) <=3 or d.check(row[1])==False or row[1].lower() in nomes:
            pass
        else:
            nomes.append(row[1].lower())
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

    for row in csv.reader(csvin2):
        if row[0] == '' or row[0] == 'GÉNERO' or len(row[0]) <=3 or d.check(row[0])==False or row[0].lower() in nomes:
            #print('Pass:',row[0])
            pass
        else:
            nomes.append(row[0].lower())
            if row[1] == 'F':
                row[1] = 'Feminino'
                f += 1
            elif row[1] == 'M':
                row[1] = 'Masculino'
                m += 1
            if len(row[0]) < len(nome_pequeno):
                nome_pequeno = row[0]

            writer.writerow(row[0:2])

print('M:',m,'; F:', f, '; Nome mais pequeno:', nome_pequeno)