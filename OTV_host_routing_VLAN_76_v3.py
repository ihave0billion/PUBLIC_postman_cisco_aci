#format allows inserting into strings, but it's not working with more than one variable. see:
#https://docs.python.org/3/library/string.html#formatexamples

import paramiko
import time

host_ip = 219

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.101',port=22,username='admin',password='cisco')

ssh_conn = ssh.invoke_shell()
output = ssh_conn.recv(65535)
print output

ssh_conn.send('conf t\n')
time.sleep(.5)
output = ssh_conn.recv(65535)
print output

ssh_conn.send('ip route 50.254.75.{0}/32 Vlan2275 50.254.75.{1}\n '.format(host_ip, host_ip))
time.sleep(.5)
output = ssh_conn.recv(65535)
print output


ssh_conn.sen('ip prefix-list OTV_2275 seq {0} permit 50.254.75.{1}/32\n'.format(host_ip, host_ip))
time.sleep(.5)
output = ssh_conn.recv(65535)
print output

ssh_conn.send('show run | sec OTV_2275')
time.sleep(.5)
output = ssh_conn.recv(65535)

ssh_conn.send('end\n')
time.sleep(.5)
output = ssh_conn.recv(65535)
print output

ssh

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.102',port=22,username='admin',password='cisco')

ssh_conn = ssh.invoke_shell()
output = ssh_conn.recv(65535)
print output

ssh_conn.send('conf t\n')
time.sleep(.5)
output = ssh_conn.recv(65535)
print output

ssh_conn.send('no ip route 50.254.75.{0}/32 Vlan2275 50.254.75.{1}\n '.format(host_ip, host_ip))
time.sleep(.5)
output = ssh_conn.recv(65535)
print output


ssh_conn.sen('no ip prefix-list OTV_2275 seq {0} permit 50.254.75.{1}/32\n'.format(host_ip, host_ip))
time.sleep(.5)
output = ssh_conn.recv(65535)
print output

ssh_conn.send('show run | sec OTV_2275')
time.sleep(.5)
output = ssh_conn.recv(65535)

ssh_conn.send('end\n')
time.sleep(.5)
output = ssh_conn.recv(65535)
print output

ssh.close()