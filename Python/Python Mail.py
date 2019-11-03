import smtplib
server = smtplib.SMTP('smtp.1usemail.com', 587)

server.login("frosliab@1usemail.com", "password")