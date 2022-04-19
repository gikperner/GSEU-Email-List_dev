# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:36:44 2022

@author: grper
"""

import pandas as pd

unit_mem = pd.read_csv('Unit_Members.csv') # Needs to be the Amy Template from
                                           # Broadstripes as a csv of members
                                           # rename if filename changes and keep
                                           # in quotes
unit_nm = pd.read_csv('Unit_Nonmem.csv')   # Needs to be the Amy Template from
                                           # Broadstripes as a csv of non-members 
                                           # rename if filename changes and keep
                                           # in quotes

# %% Simplifying the spreadsheet
# Stuff in brackets are the columns to keep. To edit, add 'column name' with a 
# comma in the order you want it to show up
mem_trim = unit_mem[['First Name','Middle Name','Last Name','Nickname','Employer',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email']]
nm_trim = unit_nm[['First Name','Middle Name','Last Name','Nickname','Employer',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email']]
# Sets the way to reference entries later, probably does not need to be changed.
mem_trim.set_index(['Last Name','First Name'],inplace=True)
nm_trim.set_index(['Last Name','First Name'],inplace=True)

# %% Putting Broadstripes list together

# Searches for matching names and checks for overlap. Right_only is names found
# only in non-member report, left_only is only in member only report, and both
# is the overlap between the two
broad_merge = mem_trim.merge(nm_trim,on=['Last Name','First Name'],how='outer',indicator=True)
print(broad_merge["_merge"].value_counts())

# Finds any records that show up in both the member and non-member lists from
# Broadstripes
dupes = broad_merge["_merge"]=="both"
dupes_info = broad_merge[dupes]
print(f'Repeated Names:\n{dupes_info}')
dupes_info.to_csv('Duplicates.csv')

# This drops an unneeded column
broad_merge.drop(columns='_merge',inplace=True)

# %% Full comparison
# Reads a compiled unit list, such as a GOER/HR list and keeps the same 
# columns as before.

hr_list = pd.read_csv('Unit_list.csv') # This is your GOER/HR list. 
                                         # File does need to be a csv, can change
                                         # the name as before
hr_trim = hr_list[['First Name','Middle Name','Last Name','Nickname','Employer',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email','Employer']]

hr_trim.set_index(['Last Name','First Name'],inplace=True) # sets references again

# As before, searches for matching names and checks for overlap. Left_only is 
# names found only in the compiled report, both is the overlap between the two, and
# right_only should be 0
check = hr_trim.merge(broad_merge,on=['Last Name','First Name'],how='left',indicator=True)
print(check["_merge"].value_counts())

# Finds all the names of people only in the compiled list and NOT Broadstripes
not_broad = check['_merge'] == 'left_only'
check.drop(columns="_merge",inplace=True)
missing = check[not_broad]

# Writes out file to a csv, can rename it away from Missing_Names
missing.to_csv('Missing_Names.csv')