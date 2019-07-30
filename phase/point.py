class POINT:
    def __init__(self, stack):
        self.phase = 0
        self.ip = 0
        self.ip_saved = 0
        self.stack = stack

    def exec(self, ip, data):
        if (self.phase == 0):
            self.ip_saved = ip
            self.ip = self.stack.top
            self.phase = 1
            return False
        elif (self.phase == 1):
            self.phase = 2
            return False
        elif (self.phase == 2):
            self.ip = self.ip_saved
            self.stack.top = data
            self.stack.sync_top()
            self.phase = 3
            return False
        else:
            assert(self.phase == 3)
            self.phase = 0
            return True
