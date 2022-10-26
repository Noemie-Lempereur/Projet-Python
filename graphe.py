from lien import lien
from noeud import noeud
import math


class graphe(lien, noeud):
    _idg = 0

    def __init__(self):
        self._nbrenoeud = 0
        self._dictNoeud = dict()
        self._dictLien = dict()

    def getNbreNoeud(self):
        return self._nbrenoeud

    def getDNoeud(self):
        return self._dictNoeud

    def getDLien(self):
        return self._dictLien

    def addNoeud(self, Noeud):
        self._dictNoeud[Noeud.getIdn()] = Noeud
        self._nbrenoeud += 1

    def addLien(self, Lien):
        self._dictLien[Lien.getId()] = Lien
        Lien.getNoeud1().ajoutIdentifiantLien(Lien.getId())
        Lien.getNoeud2().ajoutIdentifiantLien(Lien.getId())

    def obtenirProchainNoeud(self, noeudid):
        dict1 = dict()
        for i in self._dictLien.values():
            if (int(i.getNoeud1().getIdn()) == noeudid):
                dict1[i.getNoeud2().getIdn()] = i.getDistance()
            if (int(i.getNoeud2().getIdn()) == noeudid):
                dict1[i.getNoeud1().getIdn()] = i.getDistance()
        return dict1

    def __str__(self):
        print("noeud")
        for cle, valeur in self._dictNoeud.items():
            valeur.__str__()
        print("lien")
        for c, v in self._dictLien.items():
            v.__str__()

    def Djikstra(self, ndepart, narrive):
        P = list()
        distList = [math.inf] * self._nbrenoeud
        distList[ndepart - 1] = 0

        precList = [ndepart] * self._nbrenoeud
        precList[ndepart - 1] = None

        N = ndepart
        while P.__len__() < self._nbrenoeud:
            prochainNoeud = self.obtenirProchainNoeud(N)
            for i in P:
                prochainNoeud.pop(i, None)
            for k, distance in prochainNoeud.items():
                if (distList[k - 1] > distance + distList[N - 1]):
                    distList[k - 1] = distance + distList[N - 1]
                    precList[k - 1] = N
            P.append(N)
            P1 = distList.copy()
            for i in P:
                P1[i - 1] = math.inf
            N = P1.index(min(P1)) + 1
        distfinale = distList[narrive - 1]
        chemin = list()
        tmpNoeud = narrive
        while tmpNoeud != ndepart:
            tmpNoeud = precList[tmpNoeud - 1]
            chemin.append(tmpNoeud)
        return chemin, distfinale
