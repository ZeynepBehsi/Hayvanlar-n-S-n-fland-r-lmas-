class Hayvanlar():
    def __init__(self, tür = "Bilgi yok..", renk= "Bilgi yok..", ayak_sayısı = "Bilgi yok..", beslenme = "Bilgi yok..", yasam_alanı = "Bilgi yok.."):
        self.tür = tür
        self.renk = renk
        self.ayak_sayısı = ayak_sayısı
        self.beslenme = beslenme
        self.yasam_alanı = yasam_alanı

    def bilgilerigoster(self):
        print("""
        Hayvanın özellikleri:
        
        Tür : {}
        Renk : {}
        Ayak sayısı : {}
        Beslenme şekli : {}
        Yaşam alanı : {}

        """.format(self.tür, self.renk,self.ayak_sayısı, self.beslenme,self.yasam_alanı))

# 1 - Köpek sınıfı
class Kopek(Hayvanlar):
    def __init__(self, tür, renk, ayak_sayısı, beslenme, yasam_alanı, cins, benek):
        super().__init__(tür, renk, ayak_sayısı, beslenme, yasam_alanı)
        self.cins = cins
        self.benek = benek

    def __len__(self):
        return self.ayak_sayısı

    def bilgilerigoster(self):
        print("""
        Hayvanın özellikleri:

        Tür : {}
        Renk : {}
        Ayak sayısı : {}
        Beslenme şekli : {}
        Yaşam alanı : {}
        Cinsi: {}
        Benek sayısı : {}


        """.format(self.tür, self.renk, self.ayak_sayısı, self.beslenme, self.yasam_alanı, self.cins, self.benek))

golden = Kopek("Köpek", " Kahverengi", 4, "Hepçil", "karasal yaşam", "Golden", "Yok")

golden.bilgilerigoster()

#2 Kuş sınıfını tanımlayalım

class Kuşlar(Hayvanlar):
    def __init__(self,tür, renk, ayak_sayısı, beslenme, yasam_alanı, cins, gaga_tipi):
        super().__init__(tür, renk, ayak_sayısı, beslenme, yasam_alanı)
        self.cins = cins
        self.gaga_tipi = gaga_tipi

    def bilgilerigoster(self):
        print("""
        Hayvanın özellikleri:

        Tür : {}
        Renk : {}
        Ayak sayısı : {}
        Beslenme şekli : {}
        Yaşam alanı : {}
        Cinsi: {}
        Gaga Tipi: {}""".format(self.tür, self.renk, self.ayak_sayısı, self.beslenme, self.yasam_alanı, self.cins, self.gaga_tipi))



serce = Kuşlar("Kuş", "Gri", 2,  "Hepçil", "Hava ve kara", "Serçe", "Kalın ve açık renkli"  )

serce.bilgilerigoster()

# 4 Atlar sınıfı

class Atlar(Hayvanlar):
    def __init__(self, tür, renk, ayak_sayısı, beslenme, yasam_alanı, cins, kuyruk_tipi):
        super().__init__(tür, renk, ayak_sayısı, beslenme, yasam_alanı)
        self.cins = cins
        self.kuyruk_tipi = kuyruk_tipi

    def bilgilerigoster(self):
        print("""
        Hayvanın özellikleri:

        Tür : {}
        Renk : {}
        Ayak sayısı : {}
        Beslenme şekli : {}
        Yaşam alanı : {}
        Cinsi: {}
        Gaga Tipi: {}""".format(self.tür, self.renk, self.ayak_sayısı, self.beslenme, self.yasam_alanı, self.cins, self.kuyruk_tipi))


midilli = Atlar("At", "Beyaz", 4, "otçul", "Karasal", "Little Pony", "Saçaklı")

midilli.bilgilerigoster()











