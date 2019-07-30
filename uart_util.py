import polyphony
from polyphony import is_worker_running
from polyphony.io import Port
from polyphony.typing import bit, bit8
from polyphony.timing import clksleep, clkfence, wait_value

@polyphony.module
class UartBridge:
    def __init__(self):
        self.rx_data = Port(bit8, 'in')
        self.rx_ready = Port(bit, 'in')
        self.rx_idle = Port(bit, 'in')

        self.tx_start = Port(bit, 'out', 0)
        self.tx_data = Port(bit8, 'out', 0)
        self.tx_busy = Port(bit, 'in')

    def tx_char(self, char_c):
        wait_value(0, self.tx_busy)
        self.tx_data.wr(char_c)
        self.tx_start.wr(1)
        clkfence()
        wait_value(1, self.tx_busy)
        self.tx_start.wr(0)

    def flush_tx(self):
        wait_value(0, self.tx_busy)

    def rx_char(self):
        wait_value(1, self.rx_ready)
        data:bit8 = self.rx_data.rd()

        return data
