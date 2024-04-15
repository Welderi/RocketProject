from StateMachineEventPassive import *
from globalData import *
from LoRaCommunication import *




def smAction(sm):
    if not isinstance(sm, StateMachineSimply):
        raise TypeError("Input must be a StateMachineSimply")

    if sm.GetCurrentState() == G_CONST_STATE1_INIT:
        # state1_INIT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE10_DEFAULT:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE20_SYS_CHECKIN:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE30_READY:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE40_LAUNCHING:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE50_FLYING_ACTIVE:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE60_PARACHUTING:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE70_FLYING_PASSIVE:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE201_ERROR1:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE202_ERROR2:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE203_ERROR3:
        # state10_DEFAULT()
        pass
    elif sm.GetCurrentState() == G_CONST_STATE204_ERROR4:
        # state10_DEFAULT()
        pass


def smTransit(sm):
    if not isinstance(sm, StateMachineSimply):
        raise TypeError("Input must be a StateMachineSimply")

    if sm.GetCurrentState() == G_CONST_STATE1_INIT:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE10_DEFAULT:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE20_SYS_CHECKIN:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE30_READY:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE40_LAUNCHING:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE50_FLYING_ACTIVE:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE60_PARACHUTING:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE70_FLYING_PASSIVE:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE201_ERROR1:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE202_ERROR2:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE203_ERROR3:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    elif sm.GetCurrentState() == G_CONST_STATE204_ERROR4:
        if G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE10_DEFAULT)
        elif not G_CONST_TRUE:
            sm.SetNextState(G_CONST_STATE20_SYS_CHECKIN)
        else:
            return

    sm.EnableTransit()


def commandHandler(cmd: Command):
    if cmd == Command.command1:
        pass
    elif cmd == Command.command2:
        pass
    elif cmd == Command.command3:
        pass
    elif cmd == Command.command4:
        pass
    elif cmd == Command.command5:
        pass
    elif cmd == Command.command6:
        pass
    elif cmd == Command.command7:
        pass
    elif cmd == Command.command8:
        pass

def cycleLoop():
    loRa = LoRaInstance()
    sm = StateMachineSimply(initialState=G_CONST_STATE1_INIT)

    while True:
        # **************  GS's Input Handling   **************
        loRa.ReceiveData()
        receivedRawData = loRa.GetReceivedData()
        inputHandler = ReceivedMessageHandler(receivedRawData)  # Input handling
        cmd = inputHandler.GetCommandNum()  # Received command
        liveByte = inputHandler.GetLiveByte()  # Received liveByte

        # Handling input command:
        commandHandler(cmd)

        # **************  Sensor's Input Handling   **************


        # **************  State machine handling   **************
        # Transition:
        smTransit(sm)
        # Action:
        smAction(sm)

        # **************  Output Handling   **************

        # Clearing:
        del(inputHandler)
def main():



    cycleLoop()


if __name__ == "__main__":
    asyncio.run(main())