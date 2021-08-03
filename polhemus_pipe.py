import time
import struct

rf = open(r'//./pipe/PDIPnOPipe', 'rb', 0)

template = 'Hello World {}'

while True:
   # read text length and text
   n = struct.unpack('I', rf.read(4))[0]
   read = rf.read(n)
   print('Read:', read)

   time.sleep(2)