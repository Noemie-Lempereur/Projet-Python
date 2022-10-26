
class noeud :
    __idnglob = 0

    def __init__(self):
        self.__idn = noeud.__idnglob
        noeud.__idnglob += 1
        self.__links = []
        """Liste constitué des liens rattachés au noeud"""
#

    def getIdn (self):
        return self.__idn

    def setIdn (self, id) :
        self.__idn =id

    def getLinks (self) :
        return self.__links

    def setLinks (self, links) :
        self.__links = links

    def __str__(self):
        print (self.getIdn())

    def ajoutIdentifiantLien (self,lienid) :
        self.__links.append(lienid)

    def affichageIdentifiantLien (self) :
        for i in range (len(self.__links)) :
            print(self.__links[i].getId())


