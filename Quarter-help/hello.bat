@echo off
call :inputbox "Enter the name of the raw data file:" "Box Title"
:inputbox
set input=
set heading=%~2
set message=%~1
echo wscript.echo inputbox(WScript.Arguments(0),Wscript.Arguments(1)) >"%temp%\input.vbs"
for /f "tokens=* delims=" %%a in ('cscript //nologo "%temp%\input.vbs" "%message%" "%heading%"') do set input=%%a
powershell.exe %HOMEDRIVE%%HOMEPATH%\Desktop\Portable\App\python.exe %HOMEDRIVE%%HOMEPATH%\Desktop\Portable\Quarter-help\new.py %1 %HOMEDRIVE%%HOMEPATH%\Desktop\Portable\Quarter-helptemp.csv
.\temp.csv
exit \b