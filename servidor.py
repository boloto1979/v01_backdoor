import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('1pmaquina', 6088))
s.listen(1)
conexao,endereco = s.accept()
comando_enviar = input('Digite o comando que sera enviado > ')
conexao.send(comando_enviar.encode())
