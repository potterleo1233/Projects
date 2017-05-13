@echo off
echo "Working on Files."
for /r %%i in (.\Input\*.txt) do powershell.exe .\python36\python.exe .\ispcondense.py %%i
for /r %%i in (.\Input\*.csv) do move %%i .\Output\
echo "Check the Output folder for your csv files"
pause



