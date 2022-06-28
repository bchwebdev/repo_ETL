from typing import List, Dict
import json
import os
import ast
from flask import Flask, request, render_template
import shutil
import time 
import requests

#liste des fichiers reçus des unitées
def listFiles(dir):
   files =  os.listdir(dir)
   return files

#liste des fichiers restants a traiter: Comparaison de la liste des fichiers dans les deux repertoires
#Permet d'éviter les doublons
def filesListStillToBeProcessed(FilesRecevedList,filesProcessedList):
    liste = []
    if (filesProcessedList):
        difference_1 = set(filesProcessedList).difference(set(FilesRecevedList))
        difference_2 = set(FilesRecevedList).difference(set(filesProcessedList))
        liste = list(difference_1.union(difference_2))
    else:
        liste = FilesRecevedList
    return liste

#Exctraction date nom de fichier
def fotmatHeure(dh):
    date = ""
    heure = ""
    for i in range(len(dh)):
        if (i>=0 and i<=9):
            date+=str(dh[i])
        if (i>=10 and i<=18):
            heure+=str(dh[i])
    return date[len(date)-2] + date[len(date)-1] + "/" + date[len(date)-5] + date[len(date)-4] + "/" + date[0] + date[1] + date[2] + date[3]

#Traitement des données contenues dans les fichier json reçus:
#lecture des fichers, reception des données, appel API pour insertion dans la BDD Mysql (grace à Flask)
#Sauvegarde des fichiers dans le repertoire des fichiers traités
#Puis suppression des fichiers du repertoire des fichers reçus (en provenance des unitées)
def Savedatas():
    print("START")
    apiAddDatas = 'http://localhost:5000/add/addDatas'
    apiSelectIdAutomateByRef = 'http://localhost:5000/getAutomateById'
    dirFiles="json_files/"
    dirFilesProcessed="Save_Files/"
    jsonFilesRecevedList=listFiles(dirFiles)
    jsonFilesProcessedList=listFiles(dirFilesProcessed)
    filesListToRead = filesListStillToBeProcessed(jsonFilesRecevedList,jsonFilesProcessedList)
    print(filesListToRead)
    continu=True
    i=0
    while continu:   
        for jsonFileName in filesListToRead:
            i=0
            with open(dirFiles+jsonFileName) as jsonFileOpen:
                print(jsonFileOpen)
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
                        resForIdAutomate = 1
                        resForIdAutomate = requests.get(apiSelectIdAutomateByRef, params=payload)
                        datasToSave = {'valeur': d["mesure"], 'unite_mesure' : d["type_um"],'date_heure' : DateHeureCrea, 'id_automate' : int(resForIdAutomate) }
                        r = requests.post(apiAddDatas, data=datasToSave)
                        #print (type(datasToSave)," : ",payload," : ",datasToSave)
                shutil.copyfile(dirFiles+jsonFileName, dirFilesProcessed+jsonFileName)        
                
            print(jsonFileName, "saved in dir:", dirFilesProcessed)
        if(i==30):
            continu = False
        i=i+1
        time.sleep(10)
if __name__ == '__main__':
    Savedatas()