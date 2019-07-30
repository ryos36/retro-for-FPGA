class ZERO_POP_RETURN:
    def __init__(self, stack, address):
        self.phase = 0
        self.ip = 0
        self.stack = stack
        self.address = address

    def exec(self, ip):
        if (self.phase == 0):
            if self.stack.top == 0:
                self.phase = 1
                self.stack.pop()
                self.ip = self.address.pop()
                return False
            else:
                self.ip = ip
                return True
        else:
            assert(self.phase == 1)
            self.phase = 0
            return True
