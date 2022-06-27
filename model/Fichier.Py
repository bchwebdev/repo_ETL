import datetime


class FichierException( BaseException ):     # Un lien d'héritage !!!
    def __init__(self, message):
        super().__init__(message)

class Fichier( object ):

    def __init__(self,id, nom, poid, dateHeureCreation, dateHeurEnvoi):
        self._id = id
        self._nom = nom
        self._poid = poid
        self._dateHeureCreation = dateHeureCreation
        self._dateHeurEnvoi = dateHeurEnvoi

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is None:
            raise FichierException("id cannot be None")
        elif(not(isinstance( value, int))):
            raise FichierException("id must be an int")
        elif value == "":
            raise FichierException("id cannot be empty")
        else:
            self._id = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):        
        if value is None:
            raise FichierException("nom cannot be None")
        elif(not(isinstance( value, str))):
            raise FichierException("nom must be a string")
        elif value == "":
            raise FichierException("nom cannot be empty")
        else:
            self._nom = value  

    @property
    def poid(self):
        return self._poid

    @poid.setter
    def poid(self, value):                
        if value is None:
            raise FichierException("poid cannot be None")
        elif(not(isinstance( value, float))):
            raise FichierException("poid must be a float")
        elif value == "":
            raise FichierException("poid cannot be empty")
        else:
            self._poid = value 

    @property
    def dateHeureCreation(self):
        return self._dateHeureCreation

    @dateHeureCreation.setter
    def dateHeureCreation(self, value):        
        if value is None:
            raise FichierException("dateHeureCreation cannot be None")
        elif(not(isinstance( value, datetime.date))):
            raise FichierException("dateHeureCreation must be a date")
        elif value == "":
            raise FichierException("dateHeureCreation cannot be empty")
        else:
            self._dateHeureCreation = value   


    @property
    def dateHeurEnvoi(self):
        return self._dateHeurEnvoi

    @dateHeureCreation.setter
    def dateHeurEnvoi(self, value):        
        if value is None:
            raise FichierException("dateHeurEnvoi cannot be None")
        elif(not(isinstance( value, datetime.date))):
            raise FichierException("dateHeurEnvoi must be a date")
        elif value == "":
            raise FichierException("dateHeurEnvoi cannot be empty")
        else:
            self._dateHeurEnvoi = value   

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.nom,  self.poid, self.date_heure_creation, self.date_heure_envoi)       





