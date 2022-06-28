#------------------------------------
#-- Lancement du container 'collecteur'
#----Ce fichier traite la reception des fichiers envoyés par les unités de prod (json)
#---- Les traite et les renvoi
#------------------------------------
import os
# import socket programming library
import socket
# import thread module
# import thread module
from _thread import *
import threading

#import tqdm
import ssl

#HOST = '127.0.0.1'
#HOST = '0.0.0.0'
#HOST = socket.gethostbyname('collecteur')
HOST = socket.gethostbyname(socket.gethostname())
PORT = 11001
BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"
print_lock = threading.Lock()
filePath = "json_files/"


 # thread function
def threaded(c,addr):
    while True:
        # data received from client
        data = c.recv(BUFFER_SIZE)
        if not data:
            # lock released on exit
            print_lock.release()
            break         
    c.close()

def Main():
    # create the client socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("socket binded to port: ", PORT)
     # put the socket into listening mode
    s.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}.") 
    while True:
         # establish connection with client
        c, addr = s.accept()
        # lock acquired by client
        print_lock.acquire()
        jsonReceived = c.recv(BUFFER_SIZE).decode()
        if jsonReceived:
            #filePathName=filePath+fileName
            fileName, filesize = jsonReceived.split(SEPARATOR)
            print("recieve:--------"+fileName)
            # remove absolute path if there is
            fileName = os.path.basename(fileName)
            # convert to integer
            filesize = int(filesize)
            # and writing to the file stream
            filePathName = os.path.join("json_files/", fileName)

            print("write:--------"+filePathName)
            with open(filePathName, "wb") as f:
                while True:
                    # read 1024 bytes from the socket (receive)
                    bytes_read = c.recv(BUFFER_SIZE)
                    if not bytes_read:    
                        # nothing is received file transmitting is done
                        break
                    # write to the file the bytes we just received
                    f.write(bytes_read)
                    
        # Start a new thread 
        thread = threading.Thread(target=threaded, args=(c,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
       # start_new_thread(threaded, (c,))
    c.close()
    
if __name__ == '__main__':
    Main()
