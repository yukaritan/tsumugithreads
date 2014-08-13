from time import sleep
from main import ircbot
from omeglemock import OmegleMock


class IRCBotMock:
    def __init__(self):
        self._running = True
        self._omegle = None

    def set_omegle(self, omegle: OmegleMock):
        self._omegle = ircbot

    def send_to_channel(self, message: str):
        print("sending message to channel:", message)

    def send_to_omegle(self, message: str):
        print("sending message to omegle:", message)

    def start(self):
        print("Mocked Omegle class is sending things to the IRC bot")
        self._omegle.send("things from irc")
        sleep(5)