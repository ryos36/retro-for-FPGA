EXIT = 0x0FFFFFFF
INPUT_INC = 4
DEC = 2
MEMORY_SIZE = 64 #16384

# -----------------------------------------------------------------------------
def abs(a):
    return -a if a < 0 else a

# -----------------------------------------------------------------------------
def retro_divmod( a, b ):
  abs_x = abs(a)
  abs_y = abs(b)

  q = abs_x // abs_y
  r = abs_x % abs_y

  if a < 0 and b < 0:
    r *= -1
  elif a > 0 and b < 0:
    q *= -1
  elif a < 0 and b > 0:
    r *= -1
    q *= -1

  return q, r

