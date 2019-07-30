from polyphony import testbench
from polyphony.typing import int32, bit31, bit32, bit34, bit35

def find_zero_len(x:int32):
    x_30_16 = x & 0x7FFF0000
    if x_30_16 == 0:
        x_15_08 = x & 0x0000FF00
        if x_15_08 == 0:
            x_07_04 = x & 0x000000F0
            if x_07_04 == 0:
                x_03_02 = x & 0x0000000C
                if x_03_02 == 0:
                    x_01_00 = x & 0x00000003
                    if x_01_00 == 0:
                        return 31
                    elif x_01_00 == 1:
                        return 30
                    else:
                        return 29
                else:
                    x_03_03 = x & 0x00000008
                    if x_03_03 == 0:
                        return 28
                    else:
                        return 27
            else:
                x_07_06 = x & 0x000000C0
                if x_07_06 == 0:
                    x_05_05 = x & 0x00000040 
                    if x_05_05 == 0:
                        return 26
                    else:
                        return 25
                else:
                    x_07_07 = x & 0x00000080
                    if  x_07_07 == 0:
                        return 24
                    else:
                        return 23
        else:
            x_15_12 = x & 0x0000F000
            if x_15_12 == 0:
                x_11_10 = x & 0x00000C00
                if x_11_10 == 0:
                    x_09_09 = x & 0x00000200
                    if x_09_09 == 0:
                        return 22
                    else:
                        return 21
                else:
                    x_11_11 = x & 0x00000800
                    if x_11_11 == 0:
                        return 20
                    else:
                        return 19
            else:
                x_15_14 = x & 0x0000C000
                if x_15_14 == 0:
                    x_13_13 = x & 0x00002000
                    if x_13_13 == 0:
                        return 18
                    else:
                        return 17
                else:
                    x_15_15 = x & 0x00008000
                    if x_15_15 == 0:
                        return 16
                    else:
                        return 15
    else:
        x_30_24 = x & 0x7F000000
        if x_30_24 == 0:
            x_23_20 = x & 0x00F00000
            if x_23_20 == 0:
                x_19_18 = x & 0x000C0000
                if x_19_18 == 0:
                    x_17_17 = x & 0x00020000
                    if x_17_17 == 0:
                        return 14
                    else:
                        return 13
                else:
                    x_19_19 = x & 0x00080000
                    if x_19_19 == 0:
                        return 12
                    else:
                        return 11
            else:
                x_23_22 = x & 0x00C00000
                if x_23_22 == 0:
                    x_21_21 = x & 0x00400000 
                    if x_21_21 == 0:
                        return 10
                    else:
                        return  9
                else:
                    x_23_23 = x & 0x00800000
                    if  x_23_23 == 0:
                        return  8
                    else:
                        return  7
        else:
            x_30_28 = x & 0x70000000
            if x_30_28 == 0:
                x_27_26 = x & 0x0C000000
                if x_27_26 == 0:
                    x_25_25 = x & 0x02000000
                    if x_25_25 == 0:
                        return  6
                    else:
                        return  5
                else:
                    x_27_27 = x & 0x08000000
                    if x_27_27 == 0:
                        return  4
                    else:
                        return  3
            else:
                x_30_30 = x & 0x40000000
                if x_30_30 == 0:
                    x_29_29 = x & 0x20000000
                    if x_29_29 == 0:
                        return  2
                    else:
                        return  1
                else:
                    return 0

def divmod(a, b):
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

