
class AutomateException( BaseException ):     # Un lien d'héritage !!!
    def __init__(self, message):
        super().__init__(message)

class Automate( object ) :

    def __init__(self, id, reference_type, unite=None):
        self._id = id
        self._reference_type = reference_type
        self._idUnite = unite.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is None:
            raise AutomateException("id cannot be None")
        elif  not(isinstance( value, int)):
            raise AutomateException("id must be an int")
        elif value == "":
            raise AutomateException("id cannot be empty")
        else:
            self._id = value 

    @property
    def reference_type(self):
        return self._reference_type

    @id.setter
    def reference_type(self, value):
        if value is None:
            raise AutomateException("reference_type cannot be None")
        elif  not(isinstance( value, str)):
            raise AutomateException("reference_type must be a str")
        elif value == "":
            raise AutomateException("reference_type cannot be empty")
        else:
            self._reference_type = value.lower          

    @property
    def idUnite(self):
        return self._idUnite

    @id.setter
    def idUnite(self, value):
        if value is None:
            raise AutomateException("id cannot be None")
        elif  not(isinstance( value, int)):
            raise AutomateException("id must be an int")
        elif value == "":
            raise AutomateException("id cannot be empty")
        else:
            self._idUnite = value

    def __str__(self):
        return "{}, {}, {}".format(self.id, self.reference_type,  self.id_unite)       

            
               


