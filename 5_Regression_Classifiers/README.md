# __Linear and Multivariate Regression models testing on randomly generated data__
## Done: __10 November 2023__
### Tasks:
__Zadanie na zajęcia nr 5 - regresja liniowa: jak długo się uczyć na egzamin?__  
Na uczelni przeprowadzono ankietę wśród studentów, mającą określić, co miało wpływ na wyniki egzaminu.

Studenci byli pytani ile godzin spędzili nad nauką (x1), ile godzin spali przed egzaminem (x2), ile litrów kawy wypili dzień przed egzaminem (x3).

Każdy student podał też liczbę punktów oraz miał przypisaną ocenę. Ankietowanych studentów było 25. Na tej podstawie zbudowano modele wiążące liczbę punktów lub ocenę z tymi trzema czynnikami, zauważając w wielu przypadkach pewną korelację ilości punktów z ilością godzin spędzonych nad nauką oraz ilością przespanych godzin.

Skorzystaj z generatora danych dostępnego w pliku zajecia5.ipynb lub zajecia5.py, podziel dane na zbiór trenujący i testujący w proporcji 80/20, a następnie przeprowadź regresję liniową na różnych przypadkach:

- liczba punktów / ocena zależy tylko od ilości godzin spędzonych nad nauką - regresja 1D
- liczba punktów / ocena zależy tylko od ilości godzin spędzonych nad nauką (x1) oraz przespanych (x2) - regresja 2D
- liczba punktów / ocena zależy od udziału wszystkich czynników x1, x2, x3
Po wykonaniu regresji określ poziom dopasowania modelu, obliczając współczynnik R^2 dla danych testowych.

Na podstawie uzyskanych wyników wykonaj/odpowiedz:

- Dla regresji 1D narysuj wykres z prostą obrazującą zależność - czy jej przebieg jest zgodny z pomiarami?  
- Który z modeli (a,b,c) wydaje się najlepszy do przewidywania wyników punktowych?  
- Czy dokładniejsze będzie przewidywanie liczby punktów czy oceny?  
- Uruchom generator dla 1000 wyników zamiast 25. Czy wpłynęło to istotnie na wyniki regresji?  
- Zmień podział danych trenujących/testujących na proporcje 90/10 oraz 50/50. Czy wpłynęło to istotnie na wyniki regresji?  
- Jaki wynik według różnych modeli osiągnie student, który uczył się 20 godzin, spał 8 godzin* i wypił 2 litry kawy* (* - jeśli dany model nie przewiduje tego czynnika, pomiń go).  
- Jakie warunki w różnych modelach mogą "wystarczyć" do zaliczenia egzaminu (50 punktów) dla każdego przypadku (dla przypadków 2D i 3D będzie to więcej niż jeden sposób uzyskania wyniku).  
Należy pamiętać, że korzystamy z generatora i "rzeczywistość" jest generowana na podstawie przyjęcia jakiegoś założenia odnośnie relacji danych, z dodaną pewną losowością - przeprowadzenie takiej analizy na danych rzeczywistych mogłoby prowadzić do wniosków, że nie da się realnie przewidzieć wyników egzaminu na podstawie podanych czynników.  
