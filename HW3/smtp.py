from socket import *
import ssl
import base64
from time import sleep
from getpass import getpass

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

user = input("Enter gmail account: ")
pw = getpass()
sleep(1)

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

command = "STARTTLS\r\n"
clientSocket.send(command.encode())
recvdiscard = clientSocket.recv(1024)
print(recvdiscard)

clientSocket = ssl.wrap_socket(clientSocket)

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

#Send AUTH first
authMesg = 'AUTH LOGIN\r\n'
crlfMesg = '\r\n'

clientSocket.send(authMesg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

user64 = base64.b64encode(user.encode())
pass64 = base64.b64encode(pw.encode())
clientSocket.send(user64)
clientSocket.send(crlfMesg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

clientSocket.send(pass64)
clientSocket.send(crlfMesg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <' + user + '>\r\n'
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <' + user + '>\r\n'
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