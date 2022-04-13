# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:36:44 2022

@author: grper
"""

import pandas as pd

unit_mem = pd.read_csv('Unit_Members.csv')
unit_nm = pd.read_csv('Unit_Nonmem.csv')


mem_trim = unit_mem[['First Name','Middle Name','Last Name','Nickname','Employer',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email']]
nm_trim = unit_nm[['First Name','Middle Name','Last Name','Nickname','Employer',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email']]

mem_trim.set_index(['Last Name','First Name'],inplace=True)
nm_trim.set_index(['Last Name','First Name'],inplace=True)

broad_merge = mem_trim.merge(nm_trim,on=['Last Name','First Name'],how='outer',indicator=True)
print(broad_merge["_merge"].value_counts())

# busted, check later
# dupes = broad_merge[broad_merge["_merge"=="both"]]
# print(f'Repeated Names:\n{dupes}')
broad_merge.drop(columns='_merge',inplace=True)

rose_list = pd.read_csv('Unit_list.csv')
rose_trim = rose_list[['First Name','Middle Name','Last Name','Nickname','Employer',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email','Employer']]

rose_trim.set_index(['Last Name','First Name'],inplace=True)

check = rose_trim.merge(broad_merge,on=['Last Name','First Name'],how='left',indicator=True)
print(check["_merge"].value_counts())

not_broad = check['_merge'] == 'left_only'
check.drop(columns="_merge",inplace=True)
missing = check[not_broad]

missing.to_csv('Missing_Names.csv')