
class StateMachineSimply:
    def __init__(self, initialState):
        self._lastState: int = -1
        self._currentState: int = initialState
        self._nextState: int = initialState
        self._traceStateNumber: int = 0
        self._traceArrLen = 100
        self._traceArray = bytearray(self._traceArrLen)

    def SetNextState(self, stateNum):
        self._nextState = stateNum

    def GetNewState(self):
        return self._nextState

    def GetCurrentState(self, asByte = False):
        if asByte:
            return (self._currentState // 256).to_bytes(1, byteorder='big')
        return self._currentState

    def _UpdateCurrentState(self):
        self._currentState = self._nextState

    def _UpdateLastState(self):
        self._lastState = self._currentState

    def GetLastStep(self):
        return self._lastState

    def _UpdateTrace(self):
        self._traceStateNumber = self._traceStateNumber % 100
        self._traceArray[self._traceStateNumber] = self._currentState
        self._traceStateNumber += 1

    def GetTraceArr(self):
        return bytearray(self._traceArray)

    def EnableTransit(self):
        if self._nextState != self._currentState:
            self._UpdateLastState()
            self._UpdateCurrentState()
            self._UpdateTrace()
            return True

        return False


