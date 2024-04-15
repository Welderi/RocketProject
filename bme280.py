class BarometerInstance:
    def __init__(self, rx):
        self._temperature: int = -1
        self._pressure: int = -1
        self._humidity: int = -1

    def _Handling(self):
        pass

    def GetData(self):
        self._Handling()
        return {
                    "temperature": self._temperature,
                    "pressure": self._pressure,
                    "humidity": self._humidity
                }
