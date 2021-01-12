class Contato:

    def __init__(self, nome = '', numero = '', email = ''):
        
        self.__nome = nome
        self.__numero = numero
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, name):
        self.__nome = name.title()


    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, number):
        self.__numero = number
        

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email_):
        self.__email = email_.capitalize()

    
