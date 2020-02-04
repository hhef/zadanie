"""Zaimplementuj klasę, która będzie działała podobnie do Pythonowego słownika (dict)
BEZ używania słownika w swojej implementacji.

Zaimplementuj metody:
   - set(klucz, wartość) - wprowadzanie i nadpisywanie
   - get(klucz) - wyjmowanie
   - remove(klucz) - usuwanie

Twoja klasa pownna zachowywać się podobnie do słownika, to znaczy:
telefony = {}   Twój konstruktor na pewno będzie inny

Wprowadzanie danych
telefony['Ala'] = '123-456-789'
telefony['Tomek'] = '111-222-333'
Twoja klasa może implementować metodę set(klucz, wartość) zamiast operatora []

Wyjmowanie wartości
print(telefony.get('Ala'))   wypisze 123-456-789

nadpisywanie wartości
telefony['Ala'] = '999-888-777'
print(telefony.get('Ala'))  wypisze 999-888-777

Usuwanie wartości
del telefony['Ala']
Twoja klasa może implementować metodę remove(klucz) zamiast słowa kluczowego `del`

Pytania:
   - Jak szybkie będzie wyszukiwanie elementów?
   - Jak szybkie będzie dodawanie / usuwanie elementów?"""

class NowySlownik:
    osoby = []
    numery = []

    def set(self, name, number):
        if name not in self.osoby:
            self.osoby.append(name)
            self.numery.append(number)
        else:
            for i in range(0, len(self.osoby)):
                if name == self.osoby[i]:
                    self.numery[i] = number

    def get(self, name):
        for i in range(0, len(self.osoby)):
            if name == self.osoby[i]:
                return self.numery[i]

    def delete_person(self, name):
        for i in range(0, len(self.osoby)):
            if name == self.osoby[i]:
                self.osoby.pop(i)
                self.numery.pop(i)
                break


telefony = NowySlownik()
telefony.set("Ala", '123-123-123')
telefony.set("Marian", '321-321-321')
print(telefony.osoby)
print(telefony.numery)
print(telefony.get("Ala"))
print("____________________________")
telefony.set("Ala", '444-555-666')
print(telefony.osoby)
print(telefony.numery)
print("________________________")
print(telefony.get("Ala"))
print(telefony.get("Marian"))
print("____________________________")
telefony.delete_person("Ala")
print(telefony.osoby)
print(telefony.numery)
print("____________________________")
telefony.delete_person("Marian")
print(telefony.osoby)
print(telefony.numery)
