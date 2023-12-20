class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def cetak(self):
        print( "Nama\t\t:", self.name, "\nMakanan\t\t:", self.makanan, "\nHidup\t\t:", self.hidup, "\nBerkembang biak\t:", self.berkembang_biak)

class Badak(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis, cula):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.cula = cula
    
    def cetak(self):
        super().cetak()
        print("Jenis\t\t:", self.jenis, "\nCula\t\t:", self.cula)
    
    def warna(self):
        print("nwarna\t\t: Coklat")
    
    
class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kelompok, jantung):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.kelompok = kelompok
        self.jantung = jantung
    
    def cetak(self):
        super().cetak()
        print("Kelompok\t:", self.kelompok, "\nJantung\t\t:" , self.jantung)
    
    def alat_nafas(self):
        print("Alat bernafas\t: Insang")

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis, mata):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.mata = mata
    
    def cetak(self):
        super().cetak()
        print("Jenis\t\t:", self.jenis, "\nMata\t\t:", self.mata)
    
    def alat_nafas2(self):
        print("Alat Bernafas\t: Paru-Paru")

#objek Animal
satu = Animal("Kambing", "Rumput", "Darat", "Melahirkan")
satu.cetak()
print("===========================================================")

#objek Badak
dua = Badak("Badak", "Rumput", "Darat", "Melahirkan", "Badak Jawa", "1")
dua.cetak()
dua.warna()
print("===========================================================")

#objek Ikan
tiga = Ikan("Ikan Lele ",  "Mikroorgasme air", "Air", "Bertelur", "Ikan bertulang keras", "1 jantung")
tiga.cetak()
tiga.alat_nafas()
print("===========================================================")

#objek Ular
empat = Ular("Ular",  "tikus, kodok, dan burung", "darat(ladang dan pemukiman)", "bertelur", "Cobra", "Tajam")
empat.cetak()
empat.alat_nafas2()
