from flask import Flask, render_template
from pynput.keyboard import Key, Controller

app = Flask(__name__)
kb = Controller()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Crl/KbLeft', methods=['GET'])
def keyboard_left():
    print('[CONTROL] Simulated Left Button is Pressing...')
    kb.press(Key.left)
    kb.release(Key.left)
    return 'finish left'


@app.route('/Crl/KbRight', methods=['GET'])
def keyboard_right():
    print('[CONTROL] Simulated Right Button is Pressing...')
    kb.press(Key.right)
    kb.release(Key.right)
    return 'finish right'


@app.route('/Crl/KbSpace', methods=['GET'])
def keyboard_space():
    print('[CONTROL] Simulated Space Bar is Pressing...')
    kb.press(Key.space)
    kb.release(Key.space)
    return 'finish space'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
