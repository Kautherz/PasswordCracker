# PasswordCracker

Cracking hashed passwords using a python script for sha256 algorithm

- [x] wordsList.txt : the list of words to generate the password guesses within the password cracker

- [x] CTF1.py : the password cracker

- [x] cracked.txt : list of some of the cracked passwords from the hashedPasswords

- [x] hashedPasswords.txt : 100 hashes of passwords


## Rules

Rules to generate the random password guesses:
      
      1. random English word chosen (more than 10 characters)
      
      2. first character sometimes captialized
      
      3. substitutions: {'s':'$', 'a': '4', 'l': '1', 'e': '3', 't': '7', 'i': '1', 'o': '0', 'b': '8', 'g': '9'}
      
      4. At the end of the word, a symbol and a digit get appended. 
        The following are the symbols used: ! @ # $ % ^ & * ( ) { } | : ; [ ] ? > <

## Server 

Run the python password cracker script on the UNO Cook Server: ssh kzeini@cook.cs.uno.edu 

On the server, use the screen command to run the script non-stop to crack as many passwords as possible: 

      screen 
      
      screen -ls
      
      screen -r "number of screen"

## Running the Program

Run the program on a screen:

      python3 CTF1.py 


