class Inson:
    def __init__(self, ism, tugilgan_yil):
        self.ism = ism
        self.tugilgan_yil = tugilgan_yil

    def yosh_hesabla(self, joriy_yil=2026):
        return joriy_yil - self.tugilgan_yil

insonlar = [
    Inson("Ali", 1990),
    Inson("Vali", 2001),
    Inson("Jalol", 1995)
]

for inson in insonlar:
    print(f"{inson.ism} {inson.yosh_hesabla()} yoshda")
