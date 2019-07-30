class LIT:
    def __init__(self, stack):
        self.phase = 0
        self.ip = 0
        self.stack = stack

    def exec(self, ip, data):
        if (self.phase == 0):
            self.ip = ip + 1
            self.phase = 1
            return False
        elif (self.phase == 1):
            self.phase = 2
            return False
        else:
            assert(self.phase == 2)
            self.phase = 0
            self.stack.push(data)
            return True
            
