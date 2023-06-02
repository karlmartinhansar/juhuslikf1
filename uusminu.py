import random

def funktsiooninimi(vahemik):
    aeg = round(random.uniform(vahemik[0], vahemik[1]), 3)
    return aeg





nimekiri = ["Lewis", "Valtteri", "Max", "George", "Karl"]
ajad = []

for nimi in nimekiri:
    sekt1 = funktsiooninimi([23, 26])
    sekt2 = funktsiooninimi([23, 26])
    sekt3 = funktsiooninimi([23, 26])
    ajad.append([nimi, sekt1, sekt2, sekt3])



def aja_vormindamine(aeg):
    tund = int(aeg / 3600)
    minut = int((aeg % 3600) / 60)
    sekund = int(aeg % 60)
    tuhanded = int((aeg % 1) * 1000)
    return f"{tund:02d}:{minut:02d}:{sekund:02d}.{tuhanded:03d}"


ajad_sorted = sorted(ajad, key=lambda x: x[1])



def voi_aeg():
    aegade_summa = 0
    for i in range(10):
        aeg = funktsiooninimi([23, 26])
        aegade_summa += aeg
    return aegade_summa





ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])


ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])



ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])


ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])

for i, s in enumerate(sonum_sorted):
    ringid_formatted = str(s[2])
    if ringid_formatted == "[]":
        ringid_formatted = ""
    else:
        ringid_formatted = ringid_formatted[1:-1]
    nimi = s[0]
    aeg_formatted = aja_vormindamine(s[1])
    if i == 0:
        vahe_formatted = ""
    else:
        vahe_formatted = aja_vormindamine

with open('Result.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)