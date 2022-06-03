#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:59:43 2022

@author: yanis
"""

import csv
from html.entities import name2codepoint
import pandas as pd 
import numpy as np
import math
from api_insee.criteria import FieldExact
from api_insee.criteria import Periodic
from api_insee import criteria 
from api_insee import ApiInsee
from openpyxl import load_workbook
from configuration import getPathBySection

pathdirectory = getPathBySection('SECTION1')
print(pathdirectory)

print('-----------------------')





dfs = pd.read_excel(pathdirectory, usecols = 'A,B,C,E', skiprows=3)


dataf = pd.DataFrame(dfs)
df_list = dataf.values.tolist()

cols = dataf.columns.to_list()

dataf.update
for col in cols:
    filt = dataf[col].isnull()
    df_x = dataf.loc[filt]
    #for row, vals in df_x.iteritems():
        
        #print(vals)
        #for val in vals.index:
        #    print(f"index:{val}     column:  {col}")


api = ApiInsee(key = 'gi6dfDwjz39Q9vIhk8lNIsPUptMa' , secret = 'RHAFQhTnPWfkM_qFo_YAIXyVgbga')
champs = [
        'siret',
         'etatAdministratifEtablissement']


room_empty = {}
for index , var in enumerate(df_list) :
    x = float(var[2])
    if math.isnan(x) ==True :
        data = api.siret(q=((FieldExact('denominationUniteLegale', var[1]),
                             FieldExact('codePostalEtablissement', var[3])
         )), champs=champs).get(format = 'csv')
        #print(data)
        reader = csv.reader(data.split('\n'), delimiter=',')
        count = 0
        for row in reader:
            if row[1] == 'A':
                count += 1

        if(count == 1):
            room_empty[index] = data


for index in room_empty:
    reader2 = csv.reader(room_empty[index].split('\n'), delimiter=',')
    for row2 in reader2:
        if row2[1] == 'A':
            df_list[index][2] = row2[0]


df2 = pd.DataFrame(df_list, columns = dataf.columns)
dataf.update(df2)
ExcelWorkbook = load_workbook(pathdirectory)
writer = pd.ExcelWriter(pathdirectory, engine = 'openpyxl')
writer.book = ExcelWorkbook

writer.save()
writer.close()




