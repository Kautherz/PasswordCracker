import hashlib
import sys
import time
import itertools 
import string


hashFile = open("hashedPasswords.txt", "r")
wordListFile = open("wordsList.txt", "r")
crackedFile = open("cracked.txt", "w")


d = ["0", "1", "2", "3", "4", "0", "6", "7", "8", "9"]
s = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "|", ":", ";", "[", "]", "?", ">", "<"]

wordList = []  #phyllocyanin
for word in wordListFile:
     wordList.append(word.strip()) #this takes all the words in the wordListFile and places them into the wordList arrays 
wordListFile.close()

hashList = [] #list for all the hashes 
for hash in hashFile: 
    hashList.append(hash.strip()) 
hashFile.close()
hashset = set(hashList)

master_list = []
master_list2 = []
guessPasswordList = []
amountCracked = 0 
for word in wordList:
    master_list.clear()
    master_list2.clear()
    guessPasswordList.clear()
    for index, char in enumerate(word): 
        if char == "s":
            if index == 0:
                master_list.append([char, char.upper(), "$"])
                master_list2.append([char, char.upper(), "$"])
            else:
                master_list.append([char, "$"])
                master_list2.append([char, "$"])          
        elif char == "a":
            if index == 0:
                master_list.append([char, char.upper(), "4"])
                master_list2.append([char, char.upper(), "4"])
            else:
                master_list.append([char, "4"]) 
                master_list2.append([char, "4"])     
        elif char == "l": 
            if index == 0:
                master_list.append([char, char.upper(), "1"])
                master_list2.append([char, char.upper(), "1"])
            else:
                master_list.append([char, "1"])
                master_list2.append([char, "1"])    
        elif char == "e":
            if index == 0:
                master_list.append([char, char.upper(), "3"])
                master_list2.append([char, char.upper(), "3"])
            else:
                master_list.append([char, "3"])
                master_list2.append([char, "3"])
        elif char == "t":
            if index == 0:
                master_list.append([char, char.upper(), "7"])
                master_list2.append([char, char.upper(), "7"])
            else:
                master_list.append([char, "7"])
                master_list2.append([char, "7"])  
        elif char == "i":
            if index == 0:
                master_list.append([char, char.upper(), "1"])
                master_list2.append([char, char.upper(), "1"])
            else:
                master_list.append([char, "1"])
                master_list2.append([char, "1"]) 
        elif char == "o":
            if index == 0:
                master_list.append([char, char.upper(), "0"])
                master_list2.append([char, char.upper(), "0"])
            else:
                master_list.append([char, "0"])
                master_list2.append([char, "0"]) 
        elif char == "b":
            if index == 0:
                master_list.append([char, char.upper(), "8"])
                master_list2.append([char, char.upper(), "8"])
            else:
                master_list.append([char,"8"])
                master_list2.append([char,"8"])   
        elif char == "g":
            if index == 0:
                master_list.append([char, char.upper(), "9"])
                master_list2.append([char, char.upper(), "9"])
            else:
                master_list.append([char, "9"]) 
                master_list2.append([char, "9"])
        else:
            if index == 0:
                master_list.append([char, char.upper()])
                master_list2.append([char, char.upper()])
            else:
                master_list.append([char])
                master_list2.append([char])        
    master_list.append(d)
    master_list.append(s)
    master_list2.append(s)
    master_list2.append(d)

    combos = itertools.product(*master_list)
    for combo in combos:
        guessPassword = ''.join(combo) 
        guessPasswordList.append(guessPassword)

    combos2 = itertools.product(*master_list2)
    for c in combos2:
        guessPassword = ''.join(c) 
        guessPasswordList.append(guessPassword)

    for guess in guessPasswordList:  

        flag = "4621_ctf" + "{" + guess + "}"

        salt = "2546339" #student ID

        thetestedpwd = flag + salt

        sha256hash = hashlib.sha256(thetestedpwd.encode()).hexdigest().strip() #turns list into bytes acceptable by python


        if sha256hash in hashset:

            amountCracked += 1

            crackedFile.write(sha256hash +  ', ' + guess + "\n");
    
            print ("cracked password amount: ", amountCracked)

crackedFile.close()








