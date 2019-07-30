class JUMP:
    def __init__(self):
        self.phase = 0
        self.ip = 0

    def exec(self, ip, data):
        if (self.phase == 0):
            self.ip = ip + 1
            self.phase = 1
            return False
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
