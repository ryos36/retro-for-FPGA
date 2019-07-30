from polyphony import testbench
from polyphony import module
from polyphony.io import Queue, Port
from polyphony.typing import bit32
from polyphony import is_worker_running
from polyphony.timing import clksleep, wait_value, clkfence

STATUS_IO_PORT = 0
STATUS_BUSY_FLAG = 0x80000000

CMD_IO_PORT = 1
IO_CMD_NOP     = 0x00000000
IO_CMD_TX_UART = 0x00000001
IO_CMD_RX_UART = 0x00000002
IO_CMD_TX_FLUSH_UART = 0x00000003

IO_CMD_REPLY_FLAG = 0x80000000

IO_ID_PORT = 2 # Reserved for Future
UART_IO_PORT = 3

DEBUG_PORT0 = 8
DEBUG_PORT1 = 9

from uart_util import UartBridge

@module
class uart_cmd_server:
    def __init__(self):
        self.status_port = Port(bit32, 'out', init = STATUS_BUSY_FLAG)
        self.cmd_in = Port(bit32, 'in')
        self.cmd_reply = Port(bit32, 'out', init = 0)
        self.uart_data_in = Port(bit32, 'in')
        self.uart_data_out = Port(bit32, 'out')

        self.uart_bridge = UartBridge()
        self.append_worker(self.worker)

    def worker(self):
        self.status_port.wr(0)
        data:bit32 = 0
        while is_worker_running():
            while True:
                cmd:bit32 = self.cmd_in.rd()
                if cmd != IO_CMD_NOP:
                    self.status_port.wr(STATUS_BUSY_FLAG)
                    break
            
            if cmd == IO_CMD_TX_UART:
                data = self.uart_data_in.rd()
                self.uart_bridge.tx_char( data & 0xFF )
            elif cmd == IO_CMD_RX_UART:
                data = self.uart_bridge.rx_char()
                self.uart_data_out.wr(data & 0xFF)
            elif cmd == IO_CMD_TX_FLUSH_UART:
                self.uart_bridge.flush_tx()

            data = IO_CMD_REPLY_FLAG | cmd
            self.cmd_reply.wr( data )
            self.status_port.wr(0)
            while True:
                cmd = self.cmd_in.rd()
                if cmd == IO_CMD_NOP:
                    break
            data = IO_CMD_REPLY_FLAG | IO_CMD_NOP
            self.cmd_reply.wr( data )

@testbench
def test(m):
    clksleep(100)

if __name__ == '__main__':
    m = uart_cmd_server()
    test(m)
