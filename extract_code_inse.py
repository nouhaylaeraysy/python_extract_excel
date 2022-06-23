import csv
from html.entities import name2codepoint   
import pandas as pd 
import xlsxwriter
import math
from api_insee.criteria import FieldExact   
from api_insee import ApiInsee   
from openpyxl import load_workbook 
from configuration import getConfigBySection
import time

pathdirectory = getConfigBySection('SECTION1','pathSource')  
pathresultFile = getConfigBySection('SECTION1','pathResult')
secret = getConfigBySection('SECTION1','secret')
key = getConfigBySection('SECTION1','key')

dfs = pd.read_excel(pathdirectory, usecols = 'A,B,C,E', skiprows=3)   

dataf = pd.DataFrame(dfs)   
df_list = dataf.values.tolist() 
cols = dataf.columns.to_list()  

dataf.update
api = ApiInsee(key = key , secret = secret)
champs = [
        'siret',
         'etatAdministratifEtablissement'
         ]

room_empty = {}

for index , var in enumerate(df_list) :

    siret = float(var[2])
    if math.isnan(siret) == True :
        data = api.siret(q=((FieldExact('denominationUniteLegale', var[1]),
                             FieldExact('codePostalEtablissement', var[3])
         )), champs=champs).get(format = 'csv')

        print('Call API INSEE COMPANY {0} codepostal {1}'.format(var[1], var[3]))

        reader = csv.reader(data.split('\n'), delimiter=',')
        count = 0
        for row in reader:
            if row[1] == 'A':
                count += 1

        if(count == 1):
            room_empty[index] = data
    
    time.sleep(1) 


for index in room_empty:
    reader2 = csv.reader(room_empty[index].split('\n'), delimiter=',')
    for row2 in reader2:

        if row2[1] == 'A':
            df_list[index][2] = row2[0]
            #print('a new siret finded for company {0} is {1}'.format(df_list[index][1], row2[0]))
    print('A new siret finded for company {0} is {1}'.format(df_list[index][1], row2[0]))

ExcelWorkbook = load_workbook(pathdirectory)

df = pd.DataFrame(df_list, columns = dataf.columns)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(pathresultFile, engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False)


# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})

cell_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': 'red',
    'border': 1})


# Write the column headers with the defined format.
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num + 1, value, header_format)


for row_line, value in enumerate(df.values):
    siret = value[2]
    if math.isnan(float(siret)) == True :
        worksheet.write(row_line+1,  3, str(value[2]), cell_format)
        worksheet.write(row_line+1,  2, str(value[1]), cell_format)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

