class WRITE_POINT:
    def __init__(self, stack):
        self.phase = 0
        self.ip = 0
        self.stack = stack
        self.addr = 0
        self.data = 0

    def exec(self, ip):
        if (self.phase == 0):
            self.ip = ip
            self.addr = self.stack.pop()
            self.phase = 1
            return False
        else:
            assert(self.phase == 1)
            self.data = self.stack.pop()
            self.phase = 0
            return True
