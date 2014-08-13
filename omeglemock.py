from time import sleep
from main import IRCBotMock


class OmegleMock:
    def __init__(self):
        self._running = True
        self._ircbot = None

    def set_ircbot(self, ircbot: IRCBotMock):
        self._ircbot = ircbot

    def start(self):
        while self._running:
            print("Mocked Omegle class is sending things to the IRC bot")
            self._ircbot.send_to_channel("things from omegle")
            sleep(5)

    def send(self, message: str):
        print("Mocked Omegle class is sending this to the internet:", message)