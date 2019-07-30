from polyphony import testbench
from stack import retro_stack

# -----------------------------------------------------------------------------
def test_for_stack(_mem):
    s = retro_stack(_mem)
    s.push(3)
    s.push(4)
    s.push(5)
    print('top:', s.top, 'second:', s.second)
    s.swap()
    print('top:', s.top, 'second:', s.second)
    for i in range(8):
        print(i, _mem[i])
    print('pop:', s.pop())
    print('top:', s.top, 'second:', s.second, s.pos)
    s.check()
    s.swap()
    for i in range(8):
        print(i, _mem[i])
    print('top:', s.top, 'second:', s.second, s.pos)
    #s.check()
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(s.top)
    print('-------', s.top, s.second)
    for i in range(s.pos):
        print(i, _mem[i])

# -----------------------------------------------------------------------------
@testbench
def test():
    mem = [0] * 8
    test_for_stack(mem)

if __name__ == '__main__':
    test()
