# Author: Bhavishya Sharma
# Created: 3/5/09
# Description: Simple script that uses the python imap library
# to retrieve number of messages and unread messages from your 
# imap email account. 

# Script is free. Credit to twitter.com/#!/futurefurore is appreciated =)

import imaplib

# Username should be your username with '@gmail.com' added
# I think the @gmail.com is required.
# If you're trying it with something other than gmail
# you should make the username the full email address
# example@domain.com
username = '' 
password = '' # your pw
mailbox = 'INBOX' # inbox is default

# only tested with gmail and my university email
# it should work with any imap server
# change mail server and port to match your server's info
mailserver = 'imap.gmail.com'
port = 993

# connect to gmail's server (uses SSL, port 993)
server = imaplib.IMAP4_SSL(mailserver,port)

# gmail uses ssl...if your imap mail server doesn't comment the above
# line and uncomment this one.
# server = imaplib.IMAP4(mailserver,port)

# login with the variables provided up top
server.login(username,password)

# select your mailbox
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
# close the mailbox
server.close()

# logout of the server
server.logout()

