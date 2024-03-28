#21 keylogger in toulse in python
import keyboard
keys = keyboard.record(until='1')
keyboard.play(keys)