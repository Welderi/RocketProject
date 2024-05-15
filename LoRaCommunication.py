from enum import Enum
from globalData import *
import os
import time
from pyLora import LoRa


def ByteFromInt(byteNum=0, intVal: int=0):
    if byteNum == 0:
        return intVal & 0xFF
    elif byteNum == 1:
        return (intVal >> 8) & 0xFF
    elif byteNum == 2:
        return (intVal >> 16) & 0xFF
    elif byteNum == 3:
        return (intVal >> 24) & 0xFF
    else:
        return None


def Byte2Bytearray(byteArr: bytearray, byteNum: int=0, byteVal: int=0):
    if isinstance(byteArr, bytearray) and byteNum < len(byteArr):
        byteArr[byteNum] = byteVal & 0xFF
        return True
    return False


class MessageToSendType(Enum):
    INIT = 0xFF
    temperature1 = 0x11
    xAccel = 0x12
    yAccel = 0x13
    zAccel = 0x14
    xGyro = 0x15
    yGyro = 0x16
    zGyro = 0x17
    temperature2 = 0x18
    pressure = 0x19
    humidity = 0x1A
    status = 0x20


class StatusToSendType(Enum):
    status1 = 0x21
    status2 = 0x22
    status3 = 0x23
    status4 = 0x24
    status5 = 0x25
    status6 = 0x26
    status7 = 0x27
    status8 = 0x28


class AlarmToSendType(Enum):
    alarm1 = 0x31
    alarm2 = 0x32
    alarm3 = 0x33
    alarm4 = 0x34
    alarm5 = 0x35
    alarm6 = 0x36
    alarm7 = 0x37
    alarm8 = 0x38


class StateToSendType(Enum):
    state1 = 0x41
    state2 = 0x42
    state3 = 0x43
    state4 = 0x44
    state5 = 0x45
    state6 = 0x46
    state7 = 0x47
    state8 = 0x48


class Command(Enum):
    command1 = 0x51
    command2 = 0x52
    command3 = 0x53
    command4 = 0x54
    command5 = 0x55
    command6 = 0x56
    command7 = 0x57
    command8 = 0x58


class LoRaInstance:
    def __init__(self):
        self.lora = LoRa(0, 17, 1)
        self.lora.set_frequency(433000000)

        self._buffer = bytearray(4)
        self._bufferCurrentPos = 0
        self._dataToSend = bytearray(8)

    def write_to_file(self, data):
        try:
            with open("output.txt", "a") as file:
                file.write(data + "\n")
        except Exception as e:
            print(f"{e}")

    def SendData(self, packet: bytearray):
        self._dataToSend = packet

        self.lora.set_mode_idle()
        self.lora.write_payload(self._dataToSend)
        self.lora.set_mode_tx()
        while not self.lora.get_irq_flags()['tx_done']:
            time.sleep(0.1)
        self.lora.set_mode_idle()
        self.lora.collect_garbage()

    def ReceiveData(self):
        while True:
            if self.lora.received_packet():
                data_byte = self.lora.read_payload()[0]
                self._buffer[self._bufferCurrentPos] = data_byte
                self._bufferCurrentPos += 1
                if self._bufferCurrentPos == len(self._buffer):
                    data_str = ''.join(format(x, '02x') for x in self._buffer)
                    write_to_file(data_str) 
                    self._bufferCurrentPos = 0
                    return
            time.sleep(0.1)

    def _ValidateReceivedData(self):
        return (self._buffer[0] == 36) & (self._buffer[-1] == 42)

    def GetReceivedData(self):
        if self._ValidateReceivedData():
            return self._buffer
        return None


class MessageToSendFormater:
    def __init__(self, messageType: MessageToSendType, dataToSend: int):
        self._startSymbol = 36  # $
        self._messageType = messageType
        self._data = dataToSend
        self._liveByte = None
        self._endSymbol = 42  # *

        self._message = bytearray(8)

        self._MessageFormating()

    def _MessageFormating(self):
        self._message[0] = self._startSymbol
        self._message[1] = ByteFromInt(0, self._messageType.value)
        self._message[2] = ByteFromInt(0, self._data)
        self._message[3] = ByteFromInt(1, self._data)
        self._message[4] = ByteFromInt(2, self._data)
        self._message[5] = ByteFromInt(3, self._data)
        self._message[6] = G_LIVEBYTE
        self._message[7] = self._endSymbol

    def GetFormatedMessage(self):
        return self._message


class ReceivedMessageHandler:
    def __init__(self, rawMessage: bytearray):
        self._raw = rawMessage

    def Get(self):
        pass