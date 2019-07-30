#!/usr/bin/env python

from polyphony import testbench

#----------------------------------------------------------------
def exec():
    phase = 0
    ip = 0
    while True:
        if (phase == 0):
            ip = ip + 1
            if ip == 2:
                phase += 1
            else:
                phase = 4
        elif (phase == 1):
            phase += 1
        elif (phase == 2):
            phase += 1
        elif (phase == 3):
            return False
        else:
            return True
            

#----------------------------------------------------------------
@testbench
def test():
    exec()

if __name__ == "__main__":
    test()
