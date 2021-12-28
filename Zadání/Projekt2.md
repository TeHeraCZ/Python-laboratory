# Projekt číslo 2 - Generátor náhodných čísel
Zadání: Udělej program, který pomocí dvou čísel (počáteční a koncová hodnota) a následně dle rozsahu (také integer) vygeneruje náhodná čísla.

## For cyklus
Tento cyklus můžeme použít například, když potřebujeme danou funkci zopakovat. Zároveň nemusíme zbytečně psát stejný řádek několikrát.
```python
for x in range(rozsah): # tento program se zopakuje dle hodnoty rozsah, x je aktualni číslo běhu od 0 do hodnoty rozsah
  print(x) # vypíše hodnotu x ( při každém běhu se zvyšuje o 1 )
```

## Knihovna random
 Pro vygenerování náhodného čísla můžeme využít např. tuto knihovnu, která nám urychlí celý proces.

### Importování
Aby bylo možné tuto knihovnu využít, je nutné ji nejprve importovat do programu, to lze provést tímto způsobem
```python
    import random # tato funkce nám naimportuje výše zmíněnou knihovnu
```
### Použití knihovny
Pro vygenerování celého čísla se následně používá tato funkce
```python
    random.randint(a, b) # vrátí int v rozsahu a, b
```
## Použití programu
Program se zeptá uživatele na počáteční a koncové číslo, následně se zeptá počet čísel, které je nutné vygenerovat (Viz ***##Knihovna random*** ). Dále program vypíše daný počet náhodných čísel v zadaném rozsahu.

## Odevzdání
Na GitHub, branch ***projekt2***
