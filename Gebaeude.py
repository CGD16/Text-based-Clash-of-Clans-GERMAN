# pro Level up 50% mehr Gehalt, kapazitaet, produktionsrate, lagerkapazitaet - später
class Gebaeude():
    def __init__(self):
        self.trefferpunkte = 500000
        self.level = 1
        self.upgrade = 1.5

        def levelUp(self):
            self.level += 1
            self.trefferpunkte *= self.upgrade
            return self.level

    def levelUp_Zustand_Gebaeude(self):
        return "Gebäude Level: {}".format(self.lvl)

    # brauche ich nicht wirklich
    # def upgrade_methode(self):
        # return self.upgrade
