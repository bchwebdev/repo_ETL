#-----------Unitée 1
# automate 1 à 10 : Types : de 0X0000BA20 à de 0X0000BA2F

import socket
import sys
print(sys.version, sys.platform, sys.executable)
import json
import random
import os
from random import randint, randrange
from time import time, sleep
from datetime import datetime
from datetime import time
from datetime import date
import time

#HOST = '127.0.0.1'
#HOST = '0.0.0.0'
#HOST = socket.gethostbyname('collecteur')
HOST = socket.gethostbyname(socket.gethostname())
PORT = 10001

unityNum = 1
iCount=0
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 # send 4096 bytes each time step

def generateDatas(unityNum, creatTime) -> dict:
    #1: Température cuve - Entre 2,5 et 4 degrés par dixième de degré
    automate1 ={"ref" : "0X0000BA20" , "mesure" : round(random.uniform(2.5, 4),1) , "type_um" : "degre"}
    #2: Température extérieure - Entre 8 et 14degrés par dixième de degré
    automate2 ={"ref" : "0X0000BA21" , "mesure" :  randint(8, 14) , "type_um" : "degre"}
    #3: Poids du lait en cuve - Entre 3512 kg et 4607kg par incrément de 1 kilo
    automate3 ={"ref" : "0X0000BA22" , "mesure" :  randint(3512,4607) , "type_um" : "kilo"}
    #4:Poids du produit fini réalisé - différence entre les deux mesures successives de poids du lait dans la cuve
    automate4 ={"ref" : "0X0000BA23" , "mesure" :  randint(0,4607) , "type_um" : "kilo"}
    #5:Mesure pH - Entre 6,8 et 7,2 par incrément de 1/10
    automate5 ={"ref" : "0X0000BA24" , "mesure" :  round(random.uniform(6.8, 7.2),1) , "type_um" : "kilo"}
    #6:Mesure K+ - Entre 35mg et 47 mg /litres par pas de 1 mg
    automate6 ={"ref" : "0X0000BA25" , "mesure" :  round(random.uniform(2.5, 4),1), "type_um" : "mg"}
    #7:concentration de NaCl - Entre 1g et 1,7 g part litre par pas de 0,1g
    automate7 ={"ref" : "0X0000BA26" , "mesure" : round(random.uniform(1, 1.7),1) , "type_um" : "g"}
    #8:Niveau bactériensalmonelle - Entre 17 et 37 ppm , par incrément de 1 ppm
    automate8 ={"ref" : "0X0000BA27" , "mesure" : randint(17,37) , "type_um" : "ppm"}
    #9:Niveau bactérien E-coli - Entre 35 et 49 ppm , par incrément de 1 ppm
    automate9 ={"ref" : "0X0000BA28" , "mesure" : randint(35,49) , "type_um" : "ppm"}
    #10:Niveau bactérien Listéria - ntre 28 et 54 ppm , par incrément de 1 ppm
    automate10 ={"ref" : "0X0000BA29" , "mesure" :  randint(28,54), "type_um" : "ppm"}
    mesures =[automate1, automate2, automate3, automate4, automate5, automate6, automate7,automate8, automate9, automate10]
    #fileJson = {"unite" :unityNum , "dateCreation" : creatTime , "datas" : mesures}
    fileJson ={"DataSet":[{"unite": unityNum},{"DateHeure":creatTime},{"datas" : mesures}]}
    print(type(fileJson))

    jsonFileMesures = json.dumps(fileJson, sort_keys=True)
    return jsonFileMesures
        
        
        
def generateJson(datasSet, nameFile):
    jsonFile=""
    fileToJson = open(nameFile, "w")
    jsonFile = json.dump(datasSet, fileToJson)
    fileToJson.close()
    return jsonFile
   
def main():
    iCount=0
    #un par minutes;
    while iCount<10:
        # thing to run
        named_tuple = time.localtime() # get struct_time
        creatTime = time.strftime("%Y-%m-%d_%H-%M-%S", named_tuple)
        generateData = generateDatas(unityNum, creatTime)
        filePath = "json_files/"
        fileName = "Unity"+ str(unityNum) + "_" + creatTime + ".json"
        filePathName = filePath+fileName
        jsonFile= generateJson(generateData, filePathName)
        jsonFileSize = os.path.getsize(filePathName)

        print("Fichier ["+ str(iCount) +"] : ")
        print(".........File name : " + filePathName)   
        print(".........File size : " + str(jsonFileSize))
        print(".........Generated datas : " + generateData)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        # send the filename and filesize
        s.send(f"{fileName}{SEPARATOR}{jsonFileSize}".encode())
        # start sending the file
        #progress = tqdm.tqdm(range(jsonFileSize), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filePathName, "rb") as f:
            while True:               
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                #progress.update(len(bytes_read))
        print ('json was sent!')
        # close the socket
        s.close()
        iCount = iCount+1
        time.sleep(5)

if __name__ == "__main__":
    main()