---
Title: Assassin
Author: Ethan Ahlquist
Date: Feb 11, 2020
---  

# Assassin Script

At school, we wanted to play a game called assassin.

In this game, every person is given the name of a person they have to "hunt". The issue is that everyone wants to play; however, we needed someone to be a moderator, to hand out targets (without meeting in-person).

The solution I came up with was to create a script to email all the members of the game their randomly selected targets.

# Usage

   ```Usage: ./Moderator.py [filename]```

## Create a file

This file will hold name/email pairs of all players, like so:

   ```
   name1 : email1\\
   name2 : email2\\
   name3 : email3\\
   name4 : email4\\
   name5 : email5\\
   name6 : email6\\
   name7 : email7\\
   name8 : email8\\
   ```

## Running From Command Line

   - Python3 ./Moderator.py [filename]

   - ./Moderator.py [filename]

[filename] is the file containing (name : email) pairs

