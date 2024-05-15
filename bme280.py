class BarometerInstance:
    def __init__(self, rx):
        self._temperature = -1
        self._pressure = -1
        self._humidity = -1

    def _Handling(self):
        pass

    def GetData(self):
        self._Handling()
        return {
                    "temperature": self._temperature,
                    "pressure": self._pressure,
                    "humidity": self._humidity
                }
