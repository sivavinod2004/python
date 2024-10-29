"""""
AUTHOR:DENNIS TAGI
DATE=08/10/2024
PYTHON PROGRAM TO DISPLAY time and date in various formats
"""
from calendar import month
from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%d,%m,%Y")
print(format3)
format4=current_time.strftime("%d,%m,%Y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format5)
format6=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format6)
format8=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format8)
date=current_time.strftime("%d")
print(date)
time=current_time.strftime("%H:%M:%S")
print(time)
month=current_time.strftime("%m")
print(month)
year=current_time.strftime("%Y")
print(year)