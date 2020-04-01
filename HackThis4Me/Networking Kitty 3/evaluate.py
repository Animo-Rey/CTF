from pwn import *

host = "hackthisfor.me"
port = 4002

s = remote(host, port)

ex = s.recvuntil('\n', drop="True").decode("utf-8")
# s.sendline(str(ex))
s.sendline(str(eval(str(ex))))
print(s.recv().decode('utf-8'))
s.close()
