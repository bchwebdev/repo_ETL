import crypt


class UtilisateurException( BaseException ):     # Un lien d'héritage !!!
    def __init__(self, message):
        super().__init__(message)

class Utilisateur( object ):

    def __init__(self,id, nom, prenom, login, password, profil):
        self._id = id
        self._nom = nom
        self._prenom = prenom
        self._login = login
        self._salt = crypt.mksalt() # sel utilisé pour le hash du mot de passe
        self._password= password
        self._profil= profil


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if value is None:
            raise UtilisateurException("id cannot be None")
        elif(not(isinstance( value, int))):
            raise UtilisateurException("id must be an int")
        elif value == "":
            raise UtilisateurException("id cannot be empty")
        else:
            self._id = value 

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, value):        
        if value is None:
            raise UtilisateurException("nom cannot be None")
        elif(not(isinstance( value, str))):
            raise UtilisateurException("nom must be a string")
        elif value == "":
            raise UtilisateurException("nom cannot be empty")
        else:
            self._nom = value  

    @property
    def prenom(self):
        return self._prenom
    @nom.setter
    def prenom(self, value):        
        if value is None:
            raise UtilisateurException("prenom cannot be None")
        elif(not(isinstance( value, str))):
            raise UtilisateurException("prenom must be a string")
        elif value == "":
            raise UtilisateurException("prenom cannot be empty")
        else:
            self._prenom = value

    @property
    def login(self):
        return self._login
    @nom.setter
    def login(self, value):        
        if value is None:
            raise UtilisateurException("login cannot be None")
        elif(not(isinstance( value, str))):
            raise UtilisateurException("login must be a string")
        elif value == "":
            raise UtilisateurException("login cannot be empty")
        else:
            self._login = value 

    @property
    def password(self):
        return self._password
    @nom.setter
    def password(self, value):        
        if value is None:
            raise UtilisateurException("password cannot be None")
        elif(not(isinstance( value, str))):
            raise UtilisateurException("password must be a string")
        elif value == "":
            raise UtilisateurException("password cannot be empty")
        else:
            self._password = value 

    def _crypt_pwd(self, password):
        return crypt.crypt(password, self._salt)

    def check_pwd(self, password):
        return self._password == self._crypt_pwd(password)        

    @property
    def profil(self):
        return self._profil
    @nom.setter
    def profil(self, value):        
        if value is None:
            raise UtilisateurException("profil cannot be None")
        elif(not(isinstance( value, str))):
            raise UtilisateurException("profil must be a string")
        elif value == "":
            raise UtilisateurException("profil cannot be empty")
        else:
            self._profil = value

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.nom,  self.prenom, self.login, self.profil)       
