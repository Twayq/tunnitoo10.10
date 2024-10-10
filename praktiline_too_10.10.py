"""Matemaatilised tehted"""

import math

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b
a = float(input("Sisesta oma a:"))
b = float(input("Sisesta oma b:"))
# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
hupotenuusC = math.sqrt((a ** 2) + (b ** 2))
P = a + b + hupotenuusC
S = (a * b) / 2