def divmod4(a, b):
    sign_a = 1 if a & 0x80000000 else 0
    sign_b = 1 if b & 0x80000000 else 0
    abs_a:bit32 = a & 0x7FFFFFFF
    abs_b:bit32 = b & 0x7FFFFFFF

    if abs_a < abs_b:
        return 0, a
    elif abs_a == abs_b:
        return -1 if sign_a ^ sign_b else 1, 0

    abs_a_zero_len = find_zero_len(abs_a)
    abs_b_zero_len = find_zero_len(abs_b)
    #print(abs_a_zero_len, abs_b_zero_len)
    c_bit:int32 = 0

    shift_n = abs_b_zero_len - abs_a_zero_len

    abs_b0:bit32 = abs_b << shift_n
    abs_b1:bit32 = abs_b0 >> 1
    abs_b2:bit32 = abs_b0 >> 2
    abs_b3:bit32 = abs_b0 >> 3
    print(abs_b0, abs_b1, abs_b2, abs_b3)

    abs_b_1111:bit32 = abs_b0 + abs_b1 + abs_b2 + abs_b3
    abs_b_1110:bit32 = abs_b0 + abs_b1 + abs_b2
    abs_b_1101:bit32 = abs_b0 + abs_b1          + abs_b3
    abs_b_1100:bit32 = abs_b0 + abs_b1
    abs_b_1011:bit32 = abs_b0          + abs_b2 + abs_b3
    abs_b_1010:bit32 = abs_b0          + abs_b2 
    abs_b_1001:bit32 = abs_b0                   + abs_b3
    abs_b_1000:bit32 = abs_b0

    abs_b_1_1111:bit = (abs_b_1111 >> 31) & 1
    abs_b_1_1110:bit = (abs_b_1110 >> 31) & 1
    abs_b_1_1101:bit = (abs_b_1101 >> 31) & 1
    abs_b_1_1100:bit = (abs_b_1100 >> 31) & 1
    abs_b_1_1011:bit = (abs_b_1011 >> 31) & 1
    abs_b_1_1010:bit = (abs_b_1010 >> 31) & 1
    abs_b_1_1001:bit = (abs_b_1001 >> 31) & 1
    abs_b_1_1000:bit = (abs_b_1000 >> 31) & 1

    abs_b___1111:bit31 = abs_b_1111 & 0x7FFFFFFF
    abs_b___1110:bit31 = abs_b_1110 & 0x7FFFFFFF
    abs_b___1101:bit31 = abs_b_1101 & 0x7FFFFFFF
    abs_b___1100:bit31 = abs_b_1100 & 0x7FFFFFFF
    abs_b___1011:bit31 = abs_b_1011 & 0x7FFFFFFF
    abs_b___1010:bit31 = abs_b_1010 & 0x7FFFFFFF
    abs_b___1001:bit31 = abs_b_1001 & 0x7FFFFFFF
    abs_b___1000:bit31 = abs_b_1000 & 0x7FFFFFFF

    c = 0
    flag = 0x80000000 >> abs_a_zero_len
    print('go', abs_a, abs_b)

    hit = False
    #for i in range((31 - abs_a_zero_len + 3)//4):
    abs_b2 = abs_b << 1
    x = shift_n
    while abs_a > abs_b2:
        if hit:
            c <<= 4
            x -= 4
        else:
            c <<= 1
            x -= 1

        #print(c)

        #print(abs_a, '<=>', abs_b___1111, abs_b___1110, abs_b___1101, abs_b___1100, abs_b___1011, abs_b___1010, abs_b___1001, abs_b___1000)
        abs_a_1111:bit32 = abs_a - abs_b___1111
        abs_a_1110:bit32 = abs_a - abs_b___1110
        abs_a_1101:bit32 = abs_a - abs_b___1101
        abs_a_1100:bit32 = abs_a - abs_b___1100
        abs_a_1011:bit32 = abs_a - abs_b___1011
        abs_a_1010:bit32 = abs_a - abs_b___1010
        abs_a_1001:bit32 = abs_a - abs_b___1001
        abs_a_1000:bit32 = abs_a - abs_b___1000

        #print(abs_a_1111, abs_a_1110, abs_a_1101, abs_a_1100, abs_a_1011, abs_a_1010, abs_a_1001, abs_a_1000)
        #print(abs_a_1111 & flag, abs_a_1110 & flag, abs_a_1101 & flag, abs_a_1100 & flag, abs_a_1011 & flag, abs_a_1010 & flag, abs_a_1001 & flag, abs_a_1000)

        hit = True
        if (abs_b_1_1111 == 0) & ((abs_a_1111 & flag) == 0):
            c0 = 0xF
            abs_a = abs_a_1111
        elif (abs_b_1_1110 == 0) & ((abs_a_1110 & flag) == 0):
            c0 = 0xE
            abs_a = abs_a_1110
        elif (abs_b_1_1101 == 0) & ((abs_a_1101 & flag) == 0):
            c0 = 0xD
            abs_a = abs_a_1101
        elif (abs_b_1_1100 == 0) & ((abs_a_1100 & flag) == 0):
            c0 = 0xC
            abs_a = abs_a_1100
        elif (abs_b_1_1011 == 0) & ((abs_a_1011 & flag) == 0):
            c0 = 0xB
            abs_a = abs_a_1011
        elif (abs_b_1_1010 == 0) & ((abs_a_1010 & flag) == 0):
            c0 = 0xA
            abs_a = abs_a_1010
        elif (abs_b_1_1001 == 0) & ((abs_a_1001 & flag) == 0):
            c0 = 0x9
            abs_a = abs_a_1001
        elif (abs_b_1_1000 == 0) & ((abs_a_1000 & flag) == 0):
            c0 = 0x8
            abs_a = abs_a_1000
        else:
            hit = False

        #print(abs_a, c0)

        if hit:
            c |= c0

            flag >>= 4
            abs_b___1111 >>= 4
            abs_b___1110 >>= 4
            abs_b___1101 >>= 4
            abs_b___1100 >>= 4
            abs_b___1011 >>= 4
            abs_b___1010 >>= 4
            abs_b___1001 >>= 4
            abs_b___1000 >>= 4
            abs_b0 >>= 4
        else:
            flag >>= 1
            abs_b___1111 >>= 1
            abs_b___1110 >>= 1
            abs_b___1101 >>= 1
            abs_b___1100 >>= 1
            abs_b___1011 >>= 1
            abs_b___1010 >>= 1
            abs_b___1001 >>= 1
            abs_b___1000 >>= 1
            abs_b0 >>= 1

        print('abs_b0', abs_b0, 'abs_a', abs_a, abs_b2)

    print('c', c, shift_n, abs_b0, abs_b2, abs_a, abs_b)
    if abs_a >= abs_b:
        c <<= 1
        c +=1
        abs_a -= abs_b

    print('c', c, shift_n, x)
    if sign_a:
        abs_a |= 0x80000000
    if sign_a ^ sign_b:
        c |= 0x80000000

    return c, abs_a

@testbench
def test():
    lst = [4, 5, 4001, 7]
    old_e = 2903
    for e in lst:
        (ra, rb) = divmod(old_e, e)
        print(old_e, '/', e , '=>', ra, '...', rb)
        (ra, rb) = divmod4(old_e, e)
        print(old_e, '/', e , '=>', ra, '...', rb)

        old_e = e

if __name__ == "__main__":
    test()
