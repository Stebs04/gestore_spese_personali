import logica
import gestione_files
spese = gestione_files.carica_dati()

while True:
    print("\n--Gestore Spese V1.0--")
    print("1) Aggiungi spesa")
    print("2) Visualizza spese")
    print("3) Calcolo il totale delle spese")
    print("4) Elimina una spesa")
    print("5) Cerca una spesa")
    print("6) Esci")
    user_input = input("Fai la tua scelta: ")

    if user_input == '1':
        print("Hai scelto di aggiungere una spesa!!!\n")
        nuova_spesa = logica.crea_spesa()
        spese.append(nuova_spesa)
        gestione_files.salva_dati(spese)
        print("Spesa aggiunta e salvata")
    elif user_input == '2':
        print("Hai scelto di visualizzare tutte le tue spese!!\n")
        print("Ecco la lista delle tue spese\n")
        logica.stampa_spesa(spese)
    elif user_input == '3':
        print("Calcolo della somma totale di tutte le spese in corso...\n")
        totale = logica.calcola_totale(spese)
        print(f"Il totale calcolato e': {totale}")
    elif user_input == '4':
        logica.elimina_spesa(spese)#Chiamo la funzione per eliminare la spesa
        gestione_files.salva_dati(spese) #Aggiorno la lista anche nel file
    elif user_input == '5':
        logica.ricerca_spesa(spese)#Chiamo la funzione per eliminare la spesa
    elif user_input == '6':
        gestione_files.salva_dati(spese)
        print("Arrivederci")
        break

    else:
        print("Scelta non valida riprova tra le condizioni valide!!!\n")
  