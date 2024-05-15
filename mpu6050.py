class AccelerometerInstance:
    def __init__(self, rx):
        self.xAccel = -1
        self.yAccel = -1
        self.zAccel = -1

    def _Handling(self):
        pass

    def GetData(self):
        self._Handling()
        return {
                    "x": self.xAccel,
                    "y": self.yAccel,
                    "z": self.zAccel
                }


class GyroscopeInstance:
    def __init__(self, rx):
        self.xGyro = -1
        self.yGyro = -1
        self.zGyro = -1

    def _Handling(self):
        pass

    def GetData(self):
        self._Handling()
        return {
                    "x": self.xGyro,
                    "y": self.yGyro,
                    "z": self.zGyro
                }
