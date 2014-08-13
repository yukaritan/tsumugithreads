from time import sleep


class OmegleMock:
    def __init__(self, send_to_channel):
        self._running = True
        self._send_to_channel = send_to_channel

    def start(self):
        while self._running:
            self._send_to_channel("things from omegle")
            sleep(5)
        print("OmegleMock exits")

    def send(self, message: str):
        print("OmegleMock.send('%s')" % message)

    def stop(self):
        self._running = False
