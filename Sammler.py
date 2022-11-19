from Gebaeude import Gebaeude


class Sammler(Gebaeude):
    def __init__(self, ressource_name, kapazitaet=350000, produktionsrate=6300): # produktionsrate=None
        Gebaeude.__init__(self)
        self.ressource_name = ressource_name
        self.kapazitaet = kapazitaet
        self.produktionsrate = produktionsrate

    def getZustand_Sammler(self):
        return "Nutzen: {} \nLevel: {} \nKapazität: {} \nProduktionsrate (pro Stunde): {} \nTrefferpunkte: {}".format(
            self.ressource_name, self.level, self.kapazitaet, self.produktionsrate, self.trefferpunkte)

    def checkKapazitaet(self):
        if self.kapazitaet >= 350000:  # 350000 kann eigentlich nicht geschrieben werden
            return "Sammler ist voll"
        return "Kapazitaet: {}".format(self.kapazitaet)

    def runningKapazitaet(self, diff_sec):
        self.kapazitaet = (diff_sec / 3600 * self.produktionsrate)
        print("Kapazität: {}".format(round(self.kapazitaet, 2)))
        return round(self.kapazitaet, 2)

    def runningLevel(self):
        self.kapazitaet *= self.upgrade
        self.produktionsrate *= self.upgrade
        self.level += 1