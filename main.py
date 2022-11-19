

if __name__ == '__main__':
    from Sammler import Sammler
    from Lager import Lager
    import time
    # from pickle

    goldlager = Lager("Goldlager 1")
    diff_sec = 0

    end = False
    while not end:
        in_seconds_before = time.time()
        input_user = input("Für Informationen, drücke bitte '#': ")
        in_seconds_after = time.time()

        diff_sec += (in_seconds_after - in_seconds_before)

        goldMine0 = Sammler("Miene für Gold")
        # print(goldMine0.getZustand_Sammler())

        print(goldlager.getZustand_lager(goldMine0.runningKapazitaet(diff_sec)))
        # print(goldlager.levelUp_Zustand())

        diff_sec = 0
        print()
        if input_user != "#":
            end = True
            break
        if input_user == "":
            end = False
