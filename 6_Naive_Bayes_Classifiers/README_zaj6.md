# __Naive Bayes Classifiers with illness, wine and spam/ham classification__
## Done: __17th November 2023__
### Tasks:
__Zadanie na zajęcia nr 6 - naiwny klasyfikator Bayesa: prosty filtr antyspamowy w SMS-ach__  
Dawno, dawno temu, kiedy sieć LTE była jeszcze w niedostępna, a sieć 3G nie pozwalała na sprawną obsługę Internetu w telefonach, obecni dorośli używali do komunikacji głównie SMSów. Jeden kosztował ok. 20 groszy. Oczywiście jest to totalnie nieistotne dla naszego zadania.

Korzystając z bazy smsów dostępnej w pliku sms_spam.csv (uwaga na kodowanie znaków!), w której treści smsów są wstępnie zaklasyfikowane jako "spam" lub "ham" (czyli nie-spam), podziel dane na zbiór trenujący i testowy w proporcjach 90/10, zastosuj naiwny klasyfikator Bayesa do oznaczania treści jako spam i sprawdź jego skuteczność na danych testowych.

Zaprezentuj dane na wykresach przedstawiających % danych spam/ham: dane rzeczywiste ze zbioru testowego oraz dane z klasyfikatora. Wyświetl treści smsów, które zostały zaklasyfikowane: fałszywie pozytywne (czyli zwykłe wiadomości, zaklasyfikowane jako spam) oraz fałszywie negatywne (czyli wiadomości ze spamem, które dotrą do użytkownika jako poprawne). Czy obserwujesz jakieś zależności w treściach, które mogą wpłynąć na takie zaklasyfikowanie?

__Zadanie dodatkowe - ręczne obliczenie prawdopodobieństwa Bayesa dla zdarzeń (możesz skorzystać z ChatGPT, żeby zobaczyć obliczenia i kod - ale uważaj na błędy!)__  

Załóżmy, że słowo "xxx" oznacza spam na 90%, a słowo "bitcoin" spam na 80%. Załóżmy, że są to sprawy od siebie niezależne. Do obliczeń załóż dodatkowo, że pozostałe słowa nie mają wpływu na spam/ham (P_word_spam = P_word_ham = 1), a prawdopodobieństwa a priori P_spam_prior = P_ham_prior = 0.5.

Korzystając z twierdzenia Bayesa, oblicz prawodpodobieństwo, że mail o treści "give me bitcoin for xxx" będzie spamem.

__Zadanie BONUS na zajęcia nr 5/6 - algorytm KNN a brakujące wyniki wyborów__  
Plik exitpoll.csv zawiera dane z wyników exit poll w wyborach parlamentarnych w 2023: województwo, miasto wojewódzkie, jego szerokość i długość geograficzna oraz nazwa partii, która wygrała tam wybory. [TVN24] Wyniki wyborów wizualnie na mapie

Symulujemy sytuację, w której nie mamy wyników wyborów dla województw: dolnośląskiego, lubelskiego oraz śląskiego [usuń je z tabeli przed trenowaniem]

Wykorzystaj algorytm KNN do przewidzenia wyników wyborów w tych województwach, na podstawie pozostałych wyników w innych województwach ("nie wiem co mam zrobić, więc zapytam sąsiadów i zagłosuję tak jak oni mówią").

- Jakie wyniki zaobserwujesz dla k=3, a jakie dla k=10?  
- Zmień zestaw brakujących województw, na przykład na tylko skrajnie zachodnie lub skrajnie wschodnie- jak to może wpłynąc na wyniki?  
- Czy gdyby nie typowa dla Polski zależność "podziału" w wynikach wyborów i nie tylko (tzw. Polska "A" i "B"), takie przewidywanie miałoby sens?  
- Jakie dane musielibyśmy posiadać, żeby precyzyjniej przewidzieć wyniki wyborów we wszystkich miastach Polski?  
- Czy na podstawie tylko takich danych moglibyśmy przewidzieć, z której partii pochodziłby prezydent w wyborach prezydenckich (założenie: głosuje się na partię, a nie człowieka)? (wskazówka: wyniki wyborów drugiej tury w 2020, podział na województwa).
