from time import sleep


class OmegleMock:
    def __init__(self):
        self._running = True
        self._ircbot = None

    def set_ircbot(self, ircbot):
        self._ircbot = ircbot

    def start(self):
        while self._running:
            self._ircbot.send_to_channel("things from omegle")
            sleep(5)
        print("OmegleMock exits")

    def send(self, message: str):
        print("OmegleMock.send('%s')" % message)

    def stop(self):
        self._running = False
