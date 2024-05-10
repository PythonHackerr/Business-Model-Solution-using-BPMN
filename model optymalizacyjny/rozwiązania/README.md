# Legenda rozwązań:
Uwaga: Kolumny zawierające same zera zostały ukryte.

## Ogólne informacje
Dla każdego zestawu danych `generated_dataN.dat` pliki z rozwiązaniami znajdują się w folderze `dataN`

Wynik minimalizacji (całkowity koszt transportu) znajduje się w pliku `podsumowanie.txt`

## Pliki z rozwiązaniami

### Plik `rozwiązania/dataN/01-tyg_trans_warz_sklep.txt`
> zawiera informację o tym, ile ton do danego sklepu należy przetransportować pewnego warzywa z pewnego magazynu centrali w danym tygodniu

Na przykład:
```
transport_do_sklepow_tyg [*,Piaseczno,Buraki,*] (tr)
:  ArabicGroceryShop DobryWarzywniak Krzesak UKermita UPanaWojtka    :=
1         0.000            1.114       1.578   1.032      0.000
[ ... ]
```
Oznacza że z magazynu *Piaseczno*, należy przetransportować pewną ilość ton *Buraków* do jakiegoś z powyższych sklepów w danym tygodniu.

### Plik `rozwiązania/dataN/02-rok_trans_warz_magazyny.txt`
> zawiera informację o tym, ile ton do danego magazynu należy przetransportować danego warzywa od określonego producenta

Na przykład:
```
transport_do_magazynow_rok [Piaseczno,*,*]
:              Buraki   Kapusta  Marchew Ziemniaki    :=
Blonie           0.000    0.000    0.000     0.000
GoraKalwaria   190.000   70.000   90.000   160.000
Ksiazenice       0.000    0.000    0.000     0.000

```
Wyświetla ile danego ważywa zostanie przetransportowane z każdego producenta (Blonie, GoraKalwaria...) do magazynu Piaseczno

### Plik `rozwiązania/dataN/03-tyg_trans_sklepy_total.txt`

> Ile łącznie w danym tygodniu ton warzyw zostało przetransportowanych do sklepu?



### Plik `rozwiązania/dataN/04-rok_trans_magazyny_total.txt`

> Ile w sumie ton warzyw zostało przetransportowanych pomiędzy parą magazyn-producent w tym roku?



### Plik `rozwiązania/dataN/05-koszt_dostaw_do_sklepów_total.txt`

> W tym roku, jaki był łączny koszt transportu warzyw do danego sklepu? (PLN)



### Plik `rozwiązania/dataN/06-koszt_dostaw_do_magazynow_total.txt`

> W tym roku, jaki był łączny koszt transportu warzyw do danego magazynu? (PLN)



### Plik `rozwiązania/dataN/07-koszt_dostaw_od_producentow_total.txt`

> Jak rozkłada się koszt transportu warzyw do magazynu rozbijając go na poszczególnych producentów? Koszty te sumują się do tych samych wartości co w pliku 06[..] (PLN)



### Plik `rozwiązania/dataN/08-suma_dostaw_do_sklepow_total.txt`

> Ile łącznie zostało w tym roku dostarczonych warzyw do każdego ze sklepów?



### Plik `rozwiązania/dataN/09-suma_dostaw_do_magazynow_total.txt`

> Ile łącznie zostało w tym roku dostarczonych warzyw do każdego z magazynów?



### Plik `rozwiązania/dataN/10-suma_dostaw_od_producentow_total.txt`

> Ile łącznie zostało w tym roku przetransportowanych warzyw od każdego producenta?


### Plik `rozwiązania/dataN/11-koszt_dostaw_do_sklepów_na_przestrzeni_roku.txt`

> Jaki był łączny koszt dostaw w danym tygodniu? (PLN)

### Plik `rozwiązania/dataN/12-suma_dostaw_do_sklepów_na_przestrzeni_roku.txt`

> Ile łącznie ton zostało przetransportowane do sklepów w tym tygodniu?

### Plik `rozwiązania/dataN/13-koszt_dostaw_do_poszczególnych_sklepów_na_przestrzeni_roku.txt`

> Ile kosztowały dostawy do danego sklepu w poszczególnych tygodniach?

### Plik `rozwiązania/dataN/14-suma_dostaw_do_poszczególnych_sklepów_na_przestrzeni_roku.txt`

> Ile ton warzyw zostało przetransportowane do danego sklepu w danym tygodniu?

