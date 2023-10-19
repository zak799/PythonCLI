import pyfiglet as pyf                 # PIP INSTALL PYFIGLET
from termcolor import colored          # PIP INSTALL TERMCOLOR
from time import sleep                 # STDLIB
from alive_progress import alive_bar   # PIP INSTALL ALIVE-PROGRESS
import time                            # STDLIB
from getpass4 import getpass           # PIP INSTALL GETPASS4
import socket                          # STDLIB


banner = pyf.figlet_format("# Matri _ X #", justify="right") # YOU CAN CHANGE THE TEXT 
text = colored(f'{banner}', 'green') # CHANGE THE TEXT COLOR [STEREOTYPICAL HACKER COLOR -_-]
print(text) # PRINT THE BANNER


def netscan():  #CREATE A NETSCAN FUNCTION
    ip = socket.gethostbyname(socket.gethostname()) # CREATE THE VARIABLE FOR THE NETSCANNER
    for port in range(65535):  # THERE ARE 65535 PORTS ON NETWORKS, ALL OF THEM GET SCANNED 
         try:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

            #  AF_INET = (INTERNET) ADDRESS FAMILY FOR IPV4  
            #  SOCK_STREAM IS FOR THE TCP(PROTOCOL FOR SENDING MESSAGES WITHIN NETWORKS)

            client.bind((ip,port)) # ASSIGNS AN IP AND A PORT TO A SOCKET INSTANCE
         except:
               print(f"[OPEN] Port open : {port}") # PRINT LIST OF ALL OPEN PORTS
               client.close() # CLOSE THE SERVER INSTANCE

help_cmd = """
netscan /all  -  Scan all networks [RECCOMENDED FOR SCANNING NETWORKS] 
"""      # CREATE A HELP LIST [MULTI or SINGLE LINE]


def slow(text): # CREATE A TYPE WRITING FUNCTION CLASS
    for letter in text: # 'LETTER' CORRESPONDS TO THE WORDS
        print(letter, end='', flush=True) # PRINT THE WORDS FOR AFTER EVERY PRINTED LETTER END='' PRINT NOTHING 
        sleep(0.07) # DELAY BETWEEN EVERY LETTER ENTERED
slow("""
Welcome To The Matri_X. A Hacking Tool 

[For Educational Purposes] 
- Authors *DO NOT* Condone In Any Way, Shape or form, Using Said Tools On Others Maliciously Without Permission 


Enjoy, ???
""")                    # USE DEF FUNCTION TO SEE IN ACTION (:

for x in 1000, 0:                                    # https://pypi.org/project/alive-progress/
   with alive_bar(x) as bar:                         # https://pypi.org/project/alive-progress/
       for i in range(1000):                         # https://pypi.org/project/alive-progress/
           time.sleep(.005)                          # https://pypi.org/project/alive-progress/
           bar.title('LOADING [ TOOLS | CMDs]')      # https://pypi.org/project/alive-progress/
           bar()
print("LOADED [TOOLS | CMDs] - 100%") # FOR LOOKS

def main():                                       # THE MAIN CODE
    login = getpass("Login.Matri_X: ")            # GETPASS IS A MODULE FOR PASSWORDS
    if login == "12345":                          # USE PYSQLITE3 FOR A MORE SECURE PASSCODE THAN "12345" IN SOURCE CODE                        
        while True:                               # HAVE THE CLI RUN INDEFINETELY
            cmd = input("Matri_X.console>>> ")    # CREATE THE INPUT FOR THE MAIN CODE
            if cmd == "-help":                    # HELP LIST
                print(help_cmd)                   # PRINT THE HELP LIST
            elif cmd == "netscan /all":           # REFERS TO THE STR FOR NETSCAN
                print(netscan())                  # START THE NETSCAN 
            elif cmd == "":                       # CREATE A FUNCTION
                print("[ERROR 423] LOCKED: UNCOMPLETE") # BLOCK ACCESS
    else:                            
        return "[ERROR 401] UNAUTHORISED ACCESS"          # LEAVE AS IT IS!
        main()                                            # RE-UP CONSOLE
main()                                                    # START CODE!

# ENJOY (:

