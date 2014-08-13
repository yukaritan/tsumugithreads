#!/usr/bin/env python3.4

from concurrent.futures.thread import ThreadPoolExecutor

from ircbotmock import IRCBotMock
from omeglemock import OmegleMock


ircbot = IRCBotMock()
omegle = OmegleMock()

ircbot.set_omegle(omegle)
omegle.set_ircbot(ircbot)

try:
    with ThreadPoolExecutor(2) as tpe:
        tpe.submit(ircbot.start)
        tpe.submit(omegle.start)

except KeyboardInterrupt:
    ircbot.stop()
    omegle.stop()