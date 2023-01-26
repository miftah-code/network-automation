import paramiko
import time
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="103.1.1.1",username="admin",password="idnmantab")

stdin, sdtout,stderr=ssh.exec_command("export")
print(sdtout.read().decode("ascii")).strip("\n")
ssh.close()

