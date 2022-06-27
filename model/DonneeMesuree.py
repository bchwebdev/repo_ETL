import datetime
from model.Automate import Automate

class ValeurException( BaseException ):     # Un lien d'héritage !!!
    def __init__(self, message):
        super().__init__(message)

class DonneeMesuree():
 
    def __init__(self,id, valeur, uniteMesure, dateHeure, automate):
        self._id = id
        self._valeur = valeur
        self._unite_mesure = uniteMesure   
        self._date_heure = dateHeure
        self._automate = automate

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is None:
            raise ValeurException("id cannot be None")
        elif(not(isinstance( value, int))):
            raise ValeurException("id must be an int")
        elif value == "":
            raise ValeurException("id cannot be empty")
        else:
            self._id = value

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, value):        
        if value is None:
            raise ValeurException("valeur cannot be None")
        elif(not(isinstance( value, float))):
            raise ValeurException("valeur must be a float")
        elif value == "":
            raise ValeurException("valeur cannot be empty")
        else:
            self._valeur = value
 
    @property 
    def uniteMesure(self):
        return self._uniteMesure

    @uniteMesure.setter
    def uniteMesure(self, value):
        if value is None:
            raise ValeurException("uniteMesure cannot be None")
        elif(not(isinstance( value, str))):
            raise ValeurException("uniteMesure must be a string")
        elif value == "":
            raise ValeurException("uniteMesure cannot be empty")
        else:
            self._uniteMesure = value    

    @property        
    def dateHeure(self):
        return self._dateHeure

    @dateHeure.setter
    def dateHeure(self, value):
        if value is None:
            raise ValeurException("dateHeure cannot be None")
        elif(not(isinstance( value, datetime.date))):
            raise ValeurException("dateHeure must be a Date")
        elif value == "":
            raise ValeurException("dateHeure cannot be empty")
        else:
            self._dateHeure = value  

    @property        
    def automate(self):
        return self._automate

    @automate.setter        
    def automate(self, value):
        if value is None:
            raise ValeurException("automate cannot be None")
        elif(not(isinstance( value, Automate))):
            raise ValeurException("automate must be a type Automate")
        elif value == "":
            raise ValeurException("automate cannot be empty")
        else:
            self._automate = value      
    
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.valeur,  self.uniteMesure, self.dateHeure, self.automate)       
