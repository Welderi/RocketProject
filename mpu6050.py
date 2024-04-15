class AccelerometerInstance:
    def __init__(self, rx):
        self.xAccel: int = -1
        self.yAccel: int = -1
        self.zAccel: int = -1

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
        self.xGyro: int = -1
        self.yGyro: int = -1
        self.zGyro: int = -1

    def _Handling(self):
        pass

    def GetData(self):
        self._Handling()
        return {
                    "x": self.xGyro,
                    "y": self.yGyro,
                    "z": self.zGyro
                }
