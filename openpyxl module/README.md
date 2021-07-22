# Reading writting in a excel file
**Note :** Concurrent access may give you problems 
so don't open the same file with other editor during program is running
## Importing openpyxl
```
import openpyxl
```
## Getting workbook
```
wb = openpyxl.load_workbook("data.xlsx")
```
## Getting worksheet
```
st1=wb["Sheet1"]
```
## Get value of a cell
```
print(st1.cell(1,1).value)
```
## Set value of a cell
- Save the workbook after changing
```
st1.cell(1,1).value="name"
```
## Count maximum feeded row
```
print(st1.max_row)
```
## To save 
```
wb.save("data.xlsx")
```