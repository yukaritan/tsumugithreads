from time import sleep


class IRCBotMock:
    def __init__(self):
        self._running = True
        self._omegle = None

    def set_omegle(self, omegle):
        self._omegle = omegle

    def send_to_channel(self, message: str):
        print("IRCBotMock.send_to_channel('%s')" % message)

    def send_to_omegle(self, message: str):
        print("IRCBotMock.send_to_omegle('%s')" % message)
        self._omegle.send(message)

    def start(self):
        while self._running:
            self.send_to_omegle("things from irc")
            sleep(3)
        print("IRCBotMock exits")


    def stop(self):
        self._running = False
