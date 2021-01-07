#1 Wczytanie datasetu
import csv

with open('iris.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader: 
        print(row)
              
etykiety = []  
dane = []
#2 Wypisanie etykiet
with open('iris.csv', 'r') as plikcsv:
    plikcsv = csv.reader(plikcsv, delimiter=',')
    etykiety = next(plikcsv)
    print(etykiety)

#3 Wypisanie danych całego datasetu
    dane = [wiersz for wiersz in plikcsv]
    print(dane)
#Wyswietlenie przedziału
wyswietlenie_wierszy1 = input("podaj początek przedziału ")
wyswietlenie_wierszy1 = int(wyswietlenie_wierszy1)
wyswietlenie_wierszy2 = input("podaj koniec przedziału ")
wyswietlenie_wierszy2 = int(wyswietlenie_wierszy2)
przedzial = dane[wyswietlenie_wierszy1:(wyswietlenie_wierszy2+1)]
print(przedzial)

#4 Podział datasetu na zbiór testowy, treningowy, walidacyjny
with open('iris.csv', 'r') as filecsv:
    reader = csv.reader(filecsv, delimiter=',')
    lines = list(reader)

treningowy = input('podaj numer wiersza treningowego: ')
treningowy = int(treningowy)
testowy = input('podaj numer wiersza testowego: ')
testowy = int(testowy)
walidacyjny = input('podaj numer wiersza walidacyjnego: ')
walidacyjny = int(walidacyjny)
print('zbiór_treningowy', lines[treningowy])
print('zbiór_testowy', lines[testowy])
print('zbiór_walidacyjny', lines[walidacyjny])

#5 Liczba klas decyzyjnych
klasy_decyzyjne = ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica')
print('klasy decyzyjne: ', len(klasy_decyzyjne))

#6 Dane dla podanej wartości klasy decyzyjnej
with open('iris.csv', 'r') as filecsv:
    reader = csv.reader(filecsv, delimiter=',')
    lines = list(reader)

klasa_decyzyjna1 = input('Podaj wiersz od 1 do 150 aby sprawdzić klasę decyzyjną: ')
klasa_decyzyjna1 = int(klasa_decyzyjna1)
if 0 < klasa_decyzyjna1 < 51:
    print('Klasa decyzyjna 1 Iris-setosa, jej dane to: ', lines[klasa_decyzyjna1])
else:
    print('Wartość spoza klasy decyzyjnej 1, sprawdź pozostałe klasy decyzyjne')

klasa_decyzyjna2 = input('Podaj wiersz od 1 do 150 aby sprawdzić klasę decyzyjną: ')
klasa_decyzyjna2 = int(klasa_decyzyjna2)
if 50 < klasa_decyzyjna2 < 101:
    print('Klasa decyzyjna 2 Iris-versicolor, jej dane to: ', lines[klasa_decyzyjna2])
else:
    print('Wartość spoza klasy decyzyjnej 2, sprawdź pozostałe klasy decyzyjne')
    
klasa_decyzyjna3 = input('Podaj wiersz od 1 do 150 aby sprawdzić klasę decyzyjną: ')
klasa_decyzyjna3 = int(klasa_decyzyjna3)
if 100 < klasa_decyzyjna3 < 151:
    print('Klasa decyzyjna 2 Iris-virginica, jej dane to: ', lines[klasa_decyzyjna3])
else:
    print('Wartość spoza klasy decyzyjnej 3, sprawdź pozostałe klasy decyzyjne')

#7 Zapisanie danych do pliku csv
fields = ['dane', 'sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'class']

rows = [['dane dla klasy decyzyjnej 1', '5.1', '3.5', '1.4', '0.2', 'Iris-setosa'],
['dane dla klasy decyzyjnej 2', '7.0', '3.2', '4.7', '1.4', 'Iris-versicolor'],
['dane dla klasy decyzyjnej 3', '6.3', '3.3', '6.0', '2.5', 'Iris-virginica']]

with open ('dane_klas_decyzyjnych.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    


