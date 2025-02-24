"""
    We use getters & setters to add validation logic around getting and setting
    a value.
    To avoid direct access of a class field i.e. private variables cannot
    be accessed directly or modified by external user.
"""



class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        #self.email = firstName + '.' + lastName + '@gmail.com'
        
    """ the @property allows to access a method as an attribute. Its a decorator
        which appends several functionalities to existing code and then returns it
    """
    @property
    def email(self):
       return "{}.{}@email.com".format(self.firstName, self.lastName)
    
    @property
    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)
    
    """ .setter function  """
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last

    """
        deleter is a destructor that destroys an object when called
    """
    @fullName.deleter
    def fullName(self):
        print("Full Name Delete is complete")
        self.firstName = None
        self.lastName = None

person1 = Person("antonie","riziki")

person1.firstName = "James"
person1.lastName = "Mwangi"
person1.fullName = "Geoffrey Shikanda"

print(person1.firstName)
print(person1.fullName)
print(person1.email)

del person1.fullName
print("Full Name : ", person1.fullName)
