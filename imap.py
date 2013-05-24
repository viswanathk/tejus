import imaplib

username = '' 
password = '' # your pw
mailbox = 'INBOX' # inbox is default

mailserver = 'imap.gmail.com'
port = 993

server = imaplib.IMAP4_SSL(mailserver,port)

# server = imaplib.IMAP4(mailserver,port)

server.login(username,password)
server.select(mailbox)
# pull info for that mailbox
data = str(server.status(mailbox, '(MESSAGES UNSEEN)'))
# print it all out
print
#print 'GMAIL' #change this if ur not using gmail
#print username.replace('@gmail.com','') + '\'s Mailbox'
tokens = data.split()

# clean up output with str_replace()
#print tokens[2].replace('(',''),tokens[3] 
print "Sir you have ",
print tokens[5].replace(')\'])',''), tokens[4],
print " mails"
print
server.close()

server.logout()

