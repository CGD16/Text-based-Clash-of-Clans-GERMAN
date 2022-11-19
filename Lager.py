from Gebaeude import Gebaeude


class Lager(Gebaeude):

    def __init__(self, ressource_name, lagerkapazitaet=500000):
        Gebaeude.__init__(self)
        # super().__init__()
        self.ressource_name = ressource_name
        self.lagerkapazitaet = lagerkapazitaet
        self.ressource_zustand = 0

    def getZustand_lager(self, kapazitaet_jetzt):
        self.kapazitaet_jetzt = kapazitaet_jetzt
        self.ressource_zustand += self.kapazitaet_jetzt
        return "So viel wird gelagert: {}".format(round(self.ressource_zustand, 2))


"""
  def levelUp(self):
    self.lvl += 1
    return self.lvl

  def levelUp_Zustand(self):
    return "Lager Level: {}".format(self.lvl)    
"""