class LoginVO():
    def __init__(self, usuario, password):
        self._usuario = usuario
        self._password = password
        
    @property
    def usuario(self):
        return self._usuario
        
    @property
    def password(self):
        return self._password
        