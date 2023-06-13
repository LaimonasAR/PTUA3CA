"""
    Pasiimti anksčiau sukurtą programos kodą
    Teste sukurti setUp() metodą, kuriame būtų inicijuotas klasės objektas
    Funkcijas perdaryti taip, kad jos gražintų duomenis
    Sukurti UNIT testą visoms funkcijoms
    Kiekvienai funkcijai turi būti mažiausiai 3 patikrinimai
    Maksimaliai patobulinti kodą, nuolatos leidžiant sukurtą UNIT testą
"""


class Sakinys:
    def __init__(self, tekstas="Zen of Python"):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def didziosiomis(self):
        return self.tekstas.upper()

    def mazosiomis(self):
        return self.tekstas.lower()

    def ieskoti(self, ieskomas):
        return self.tekstas.count(ieskomas)

    def pakeisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def atspausdintiZodi(self, skaicius):
        suskirstytas = self.tekstas.split()
        return suskirstytas[skaicius]

    def info(self):
        zodziu_kiekis = len(self.tekstas.split())
        skaiciai = sum(i.isnumeric() for i in self.tekstas)
        didziosios = sum(i.isupper() for i in self.tekstas)
        mazosios = sum(i.islower() for i in self.tekstas)
        return {
            "Žodžių kiekis": zodziu_kiekis,
            "Skaičiai": skaiciai,
            "Didžiosios": didziosios,
            "Mažosios": mazosios,
        }

    def __str__(self):
        return "Tekstas: " + self.tekstas


if __name__ == "__main__":
    mano_sakinys = Sakinys()
    print(mano_sakinys.atbulai())
    print(mano_sakinys.mazosiomis())
    print(mano_sakinys.didziosiomis())
    print(mano_sakinys.ieskoti("a"))
    print(mano_sakinys.pakeisti("Zen", "Ben"))
    print(mano_sakinys.atspausdintiZodi(2))
    mano_sakinys.info()
    print(mano_sakinys)
    mano_sakinys = Sakinys("Mano tekstas yra toks")
    print(mano_sakinys.atbulai())
    print(mano_sakinys.mazosiomis())
    print(mano_sakinys.didziosiomis())
    print(mano_sakinys.ieskoti("a"))
    print(mano_sakinys.pakeisti("Mano", "Savo"))
    print(mano_sakinys.atspausdintiZodi(2))
    mano_sakinys.info()
    print(mano_sakinys)
    mano_sakinys = Sakinys("Lorem ipsum dolor sit amet")
    print(mano_sakinys.atbulai())
    print(mano_sakinys.mazosiomis())
    print(mano_sakinys.didziosiomis())
    print(mano_sakinys.ieskoti("a"))
    print(mano_sakinys.pakeisti("Lorem", "Borem"))
    print(mano_sakinys.atspausdintiZodi(2))
    mano_sakinys.info()
    print(mano_sakinys)
