set PRODUCENCI;
set MAGAZYNY;
set SKLEPY;
set WARZYWA;
set TYGODNIE;

param maks_produkcja {PRODUCENCI, WARZYWA};
param pojemnosc_mag_centrala {MAGAZYNY};
param dystans_sklep_magazyn {SKLEPY, MAGAZYNY};
param dystans_magazyn_producent {PRODUCENCI, MAGAZYNY};
param sklep_prognoza_tyg {TYGODNIE, WARZYWA, SKLEPY};
param pojemnosc_mag_sklepu {SKLEPY};

param koszt_transportu; # PLN / (km*t)
param min_zapasy_sklep; # %

var transport_do_sklepow_tyg {SKLEPY, MAGAZYNY, WARZYWA, TYGODNIE};
var transport_do_magazynow_rok {MAGAZYNY, PRODUCENCI, WARZYWA};

# Zmienne pomocnicze
# stan na koniec tygodnia (po dostawie na początku oraz po sprzedarzy prognozy)
# stan_mag_sklep_tyg[s, w, t] + sklep_prognoza_tyg[t, w, s] to stan magazynu na początek tygonia PO dostawie
var stan_mag_sklep_tyg {SKLEPY, WARZYWA, TYGODNIE} >=0;

minimize calk_koszt_transportu:
	sum { s in SKLEPY, m in MAGAZYNY, w in WARZYWA, t in TYGODNIE }
		(transport_do_sklepow_tyg[s, m, w, t] * dystans_sklep_magazyn[s, m] * koszt_transportu) +
	sum { m in MAGAZYNY, p in PRODUCENCI, w in WARZYWA}
		(transport_do_magazynow_rok[m, p, w] * dystans_magazyn_producent[p, m] * koszt_transportu);

#Dla zmiennych pomocniczych:
# na zakończenie tygodnia
subject to aktualny_stan_mag_sklep {s in SKLEPY, w in WARZYWA, t in TYGODNIE}:
	stan_mag_sklep_tyg[s, w, t] =
		sum{ i in 1..t }  # suma prefiksowa
			(sum { m in MAGAZYNY } (transport_do_sklepow_tyg[s, m, w, i]) - sklep_prognoza_tyg[i, w, s]);

# na samym początku roku do magazynów przyjeżdżają świerze warzywka. potem w przeciągu roku dostarczane są do
# warzywniaków. Dostarczane są na początku tygodnia. Czyli na samym początku roku jest dostawa warzyw do
# magazynów oraz odrazu odbywa się też pierwsza dostawa do sklepów

# Zmienne większe od zera:
subject to transport_do_sklepow_tyg_min { s in SKLEPY, m in MAGAZYNY, w in WARZYWA, t in TYGODNIE }: transport_do_sklepow_tyg[s, m, w, t] >=0;
subject to transport_do_magazynow_rok_min { m in MAGAZYNY, p in PRODUCENCI, w in WARZYWA} : transport_do_magazynow_rok[m, p, w] >=0;

# limity pojemności magazynów centrali
subject to mag_centrala_limit_max {m in MAGAZYNY}: sum {w in WARZYWA, p in PRODUCENCI} transport_do_magazynow_rok[m, p, w] <= pojemnosc_mag_centrala[m];

# warzywa brane są z magazynów
subject to transport_warzyw_z_magaznow_do_sklepow {m in MAGAZYNY, w in WARZYWA}:
	sum {s in SKLEPY, t in TYGODNIE} transport_do_sklepow_tyg[s, m, w, t] = sum{p in PRODUCENCI} transport_do_magazynow_rok[m, p, w];

# limity pojemności magazynów przysklepowych
subject to mag_sklep_limit_max {s in SKLEPY, t in TYGODNIE}: sum {w in WARZYWA} (stan_mag_sklep_tyg[s, w, t] + sklep_prognoza_tyg[t, w, s]) <= pojemnosc_mag_sklepu[s];
subject to mag_sklep_limit_min {s in SKLEPY, t in TYGODNIE, w in WARZYWA}: stan_mag_sklep_tyg[s, w, t] >= min_zapasy_sklep * sklep_prognoza_tyg[t, w, s];

# limit maksymalnej produkcji warzyw producentów
subject to produkcja_warzyw_max {p in PRODUCENCI, w in WARZYWA}: sum { m in MAGAZYNY} transport_do_magazynow_rok[m, p, w] <= maks_produkcja[p, w];
