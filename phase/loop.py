class LOOP:
    def __init__(self, stack):
        self.phase = 0
        self.ip = 0
        self.stack = stack

    def exec(self, ip, data):
        if (self.phase == 0):
            self.stack.top -= 1
            self.stack.sync_top()

            self.ip = ip + 1
            if self.stack.top != 0 and self.stack.top > -1:
                self.phase = 1
            else:
                self.stack.pop()
                self.phase = 0
                return True
        elif (self.phase == 1):
            self.phase = 2
            return False
        elif (self.phase == 2):
            self.ip = data - 1
            self.phase = 3
            return False
        else:
            assert(self.phase == 3)
            self.phase = 0
            return True
