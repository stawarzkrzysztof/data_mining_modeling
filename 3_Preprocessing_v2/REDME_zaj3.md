# __Still working with pure Pandas__
## Done: __20th October 2023__
### Tasks:
__Zadanie na zajęcia nr 3 - preprocessing: integracja, sprawdzanie, oczyszczanie, normalizacja danych__  
W szkole średniej robiony jest prosty bilans uczniów - badanie wzrostu i wagi. Są 3 klasy - A, B, C, każda licząca ok. 15-25 os. Pomiary wykonują panie pielęgniarki Krysia, Marysia i Zbysia, każda dla innej klasy.
Każda zapisuje wyniki w osobnej tabelce do pliku CSV. Ale jak to w polskiej szkole, każdy robi po swojemu i jedna zapisuje wzrost w metrach, druga w centymetrach, jedna zapisuje wagę jako liczbę całkowitą, druga jako zmiennoprzecinkową.
jeszcze inna nie ma zainstalowanego Excela i robi to w notatniku, używając innych separatorów wartości i znaku dziesiętnego. W dodatku może się zdarzyć literówka i ktoś dostanie wzrost czterocyfrowy w cm, bo za długo wciśnie się klawisz 1 na starej 30-letniej klawiaturze. Żeby dopełnić katastrofy, trzech uczniów poszło na bilans drugi raz do innej klasy, żeby zwiać z lekcji, więc znajdują się na dwóch listach.
Pani Grażynka z sekretariatu ma teraz problem, bo musi szybko wysłać dane do kuratorium i czeka ją pewnie ręczne przepisywanie cyferek do Excela, żeby się wszystko zgadzało.

Bądź dobrym człowiekiem i pomóż pani Grażynce pisząc do tego automat, w którym pani Grażynka podaje tylko nazwy plików, a reszta robi się sama.
Do kuratorium należy wysłać:  
- wspólną listę uczniów i pomiarów bez podziału na klasy;  
- statystyki: min, max, średnią i medianę wzrostu oraz wagi dla całego zbioru danych;  
- w tabelce dodatkowo obliczone BMI każdego ucznia  
- dane dotyczące BMI: ile % w BMI stanowią osoby "optymalne", ile jest nadwagi, ile jest niedowagi (uproszczone warunki: tylko 3 przedziały, można wszystkie)  
- wykres punktowy wzrostu i wagi uczniów oraz wykres kołowy % zakresów BMI  
- współczynnik korelacji danych wzrostu i wagi
  
Uwzględnij problemy:
- Różne separatory i znaki dziesiętne w plikach, które należy połączyć
- Różne skale i formaty liczbowe wzrostu i wagi - ustal arbitralnie i przelicz wartości w odpowiednich kolumnach
- Duplikacja danych - uczniowie, którzy dwa razy poszli na bilans
- Błędy grube, czyli wzrost >1000cm (przyczyna problemu do usunięcia: duplikacja pierwszej cyfry)
- Generator danych (stworzony z użyciem ChatGPT, wymaga zainstalowania biblioteki Faker): generator.py

Przykładowe wygenerowane pliki z danymi do pobrania: students_A.csv ; students_B.csv ; students_C.csv

__Zadanie domowe__
Pogłębienie problemu: usuń 3 losowe wartości wzrostu i wagi z tabeli, zostawiając puste pola (usuń ręcznie albo napisz skrypt, który to zrobi).
Co może zrobić pani Grażynka, żeby mieć spokój i nie musieć ponawiać całych badań dla 3 osób z pustymi komórkami? Podpowiedź: kuratorium sprawdza dokładnie liczbę uczniów, zwraca uwagę na minima i maksima danych, ale nie testuje każdego ponownie.
Uwaga: Może to wpłynąć niekorzystnie na pojedyncze przypadki ze względu na przekłamanie stanu zdrowia, ale "statystyki mają się zgadzać".
Uwaga2: To nieetyczne i nie powinno się tak robić!

Do poćwiczenia praktycznego kodowania: wyślij maila od pani Grażynki z poziomu skryptu Pythona, załącz tabelki i obrazki w załączniku, a statystki w treści maila, dodaj tytuł, nadawcę, itd. Przydadzą się moduły smtplib i email. Dane serwera SMTP weź z prywatnej skrzynki

Inny przypadek danych wymagających obróbki przed dalszym działaniem: cars.csv; tutorial video (z zajęć dla EAIiIB)
