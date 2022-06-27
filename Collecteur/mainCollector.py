#------------------------------------
#-- Lancement du container 'collecteur'
#----Ce fichier traite la reception des fichiers envoyés par les unités de prod (json)
#---- Les traite et les renvoi
#------------------------------------
from _thread import *
import time
import requests, json, threading, socket, os, shutil, ssl
#HOST = '127.0.0.1'
#HOST = '0.0.0.0'
#HOST = socket.gethostbyname()
HOST = socket.gethostbyname(socket.gethostname())
PORT = 10001
PORT_MYSQL = 30000
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
    apiAddDatas = 'http://localhost:5000/add/addDatas'
    apiSelectIdAutomateByRef = 'http://localhost:5000/getAutomateById'
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
            # start receiving the file from the socket and writing to the file stream
           # progress = tqdm.tqdm(range(int(filesize)), f"Receiving {fileName}", unit="B", unit_scale=True, unit_divisor=1024)
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
                    # update the progress bar
                    # progress.update(len(bytes_read)) 

        #Insertion des données
        #----------------------
        #insertDatas(fileName)  
        #----------------------       
        thread = threading.Thread(target=threaded, args=(c,addr))
        thread.start()# Start a new thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
       # start_new_thread(threaded, (c,))

if __name__ == '__main__':
    Main()