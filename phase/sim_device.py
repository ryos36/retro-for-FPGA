from utils_for_retro import EXIT, INPUT_INC, DEC, MEMORY_SIZE
from stack import retro_stack
from polyphony.typing import bit32

#----------------------------------------------------------------
def rx_char( io_ports ):
    print('rx_chflush')
    return 0

def tx_char( io_ports, char_c ):
#    print(chr(char_c), end='', flush=True)
    print(char_c)

def flush( io_ports ):
    #print('flush')
    pass

#----------------------------------------------------------------
def handle_devices( ip, stack:retro_stack, address:retro_stack, ports:list, memory:list, io_ports:list ):
  ports[0] = 1
  if ports[1] == 1:
    ports[1] = rx_char( io_ports )
    if ports[1] == 13:
      ports[1] = 10
  if ports[2] == 1:
    if stack.top > 0 and stack.top < 128:
      if stack.top == 8:
        tx_char(io_ports, stack.pop())
        tx_char(io_ports, 32)
        tx_char(io_ports, 8)
      else:
        tx_char(io_ports, stack.pop())
    else:
      #escape seqence TODO
      #sys.stdout.write("\033[2J\033[1;1H")
      stack.pop()
    flush(io_ports)
    ports[2] = 0
  if ports[4] ==  1:    # file save
#    TODO
#    f = open('retroImage', 'wb')
#    i = 0
#    while i < memory[3]:
#      f.write(struct.pack('i', memory[i]))
#      i += 1
#    f.close()
    ports[4] = 0
  if ports[4] ==  2:    # file include
#    TODO
#    name = ''
#    i = stack.pop()
#    while memory[i] != 0:
#      name = name + chr(memory[i])
#      i += 1
#    f = open(name, 'r')
#    inputs.append( f )
    ports[4] = 0
  if ports[4] == -1:    # file open
#    TODO
#    slot = 0
#    i = 1
#    name = ''
#    while i < 8:
#      if files[i] == 0:
#        slot = i
#      i += 1
#    mode = stack.pop()
#    i = stack.pop()
#    while memory[i] != 0:
#      name = name + chr(memory[i])
#      i += 1
#    if slot > 0:
#      if mode == 0:
#        if os.path.exists(name):
#          files[slot] = open(name, 'r')
#        else:
#          slot = 0
#      elif mode == 1:
#        files[slot] = open(name, 'w')
#      elif mode == 2:
#        files[slot] = open(name, 'a')
#      elif mode == 3:
#        if os.path.exists(name):
#          files[slot] = open(name, 'r+')
#        else:
#          slot = 0
#    ports[4] = slot;
    ports[4] = 0;
  elif ports[4] == -2:  # file read
#    slot = stack.pop()
#    ports[4] = ord(files[slot].read(1))
    ports[4] = 0;
  elif ports[4] == -3:  # file write
#    slot = stack.pop()
#    files[slot].write(chr(stack.pop()))
    ports[4] = 1
  elif ports[4] == -4:  # file close
#    slot = stack.pop()
#    files[slot].close()
#    files[slot] = 0
    ports[4] = 0
  elif ports[4] == -5:  # file position
#    slot = stack.pop()
#    ports[4] = files[slot].tell()
    ports[4] = 0
  elif ports[4] == -6:  # file seek
#    slot = stack.pop();
#    pos  = stack.pop();
#    ports[4] = files[slot].seek(pos, 0);
    ports[4] = 0
  elif ports[4] == -7:  # file size
#    slot = stack.pop()
#    at = files[slot].tell()
#    files[slot].seek(0, 2) # SEEK_END
#    ports[4] = files[slot].tell()
#    files[slot].seek(at, 0) # SEEK_SET
    ports[4] = 0
  if ports[4] == -8:    # file delete
#    name = ''
#    i = stack.pop()
#    while memory[i] != 0:
#      name = name + chr(memory[i])
#      i = i + 1
#    i = 0
#    if os.path.exists(name):
#      os.remove(name)
#      i = 1
#    ports[4] = i
    ports[4] = 0
  if ports[5] == -1:  # memory size - zero based index
    ports[5] = 100000 - 1
  elif ports[5] == -2:  # canvas exists?
    ports[5] = 0
  elif ports[5] == -3:  # canvas width
    ports[5] = 0
  elif ports[5] == -4:  # canvas height
    ports[5] = 0
  elif ports[5] == -5:  # stack depth
    ports[5] = stack.length()
  elif ports[5] == -6:  # address stack depth
    ports[5] = address.length()
  elif ports[5] == -7:  # mouse exists?
    ports[5] = 0
  elif ports[5] == -8:  # time
#    ports[5] = int(time.time())
    ports[5] = 0
  elif ports[5] == -9:  # exit vm
    ip = EXIT
    ports[5] = 0
  elif ports[5] == -10: # environment variable
# TODO
#    req = stack.pop()
#    dest = stack.pop()
#    key = ''
#    while memory[req] != 0:
#      key = key + chr(memory[req])
#      req += 1
#    req = os.getenv(key, default="/")
#    memory[dest] = 0
#    i = 0
#    while i < len(req):
#      memory[dest] = ord(req[i])
#      i += 1
#      dest += 1
#      memory[dest] = 0
    ports[5] = 0
  elif ports[5] == -11: # console width
    ports[5] = 0
  elif ports[5] == -12: # console height
    ports[5] = 0
  elif ports[5] == -13: # bits per cell
    ports[5] = 32
  elif ports[5] == -14: # endian
    ports[5] = 0
  elif ports[5] == -15: # console extensions
    ports[5] = -1

# TODO
#  if ports[8] == 1:
#    ports[8] = 0
#    a = stack[-2]
#    stack[-2] = stack.top
#    stack.top = a
#    sys.stdout.write("\33[" + str(stack.pop()) + ";" + str(stack.pop()) + "H")
#  elif ports[8] == 2:
#    ports[8] = 0
#    sys.stdout.write("\33[3" + str(stack.pop()) + "m")
#  elif ports[8] == 3:
#    ports[8] = 0
#    sys.stdout.write("\33[4" + str(stack.pop()) + "m")
#  else:
#    ports[8] = 0
  if ports[8] == 1:
    ports[8] = 0

  return ip
