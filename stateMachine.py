from globalData import *

# Functions for each state handling:
def state1_INIT():  # Initialization State

    statusByte = 0x0
    stateByte = 0x0

    qDataByte1 = 0x0
    qDataByte1 = 0x0
    qDataByte1 = 0x0
    qDataByte1 = 0x0
    qDataByte1 = 0x0


def state10_DEFAULT():  # Default State
    pass


def state20_SYS_CHECKIN():  # System checking State
    pass


def state30_READY():  # System is ready State
    pass


def state40_LAUNCHING():  # Launching State
    pass


def state50_FLYING_ACTIVE():  # Flying (active phase) State
    pass


def state60_PARACHUTING():  # Parachute dropping State
    pass


def state70_FLYING_PASSIVE():  # Flying (passive phase) State
    pass


def stateError201_TYPE1():  # Error 1 Executing State
    pass


def stateError202_TYPE2():  # Error 2 Executing State
    pass


def stateError203_TYPE3():  # Error 3 Executing State
    pass


def stateError204_TYPE4():  # Error 4 Executing State
    pass


# Transition handling function:
def transitionHandler():
    if state == G_CONST_STATE1_INIT:
        state1_INIT()
    elif state == G_CONST_STATE10_DEFAULT:
        state10_DEFAULT()
    elif state == G_CONST_STATE20_SYS_CHECKIN:
        state10_DEFAULT()
    elif state == G_CONST_STATE30_READY:
        state10_DEFAULT()
    elif state == G_CONST_STATE40_LAUNCHING:
        state10_DEFAULT()
    elif state == G_CONST_STATE50_FLYING_ACTIVE:
        state10_DEFAULT()
    elif state == G_CONST_STATE60_PARACHUTING:
        state10_DEFAULT()
    elif state == G_CONST_STATE70_FLYING_PASSIVE:
        state10_DEFAULT()
    elif state == G_CONST_STATE201_ERROR1:
        state10_DEFAULT()
    elif state == G_CONST_STATE202_ERROR2:
        state10_DEFAULT()
    elif state == G_CONST_STATE203_ERROR3:
        state10_DEFAULT()
    elif state == G_CONST_STATE204_ERROR4:
        state10_DEFAULT()
