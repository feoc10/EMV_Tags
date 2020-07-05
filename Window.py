import PySimpleGUI as sg


class Window:
    def __init__(self):
        # layout
        self.layout = [
            [sg.Text("EMV TAG Decoder")],
            [sg.Text("Tag and Value"), sg.Input("", key='Tag', size=(40, 1))],
            [sg.Button("Decoder", key='Decoder')],
            [sg.Output(size=(70, 20), key='Result')]
        ]
        # window
        self.window = sg.Window("EMV Tag Decoder", self.layout, element_justification='c')
