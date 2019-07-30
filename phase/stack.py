#!skip

class retro_stack:
    def __init__(self, mem):
        self.pos = 0
        self.top = 0
        self.second = 0
        self.mem = mem
        self.debug = 0

    def pop(self):
        if self.debug:
            assert(self.pos >= 1)
        rv = self.top
        self.top = self.second
        self.pos -= 1
        self.second = self.mem[self.pos - 2]
        return rv

    def push(self, v):
        if self.debug:
            assert(self.pos < len(self.mem))
            self.mem[self.pos] = v
        self.mem[self.pos - 2] = self.second
        self.second = self.top
        self.top = v
        self.pos += 1

    def swap(self):
        if self.debug:
            a = self.mem[self.pos - 2]
            self.mem[self.pos - 2] = self.mem[self.pos - 1]
            self.mem[self.pos - 1] = a
        (self.top, self.second) = (self.second, self.top)

    def length(self):
        return len(self.mem)

    def sync_top(self):
        if self.debug:
            self.mem[self.pos - 1] = self.top

    def sync_second(self):
        if self.debug:
            self.mem[self.pos - 2] = self.second

    def sync(self):
        if self.debug:
            self.mem[self.pos - 1] = self.top
            self.mem[self.pos - 2] = self.second

    def check(self):
        assert( self.top == self.mem[self.pos - 1] )
        assert( self.second == self.mem[self.pos - 2] )

#    def __str__(self):
#        return f'{self.top} {self.second}';


