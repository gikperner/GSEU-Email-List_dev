# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:11:07 2022

@author: grper
"""

import pandas as pd

unit = pd.read_csv('ESF_Contact.csv')

campus = 'ESF'


contact_info = unit[['First Name','Middle Name','Last Name','Nickname',
                      'Department','Dues Status','Member Card Received','Personal Email',
                      'Business Email']]


dues = contact_info['Dues Status']=='Active Member'
cards = contact_info['Member Card Received'] == 'Yes'
member = dues | cards
nonmember = member == False

mem_info = contact_info[member]
non_info = contact_info[nonmember]

mem_info.to_csv(campus+'_mem_contact.csv',index=False)
non_info.to_csv(campus+'_nonmem_contact.csv',index=False)

writer = pd.ExcelWriter(campus+'_contact.xlsx',engine='xlsxwriter')
contact_info.to_excel(writer,sheet_name='Sheet1')
workbook = writer.book
worksheet = writer.sheets['Sheet1']

format1 = workbook.add_format({'bg_color': '#FFC7CE','font_color': '#9C0006'})

start_row = 1
start_col = 1
end_row = len(contact_info)
end_cold = start_col

worksheet.conditional_format(start_row, start_col, end_row, end_cold,
                             {'type':     'cell',
                              'criteria': non_info,
                              'value':    True,
                              'format':   format1})
writer.save()