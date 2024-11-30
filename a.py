# Usage: python a.py id_of_SigStick

import sys, re
import os
import binascii

id = sys.argv[1]
num = int(sys.argv[2])
for i in range(num):
    os.system('wget https://imgcdn.sigstick.com/%s/%d-1.png'%(id,i))
    os.system('apng2gif %d-1.png'%i)
    f = open('./%d-1.gif'%i, 'r+b')
    pattern = "\x4E\x45\x54\x53\x43\x41\x50\x45\x32\x2E\x30"
    regex = re.compile(pattern)
    # 4e45 5453 4341 5045 322e 3003 0103
    # 4e45 5453 4341 5045 322e 3003 0100
    for match_obj in regex.finditer(f.read()):
        offset = match_obj.start()
        f.seek(offset + 13)
        f.write('\x00')
    print 'Done.'
