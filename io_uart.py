from polyphony import testbench
from polyphony.typing import bit32, List
from io_device import tx_char, rx_char, flush

def test_io_uart(io:List[bit32]):
    print("START")
    tx_char(io, 0x41)
    print("SEC")
    tx_char(io, 0x61)
    print("THER")
    tx_char(io, 0x31)
    print("FOR")
    tx_char(io, 0x39)
    print("X")
    flush(io)
    print("R")
    c = rx_char(io)
    print(c)

#----------------------------------------------------------------
@testbench
def test():
    io_ports = [0]*16

    test_io_uart(io_ports)

if __name__ == "__main__":
    test()
