#!/usr/bin/env python3.4

from concurrent.futures.thread import ThreadPoolExecutor
from omeglemock2 import OmegleMock


def send_to_channel(message: str):
    print("send_to_channel('%s')" % message)


# OmegleMock2 doesn't have a reference to an ircbot
# but it still needs to know how to send stuff,
# so we'll pass a reference to our send_to_channel
# function instead.
omegle = OmegleMock(send_to_channel)

try:
    with ThreadPoolExecutor(2) as tpe:
        tpe.submit(omegle.start)

        while True:
            text = input("Enter some text: ")
            tpe.submit(omegle.send, text)

except KeyboardInterrupt:
    omegle.stop()