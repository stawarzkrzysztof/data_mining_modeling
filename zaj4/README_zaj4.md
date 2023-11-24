# __Using PCA to show how Pokemon's Stats and Types are NOT correlated xd__
## Done: __27th October 2023__
### Tasks:
__Zadanie na zajęcia nr 4 - redukcja wielowymiarowości w bazie danych Pokemonów__  
Zagadnienie wielowymiarowości jest zgrabnie pokazane na przykładzie Pokemonów na blogu Mirosława Mamczura.

Wykorzystajmy zatem bazę Pokemonów dostępną w pliku pokemon.csv (źródło), żeby zobrazować na czym polega redukcja wielowymiarowości.

Zastosuj na podanej bazie algorytm PCA i zredukuj wymiary do 2:

- "ręcznie", wykorzystując kolejne kroki PCA: standaryzacja, obliczaniem macierzy kowariancji, wartości i wektorów własnych, wyboru 2 składowych głównych oraz transformacji danych na nowe składowe - skorzystamy z Numpy;  
- wykorzystując gotową funkcję do PCA z biblioteki Scikit-learn;
a następnie zwizualizuj dane TYPÓW Pokemonów na wykresie 2D.
Czy na podstawie takiej redukcji danych i wizualizacji da się wykonać prostą klasteryzację? Co możemy odczytać z takich danych? Czy możemy coś odczytać po redukcji danych (np. wybrania tylko określonych typów)?


