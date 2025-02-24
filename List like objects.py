class AsapMob:
    def __init__(self):
        
        """ '.' refers to the members initialized
            '_' refers to private property of the object and cant be accessed from
            the outside of the class
        """
        
        self._members = [
            "ASAP Ant",
            "Asap Bari",
            "Asap Ferg",
            "Asap Illz",
            "Asap Lotto",
            "Asap Lou Bang",
            "Asap Nasty",
            "Asap P on the Boards",
            "Asap Relli",
            "Asap Rocky",
            "Asap Snacks",
            "Asap Twelvy",
            "Asap Ty Beats",
            "Asap TyY",
            "Asap Trash Panda"
            ]
        """
            Define a function that access self._members initialized
        """

    def __len__(self):
        return len(self._members)

    """
        define another function __getitem__ to return the index of self._members
    """
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._members.pop(key)
        raise TypeError ("Value must be integer ", key)

    """
        define another function __contains__ that allows for looping through the members
        without tampering with the current list
    """

    def __contains__(self, member):
        return member in self._members

    """
        defining a function that will return iterator
        that allows looping through the object
    """

    def __iter__(self):
        while self._members:
            yield self._members.pop()
    
asap = AsapMob()
print("There are ", len(asap), " members in the Asap Mob crew " )
print(asap[5], " goes solo")
print("There are ", len(asap), "A$AP members left in the crew")

""" check whether the given name is in ASAP Mob """

if "antonie" in asap:
    print("antonie is part of Asap Mob")
else:
    print("antonie is not part of Asap Mob")

print(len(asap), "Asaps remaining")

for member in asap:
    print(member)

print("There are", len(asap), "A$AP members left in the crew")
