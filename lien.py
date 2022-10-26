import noeud


class lien():
    """Class with the graphs links"""
    __idlglob = 0

    def __init__(self, noeud1, noeud2, distance):
        self.__noeud1 = noeud1
        self.__noeud2 = noeud2
        self.__distance = distance
        self.__id = lien.__idlglob
        lien.__idlglob += 1

    def getNoeud1(self):
        return self.__noeud1

    def setNoeud1(self, value):
        self.__noeud1 = value

    def getNoeud2(self):
        return self.__noeud2

    def setNoeud2(self, value):
        self.__noeud2 = value

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getDistance(self):
        return self.__distance

    def setDistance(self, value):
        self.__distance = value

    def __str__(self):
        print(self.getId())
