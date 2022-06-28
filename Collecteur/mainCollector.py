#------------------------------------
#-- Lancement du container 'collecteur'
#----Ce fichier traite la reception des fichiers envoyés par les unités de prod (json)
#---- Les traite et les renvoi
#------------------------------------
import requests, json, threading, socket, os, shutil, ssl, time

import os
# import socket programming library
import socket
# import thread module
# import thread module
from _thread import *
import threading
import ssl

#HOST = '127.0.0.1'
#HOST = '0.0.0.0'
#HOST = socket.gethostbyname('collecteur')
HOST = socket.gethostbyname(socket.gethostname())
PORT = 10001
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
def insertDatas(jsonFile):
    print("START insert")
    apiURL ='http://localhost:5000'
    apiAddDatas = apiURL+'/add/addDatas'
    apiSelectIdAutomateByRef = apiURL+'/getAutomateById'
    dirFiles="json_files/"
    dirFilesProcessed="Save_Files/"
    if jsonFile:
        print("Insert data from ", jsonFile)
        with open(dirFiles+jsonFile) as jsonFileOpen:
            print("jsonFileOpen: ", jsonFileOpen)

            datas = json.load(jsonFileOpen)
            datasDict = json.loads(datas)
            uniteId= datasDict["DataSet"][0]['unite']
            DateHeureCrea= datasDict["DataSet"][1]['DateHeure']
            datasDic= datasDict["DataSet"][2]['datas']
            #print(datas)
            for ds in datasDict["DataSet"]:
                #print(ds)
                for d in datasDic:                    
                    ref = d["ref"]
                    payload = {'ref': ref, 'uniteId': uniteId}  
                    #resForIdAutomate = 1
                    print('Api', payload)
                    resForIdAutomate = requests.get(apiSelectIdAutomateByRef, params=payload)
                    time.sleep(5)
                    datasToSave = {'valeur': d["mesure"], 'unite_mesure' : d["type_um"],'date_heure' : DateHeureCrea, 'id_automate' : int(resForIdAutomate) }
                    r = requests.post(apiAddDatas, data=datasToSave)
                    #print (type(datasToSave)," : ",payload," : ",datasToSave)
            shutil.copyfile(dirFiles+jsonFile, dirFilesProcessed+jsonFile)  
            os.remove(dirFiles+jsonFile)
        print(jsonFile, "saved in dir:", dirFilesProcessed)
    else:
        print("No files to save")
#------------------------------------
def main():   
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
            fileName = os.path.basename(fileName)
            # start receiving the file from the socket
            filePathName = os.path.join("json_files/", fileName)
            # and writing to the file stream
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
        #Insert datas
        #----------------------
        insertDatas(fileName)  
        #----------------------
        c.close()
    
        # Start a new thread 
        thread = threading.Thread(target=threaded, args=(c,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    
if __name__ == '__main__':
    main()