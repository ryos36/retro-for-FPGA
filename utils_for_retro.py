from polyphony import testbench
from polyphony.typing import int32, bit32

EXIT = 16384
INPUT_INC = 4
DEC = 2
MEMORY_SIZE = 16384

# -----------------------------------------------------------------------------
def abs(a):
    return -a if a < 0 else a

def find_zero_len(x:bit32):
    test_bit:bit32 = 0x40000000
    n = 0
    for i in range(31): 
        if test_bit & x:
            return n
        test_bit >>= 1
        n += 1
    return 0

def retro_divmod(a, b):
    sign_a = 1 if a & 0x80000000 else 0
    sign_b = 1 if b & 0x80000000 else 0
    abs_a = a & 0x7FFFFFFF
    abs_b = b & 0x7FFFFFFF
    abs_a_zero_len = find_zero_len(abs_a)
    abs_b_zero_len = find_zero_len(abs_b)
    #print(abs_a_zero_len, abs_b_zero_len)
    c_bit:int32 = 0
    abs_b <<= abs_b_zero_len
    #print(abs_a, abs_b)
    for i in range(abs_b_zero_len+1):
        if abs_a >= abs_b:
            c_bit <<= 1
            c_bit |= 1
            abs_a -= abs_b
        else:
            c_bit <<= 1
        abs_b >>= 1

    if sign_a:
        abs_a |= 0x80000000
    if sign_a ^ sign_b:
        c_bit |= 0x80000000

    return c_bit, abs_a

#----------------------------------------------------------------
def deprecated_skip_nop( memory:list, ip ):
    next_v:bit32 = memory[ip + 1]
    if next_v == 0:
        ip += 1
        next_v = memory[ip + 1]
        if next_v == 0:
            ip += 1
    return ip

@testbench
def test():
    #lst = [4, 5, 4001, 7]
    old_e = 2903
    #for e in lst:
    e = 7
    (ra, rb) = retro_divmod(old_e, e)
    print(old_e, '/', e , '=>', ra, '...', rb)

    old_e = e

if __name__ == "__main__":
    test()
