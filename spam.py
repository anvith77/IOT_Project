import pyautogui
import time

msg = str(input("Enter your Message :"))
n = int(input("Enter the number of times"))

time.sleep(10)

for i in range(0,n):
    pyautogui.typewrite(msg+'\n')
    
