import pyautogui
import time

#sleeptime = 1
sleeptime = float(input('please enter sleep time(in minute):'))
print('')

while sleeptime == 0 or sleeptime < 0.5:
    sleeptime = float(input('Dear user, Sleep time should be more than or equal to 0.5:'))
    print('')

if sleeptime < 1:
    print('ok sir, i will move your mouse after every', sleeptime * 60, 'seconds')
elif sleeptime == 1:
    print('ok sir, i will move your mouse after every', sleeptime, 'minute')
else:
    print('ok sir, i will move your mouse after every', sleeptime, 'minutes')

    while True:
        time.sleep(sleeptime * 60)
    for i in range(50, 100):
        pyautogui.moveTo(250, i * 5)
