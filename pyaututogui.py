import pyaututogui
import time

print(pyaututogui.position())
time.sleep(3)
pyaututogui.moveTo(500, 500, 2)