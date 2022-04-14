# GSEU-Email-List_dev

## Inputs
____
### From Broadstripes:
All files must be .csv format
* Non-Members report using Amy's template with the title Unit_Nonmem.csv
* Members report using Amy's template with the title Unit_Members.csv

If other file names want to be used, change lines 10 and 14 from `unit_mem = pd.read_csv('Unit_Members.csv')` or `unit_nm = pd.read_csv('Unit_Nonmem.csv')`
to `unit_mem = pd.read_csv('Insert filename here.csv')` or `unit_nm = pd.read_csv('Insert File name here.csv')` The files must still be .csv files.

### To compare
A .csv file named Unit_list.csv. The file should be a compiled GOER/HR list that is kept up.
* A column of last names called "First Name" and "Last Name" (note capitalization)
* Other columns that are filtered for are (note capitalization):
  * First Name
  * Middle Name
  * Last Name
  * Nickname
  * Employer
  * Department
  * Dues Status
  * Member Card Received
  * Personal Email
  * Business Email
  * Employer
* Any other column names will be dropped

## Outputs
_____
Will output a file named Missing_Names.csv that *should* be every missing name in Broadstripes with some basic identifying info

## Current Issues
______
* Will say that misspelled names are not found on Broadstripes
* 