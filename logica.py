import gestione_files
import re
import os

#Creo la funzione per aggiungere una spesa
def crea_spesa():
    spesa = {}
    importo = float(input("Inserisci l'importo della spesa: "))
    while True: 
        categoria = input("Seleziona tra le categorie presenti\n1)Casa e bollette\n2)Trasporti\n3)Alimentari\n" \
        "4)Svago e ristoranti\n5)Salute\n6)Shopping\n7)Altro\nScrivi la categoria: ")
        if categoria in ["1", "2", "3", "4", "5", "6", "7"]:
            spesa["categoria"] = categoria
            break
        else:
            print("Categoria non valida riprova da capo!!!!")
    descrizione = input("Inserisci una descrizione della spesa o la tipologia: ")
    data = input("Inserisci la data in cui è stata fatta\n (Usa questo formato GG/MM/YY): ")
    spesa["importo"] = importo
    spesa["descrizione"] = descrizione
    spesa["data"] = data
    return spesa


#Creo una funzione per formattare in maniera pulita la stampa delle spese
def stampa_spesa(lista_spese):
    #Controllo che la lista non sia vuota
    if not lista_spese:
        print("Non ci sono spese registrate!!!\n")
    else:
        for spesa in lista_spese:
            print(f"{spesa['data']} -> {spesa['categoria']} -> {spesa['descrizione']}: {spesa['importo']}€")
            print("-------------------")

#Funzione che calcola la somma di tutte le spese inserite nel file JSON
def calcola_totale(lista_spese):
    somma = 0
    for spesa in lista_spese:
        somma += spesa['importo']
    return somma 

def elimina_spesa(lista_spese):
    user_input = input("Inserisci la descrizione della spesa da eliminare: ")
    
    # Scorriamo la lista
    for spesa in lista_spese:
        # Guardiamo se la descrizione di QUESTA spesa corrisponde all'input
        if spesa['descrizione'] == user_input:
            # Trovata! La rimuoviamo dalla lista
            lista_spese.remove(spesa)
            print("Spesa eliminata con successo!")
            return lista_spese
            
    # Se il ciclo finisce senza aver trovato nulla (senza aver fatto return)
    print("Descrizione non trovata.")
    return lista_spese
        
            
def ricerca_spesa(lista_spese):
    trovato = False
    user_input = input("Inserisci la data da cercare: ")
    for spesa in lista_spese:
        if spesa['data'] == user_input:
            #Spesa trovata la stampo
            print(f"{spesa['data']} -> {spesa['descrizione']}: {spesa['importo']}€")
            print("-------------------")
            trovato = True
        elif not trovato:
            print("Nessuna spesa trovata con questa data")

def crea_spesa_gui(importo, categoria, descrizione, data, nome_utente):
    spesa = {}
    spesa["importo"] = importo
    spesa["categoria"] = categoria
    spesa["descrizione"] = descrizione
    spesa["data"] = data
    nome_base = re.sub(r'[@.]', '_', nome_utente) + ".json"
    percorso_spese = os.path.join("spese", nome_base)
    lista_spese = gestione_files.carica_dati(percorso_spese)
    if isinstance(lista_spese, dict):
        if lista_spese:
            lista_spese = [lista_spese]
        else:
            lista_spese = []
    elif not isinstance(lista_spese, list):
        lista_spese=[]
    lista_spese.append(spesa)
    gestione_files.salva_dati(lista_spese, percorso_spese)
    return True