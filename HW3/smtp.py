from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)

print("Started, creating socket!")
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

print("Connected, listening!")
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO smtp.gmail.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM starphys@gmail.com\r\n'
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO starphys@gmail.com\r\n'
clientSocket.send(rcptToCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
mailFromCommand = 'QUIT\r\n'
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '221':
    print('221 reply not received from server.')