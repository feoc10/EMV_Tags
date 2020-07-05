from Decoder import Decoder
from Window import Window

window = Window()
decoder = Decoder()
while True:
    event, values = window.window.Read()

    if event is None or event == 'Exit':
        break

    if event == 'Decoder':
        decoder.decoder_tag(window, values)
