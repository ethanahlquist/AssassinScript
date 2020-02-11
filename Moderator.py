#!/usr/bin/python3
import smtplib, ssl
import getpass
import string
import sys
import os

NAME = 0
EMAIL = 1

PreMsg = 'THIS IS A TEST RUN\n\nYOUR TARGET IS: '

def sendemail(sender_email, receiver_list, cc_list,
              subject, message, password):

    header  = 'From: %s\n' % sender_email
    header += 'To: %s\n' % ','.join(receiver_list)
    header += 'Cc: %s\n' % ','.join(cc_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_list, message)


def checkInput():
    # Check if input file exists
    if(len(sys.argv) == 1):
        raise FileNotFoundError
    try:
        f = open(sys.argv[1])
        f.close()
    except FileNotFoundError:
        raise FileNotFoundError


def parseAndShufFile():

    NameEmail = [] 
    # Shuffle the input file
    cmd = "shuf " + sys.argv[1] 
    filePtr = os.popen(cmd, 'r',1)

    # Organize formate file, into a two dimensional array
    for line in filePtr:
        line = line.strip('\n')
        my_line = line.split(" : ") # Separate (Name : email)
        NameEmail.append(my_line)

    NameEmail.reverse()
    return NameEmail


def AssassinMail(assassin, target, password):
    sendemail(
        sender_email    = 'ethanahlquist@gmail.com', 
        receiver_list   = [assassin[EMAIL]],
        cc_list         = [''], 
        subject         = 'Assassin', 
        message         = assassin[NAME] + " -> " + PreMsg + target[NAME], 
        password        = password)    

def main():
    NameEmail = [] 
    checkInput()
    NameEmail = parseAndShufFile()

    # Ask for my gmail password once
    password = getpass.getpass("Type your password and press enter: ")

    # This sends emails to people playing in the game, with their targets
    num_items = len(NameEmail)
    for i in range(0, num_items):
        nindex = (i + 1) % num_items # index of the next preson in the list
        AssassinMail(
            assassin = NameEmail[i],
            target = NameEmail[nindex],
            password = password)
        
    print(NameEmail)
     
if __name__== "__main__":
    main()
