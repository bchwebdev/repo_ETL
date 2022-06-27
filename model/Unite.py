class UniteException( BaseException ):     # Un lien d'héritage !!!
    def __init__(self, message):
        super().__init__(message)

class Unite( object) :

    def __init__(self,id, numero):
        self._id = id
        self._numero = numero

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is None:
            raise UniteException("id cannot be None")
        elif(not(isinstance( value, int))):
            raise UniteException("id must be an int")
        elif value == "":
            raise UniteException("id cannot be empty")
        else:
            self._id = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if value is None:
            raise UniteException("Numero cannot be None")
        elif  not(isinstance( value, float)):
            raise UniteException("Numero must be a float")
        elif value == "":
            raise UniteException("Numero cannot be empty")
        else:
            self._numero = value
    
    def __str__(self):
        return "{},{}" % (self.id, self.numero)

        