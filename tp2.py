from graphe import graphe
from noeud import noeud
from lien import lien
import csv
#
def creationGraphe(idg,filepath) :
    g = graphe()
    g._idg = idg
    with open(filepath,newline ='') as file :
        reader =csv.reader(file, delimiter ='\t')
        corentin = int (next(reader)[0])
        for row in reader:
            good1 = 0
            good2 = 0
            n1 = None
            n2 = None
            for k,val in g._dictNoeud.items() :
                if (k== row[0]) :
                    n1 =val
                    good1 = 1
                if (k == row[1]) :
                    n2 = val
                    good2 = 1
            if (good1 == 0) :
                n1 = noeud()
                n1.setIdn(int (row[0]))
                g.addNoeud(n1)
                good1 =0
            if (good2 == 0) :
                n2 = noeud()
                n2.setIdn(int(row[1]))
                g.addNoeud(n2)
                good2 =0
            dist = row[2]
            l1 = lien(n1,n2,float(row[2]))
            g.addLien(l1)

    g._nbrenoeud = corentin
    g.__str__()
    return g


g =creationGraphe(1,'fileGraph1.csv')
print (g.Djikstra(1,4))




# g =graphe()
# n1= noeud()
# n2 =noeud()
# n3 = noeud()
# l1 =lien(n1,n2,4)
# l2 = lien (n1, n3, 12)
# l3 = lien (n2,n3,2)
# g.addNoeud(n1)
# g.addNoeud(n2)
# g.addNoeud(n3)
# g.addLien(l1)
# g.addLien(l2)
# g.addLien(l2)

