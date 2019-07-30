class JUMP_EQ:
    def __init__(self, stack):
        self.phase = 0
        self.ip = 0
        self.stack = stack
        self.a = 0

    def exec(self, ip, data):
        if (self.phase == 0):
            self.ip = ip + 1
            self.a = self.stack.pop()
            self.phase = 1
            return False
        elif (self.phase == 1):
            b = self.stack.pop()
            if b == self.a:
                self.phase = 2
                return False
            else:
                self.phase = 0
                return True
        elif (self.phase == 2):
            self.ip = data - 1
            self.phase = 3
            return False
        else:
            assert(self.phase == 3)
            self.phase = 0
            return True
