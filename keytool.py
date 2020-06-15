import os

window=33555185

def txt_to_keysym(txt):

    s = ''

    keysym = {
         ' ': 'space',
         '!': 'exclam',
         '"': 'quotedbl',
         '#': 'numbersign',
         '$': 'dollar',
         '%': 'percent',
         '&': 'ampersand',
         "'": 'quoterigt',
         '(': 'parenleft',
         ')': 'parenright',
         '[': 'bracketleft',
         '*': 'asterisk',
         '\\': 'backslash',
         '+': 'plus',
         ']': 'bracketright',
         '': 'comma',
         '^': 'asciicircum',
         '-': 'minus',
         '_': 'underscore',
         '.': 'period',
         '`': 'quoteleft',
         '/': 'slash',
         ':': 'colon',
         ';': 'semicolon',
         '<': 'less',
         '=': 'equal',
         '>': 'greater',
         '?': 'question',
         '@': 'at',
         '{': 'braceleft',
         '|': 'bar',
         '}': 'braceright',
         '~': 'asciitilde',
         '\x08': 'BackSpace',
         '\n': 'Return'}

    for i in txt:
        if keysym.get(i):
            s += ' ' + keysym[i]
        else:
            s += ' ' + i

    return s[1:]

def write(txt):
    aux = txt_to_keysym(txt + '\n')
    os.system('xdotool key --window {} {}'.format(window, aux))

def send_command(cmmd):
    write('koya ' + cmmd)
