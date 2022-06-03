#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:11:32 2022

@author: yanis
"""

from sqlite3 import Row
import pandas as pd
import json
from api_insee import criteria 

from api_insee.criteria import Field
from api_insee.criteria import FieldExact
from api_insee.criteria import Periodic
from api_insee import ApiInsee

import numpy as np

from io import StringIO
import csv
import xlrd
import xlwt
from xlwt import Workbook
import pandas as pd
from openpyxl import load_workbook

df = pd.read_excel("Test 2022.xlsx", usecols = 'A,B,C,E', skiprows=3)
ExcelWorkbook = load_workbook("Test 2022.xlsx")
writer = pd.ExcelWriter("Test 2022.xlsx", engine = 'openpyxl')
writer.book = ExcelWorkbook
df.to_excel(writer, sheet_name = 'your sheet name')
writer.save()
writer.close()



