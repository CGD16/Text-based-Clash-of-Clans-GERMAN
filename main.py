if __name__ == '__main__':
    from Sammler import Sammler
    from Lager import Lager
    import time
    import pickle
    import os

    path = "coc_data.p"
    isExist = os.path.exists(path)
    if isExist:
        with open("coc_data.p", "rb") as file:
            goldlager, goldMine0 = pickle.load(file)
            print("... wurde geladen")
    else:
        goldMine0 = Sammler("Miene für Gold")
        goldlager = Lager("Goldlager 1")

    diff_sec = 0

    end = False
    while not end:
        in_seconds_before = time.time()
        input_user = input("Für Informationen, drücke bitte '#': ")
        in_seconds_after = time.time()

        diff_sec += (in_seconds_after - in_seconds_before)

        # print(goldMine0.getZustand_Sammler())
        print(goldlager.getZustand_lager(goldMine0.runningKapazitaet(diff_sec)))
        print(goldlager.levelUp_Zustand_Gebaeude())

        diff_sec = 0
        print()
        if input_user != "#":
            end = True
            # pickle
            data = goldlager, goldMine0
            with open("coc_data.p", "wb") as file:
                pickle.dump(data, file)
            break
        if input_user == "":
            end = False
