import pandas as pd
import numpy as np
import random
random.seed(2023)

#  funkcja do liczenia wierszy
def count_rows(df):
    return df.shape[0]

#  funkcja przewidująca klase działająca jak klasyfikator bayesowski
def predict_with_bayes(row2predict, train_set):
    #  podział datasetu na dwa mniejsze zalezne od klasy
    class_zero = train_set[train_set.iloc[:, -1]==0]
    class_one = train_set[train_set.iloc[:, -1]==1]

    #  wyznaczenie prawdopodobienstwa poczatkowego 
    apriori_zero = count_rows(class_zero) / count_rows(train_set)
    apriori_one = count_rows(class_one) / count_rows(train_set)
    
    #  duze pi, czyli mnozenie w petli prawdopodobienstw
    for i, feature in enumerate(row2predict):
        apriori_zero *= (class_zero.iloc[:, i]==feature).sum()/count_rows(class_zero)
        apriori_one *= (class_one.iloc[:, i]==feature).sum()/count_rows(class_one)
        
    #  wypisanie wynikow i predykcja
    print(f"Probability of class=0: {apriori_zero}") 
    print(f"Probability of class=1: {apriori_one}")
    print(f"Prediction: class={0 if apriori_zero > apriori_one else 1}")

#  generator danych
df = pd.DataFrame(
    np.array([
        [random.randint(1, 5), random.randint(0, 1), random.randint(0,1)] 
        for i in range(30)
        ]), 
    columns=["cieplo", "zachmurzenie", "pada"])

#  klasyfikacja ręczna training setu
df["wyjde_na_spacer"] = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0,\
    0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]

#  wyniki funkcji
predict_with_bayes([5, 0, 0], train_set=df)
predict_with_bayes([1, 1, 1], train_set=df)
predict_with_bayes([3, 1, 0], train_set=df)
predict_with_bayes([4, 0, 1], train_set=df)