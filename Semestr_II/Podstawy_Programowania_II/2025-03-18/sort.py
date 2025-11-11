bombelek = [5,3,7,2,1]
# Sortowanie ASC
# Sortowanie bombelkowe (bubble sort)
# Porównanie kolejnych par liczb
# jezeli elementy 1 jest większy od elementu 2 to (n-1):
#   zamiana miejsczami liczb

def bubble_sort(lista_do_posortowania):
    #Funkcja sortowania liczb (metoda przez bombelkowanie)
    n = len(lista_do_posortowania)  # Długość listy
    for i in range(n):  # Przejście przez listę n razy
        zmiana = False # Z założenia brak zmiay
        for j in range(0, n - i - 1):  # Przejście przez nieposortowaną część listy
            if lista_do_posortowania[j] > lista_do_posortowania[j + 1]:  # Porówywanie par elementów
                # Zamiana miejscami, jeśli elementy są w złej kolejności
                lista_do_posortowania[j], lista_do_posortowania[j + 1] = lista_do_posortowania[j + 1], lista_do_posortowania[j]
                zmiana = True # Była zmiana
            if not zmiana: # Jeżeli nie ma zmiany (Celem optymalizacji kodu)
                break
    return lista_do_posortowania


posortowana_lista = bubble_sort(bombelek)
print("Po sortowaniu:", posortowana_lista)