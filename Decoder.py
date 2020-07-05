from typing import Any

import PySimpleGUI


class Decoder:
    def __init__(self):
        self.tag_dict = {'95': self.TVR, '9f33': self.Capabities, '9f34': self.CVMResults}

    def decoder_tag(self, window: PySimpleGUI, values: dict):
        tag_value = values['Tag']
        if tag_value[1].lower() == 'f':
            tag = tag_value[:4].lower()
        else:
            tag = tag_value[:2].lower()

        try:
            func = self.tag_dict[tag]
            func(window, tag_value)
        except Exception as e:
            window.window['Result'].update("Tag not found")

    def TVR(self, window: PySimpleGUI, tag_value):
        value = tag_value[4:]
        if len(value) != 10:
            window.window['Result'].update("TVR must have 5 bytes")
        else:
            result = "{0:040b}".format(int(value, 16))
            aux = "Tag 95 - TVR\n "
            if result[0] == '1':
                aux += '(Byte 1 Bit 8) Offline data authentication was not performed\n '
            if result[1] == '1':
                aux += '(Byte 1 Bit 7) SDA failed\n '
            if result[2] == '1':
                aux += '(Byte 1 Bit 6) ICC data missing\n '
            if result[3] == '1':
                aux += '(Byte 1 Bit 5) Card appears on terminal exception file\n '
            if result[4] == '1':
                aux += '(Byte 1 Bit 4) DDA failed\n '
            if result[5] == '1':
                aux += '(Byte 1 Bit 3) CDA failed\n '
            if result[6] == '1':
                aux += '(Byte 1 Bit 2) SDA selected\n '
            if result[7] == '1':
                aux += '(Byte 1 Bit 1) RFU\n '
            if result[8] == '1':
                aux += '(Byte 2 Bit 8) ICC and terminal have different application versions\n '
            if result[9] == '1':
                aux += '(Byte 2 Bit 7) Expired application\n '
            if result[10] == '1':
                aux += '(Byte 2 Bit 6) Application not yet effective\n '
            if result[11] == '1':
                aux += '(Byte 2 Bit 5) Requested service not allowed for card product\n '
            if result[12] == '1':
                aux += '(Byte 2 Bit 4) New card\n '
            if result[13] == '1':
                aux += '(Byte 2 Bit 3) RFU\n '
            if result[14] == '1':
                aux += '(Byte 2 Bit 2) RFU\n '
            if result[15] == '1':
                aux += '(Byte 2 Bit 1) RFU\n '
            if result[16] == '1':
                aux += '(Byte 3 Bit 8) Cardholder verification was not successful\n '
            if result[17] == '1':
                aux += '(Byte 3 Bit 7) Unrecognised CVM\n '
            if result[18] == '1':
                aux += '(Byte 3 Bit 6) PIN try limit exceeded\n '
            if result[19] == '1':
                aux += '(Byte 3 Bit 5) PIN entry required and PIN pad not present or not working\n '
            if result[20] == '1':
                aux += '(Byte 3 Bit 4) PIN entry required, PIN pad present, but PIN was not entered\n '
            if result[21] == '1':
                aux += '(Byte 3 Bit 3) Online PIN entered\n '
            if result[22] == '1':
                aux += '(Byte 3 Bit 2) RFU\n '
            if result[23] == '1':
                aux += '(Byte 3 Bit 1) RFU\n '
            if result[24] == '1':
                aux += '(Byte 4 Bit 8) Transaction exceeds floor limit\n '
            if result[25] == '1':
                aux += '(Byte 4 Bit 7) Lower consecutive offline limit exceeded\n '
            if result[26] == '1':
                aux += '(Byte 4 Bit 6) Upper consecutive offline limit exceeded\n '
            if result[27] == '1':
                aux += '(Byte 4 Bit 5) Transaction selected randomly for online processing\n '
            if result[28] == '1':
                aux += '(Byte 4 Bit 4) Merchant forced transaction online\n '
            if result[29] == '1':
                aux += '(Byte 4 Bit 3) RFU\n '
            if result[30] == '1':
                aux += '(Byte 4 Bit 2) RFU\n '
            if result[31] == '1':
                aux += '(Byte 4 Bit 1) RFU\n '
            if result[32] == '1':
                aux += '(Byte 5 Bit 8) Default TDOL used\n '
            if result[33] == '1':
                aux += '(Byte 5 Bit 7) Issuer authentication failed\n '
            if result[34] == '1':
                aux += '(Byte 5 Bit 6) Script processing failed before final GENERATE AC\n '
            if result[35] == '1':
                aux += '(Byte 5 Bit 5) Script processing failed after final GENERATE AC\n '
            if result[36] == '1':
                aux += '(Byte 5 Bit 4) RFU\n '
            if result[37] == '1':
                aux += '(Byte 5 Bit 3) RFU\n '
            if result[38] == '1':
                aux += '(Byte 5 Bit 2) RFU\n '
            if result[39] == '1':
                aux += '(Byte 5 Bit 1) RFU\n '

            window.window['Result'].update(aux)

    def Capabities(self, window: PySimpleGUI, tag_value):
        value = tag_value[6:]
        if len(value) != 6:
            window.window['Result'].update("Terminal Capabilities must have 3 bytes")
        else:
            result = "{0:024b}".format(int(value, 16))
            aux = "Tag 9F33 - Terminal Capabilities\n "
            if result[0] == '1':
                aux += '(Byte 1 Bit 8) Manual key entry\n '
            if result[1] == '1':
                aux += '(Byte 1 Bit 7) Magnetic stripe\n '
            if result[2] == '1':
                aux += '(Byte 1 Bit 6) IC with contact\n '
            if result[3] == '1':
                aux += '(Byte 1 Bit 5) (RFU)\n '
            if result[4] == '1':
                aux += '(Byte 1 Bit 4) (RFU)\n '
            if result[5] == '1':
                aux += '(Byte 1 Bit 3) (RFU)\n '
            if result[6] == '1':
                aux += '(Byte 1 Bit 2) (RFU)\n '
            if result[7] == '1':
                aux += '(Byte 1 Bit 1) (RFU)\n '
            if result[8] == '1':
                aux += '(Byte 2 Bit 8) Plaintext PIN for ICC verification\n '
            if result[9] == '1':
                aux += '(Byte 2 Bit 7) Enciphered PIN for online verificatio\n '
            if result[10] == '1':
                aux += '(Byte 2 Bit 6) Signature (paper)\n '
            if result[11] == '1':
                aux += '(Byte 2 Bit 5) Enciphered PIN for offline verification\n '
            if result[12] == '1':
                aux += '(Byte 2 Bit 4) No CVM Required\n '
            if result[13] == '1':
                aux += '(Byte 2 Bit 3) (RFU)\n '
            if result[14] == '1':
                aux += '(Byte 2 Bit 2) (RFU)\n '
            if result[15] == '1':
                aux += '(Byte 2 Bit 1) (RFU)\n '
            if result[16] == '1':
                aux += '(Byte 3 Bit 8) SDA\n '
            if result[17] == '1':
                aux += '(Byte 3 Bit 7) DDA\n '
            if result[18] == '1':
                aux += '(Byte 3 Bit 6) Card capture\n '
            if result[19] == '1':
                aux += '(Byte 3 Bit 5) (RFU)\n '
            if result[20] == '1':
                aux += '(Byte 3 Bit 4) CDA\n '
            if result[21] == '1':
                aux += '(Byte 3 Bit 3) (RFU)\n '
            if result[22] == '1':
                aux += '(Byte 3 Bit 2) (RFU)\n '
            if result[23] == '1':
                aux += '(Byte 3 Bit 1) (RFU)\n '

            window.window['Result'].update(aux)

    def CVMResults(self, window: PySimpleGUI, tag_value):
        value = tag_value[6:]
        if len(value) != 6:
            window.window['Result'].update("Cardholder Verification Results must have 3 bytes")
        else:
            result = "{0:024b}".format(int(value, 16))
            byte1 = result[:8]
            byte2 = value[2:4]
            byte3 = value[4:]
            aux = "Tag 9F33 - Terminal Capabilities\n "

            # Byte 1 - CVM Rule
            if byte1[1] == '1':
                aux += "Apply succeeding CV Rule if this CVM is unsuccessful\n "
            else:
                aux += "Fail cardholder verification if this CVM is unsuccessful\n "

            # Byte 1 - CVM process applied
            aux += 'Method: '
            if byte1[2:] == '000000':
                aux += 'Fail CVM processing\n '
            elif byte1[2:] == '000001':
                aux += 'Plaintext PIN verification performed by ICC\n '
            elif byte1[2:] == '000010':
                aux += 'Enciphered PIN verified online\n '
            elif byte1[2:] == '000010':
                aux += 'Enciphered PIN verified online\n '
            elif byte1[2:] == '000011':
                aux += 'Plaintext PIN verification performed by ICC and signature (paper)\n '
            elif byte1[2:] == '000100':
                aux += 'Enciphered PIN verification performed by ICC\n '
            elif byte1[2:] == '000101':
                aux += 'Enciphered PIN verification performed by ICC and signature (paper)\n '
            elif byte1[2:] == '011110':
                aux += 'Signature\n '
            elif byte1[2:] == '011111':
                aux += 'NoCVM Required\n '
            elif byte1[2:] == '111111':
                aux += 'This value is not available for use\n '

            # Byte 2 - Condition codes
            aux += 'Condition use: '
            if byte2 == '00':
                aux += 'Always \n '
            elif byte2 == '01':
                aux += 'If unattended cash \n '
            elif byte2 == '02':
                aux += 'If not unattended cash and not manual cash and not purchase with cashback \n '
            elif byte2 == '03':
                aux += 'If terminal supports the CVM \n '
            elif byte2 == '04':
                aux += 'If manual cash \n '
            elif byte2 == '05':
                aux += 'If purchase with cashback \n '
            elif byte2 == '06':
                aux += 'If transaction is in the application currency and is under X value \n '
            elif byte2 == '07':
                aux += 'If transaction is in the application currency and is over X value \n '
            elif byte2 == '08':
                aux += 'If transaction is in the application currency and is under Y value \n '
            elif byte2 == '09':
                aux += 'If transaction is in the application currency and is over Y value \n '
            else:
                aux += 'RFU \n '

            # Byte 3 - Result
            aux += 'Result: '
            if byte3 == '00':
                aux += 'Unknown'
            elif byte3 == '01':
                aux += 'Failed'
            elif byte3 == '02':
                aux += 'Successful'

            window.window['Result'].update(aux)

            # Byte 1 - bit8 - RFU
            if byte1[0] == '1':
                window.window['Result'].update("Byte 1 - bit8 can't be assigned - RFU")
