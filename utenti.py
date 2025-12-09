import json
import re
import gestione_files
import os

FILE_UTENTI = os.path.join("utenti", "utenti.json")

def _carica_utenti():
    try:
        with open(FILE_UTENTI, "r") as f:
            dati_caricati = json.load(f)
            return dati_caricati
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _salva_utenti(lista_utenti):
    with open(FILE_UTENTI, "w") as f:
        json.dump(lista_utenti, f, indent=4)

def registra_utente():
    # 1. CARICHIAMO il database esistente
    database_utenti = _carica_utenti()
    
    email = input("Inserisci una email (sarà il tuo username): ")
    
    # 2. CONTROLLO: Se l'email esiste già, fermiamoci subito
    if email in database_utenti:
        print("Errore: Questa email è già registrata.")
        return False

    anagrafica = input("Inserisci nome e cognome: ")
    
    # Ciclo per la password sicura
    while True:
        pwd = input("Inserisci una password (min 8 caratteri): ")
        if len(pwd) < 8:
            print("Password troppo corta! Riprova.")
        else:
            break 
    
    token = input("Inserisci token per recupero password: ")
    
    # 3. CREIAMO IL PROFILO
    nuovo_profilo = {
        "anagrafica": anagrafica,
        "pwd": pwd,
        "token": token
    }
    
    # 4. AGGIUNGIAMO AL DATABASE con la chiave Email
    database_utenti[email] = nuovo_profilo
    
    # 5. SALVIAMO SU FILE UTENTI
    _salva_utenti(database_utenti)
    
    print("Registrazione avvenuta con successo!")

    # 6. CREIAMO IL FILE SPESE PERSONALE (Vuoto)
    # Qui usiamo re.sub ma SENZA cartelle, file salvato nella root
    nome_base = re.sub(r'[@.]', '_', email) + ".json"
    percorso_spese = os.path.join("spese", nome_base)
    gestione_files.salva_dati([], percorso_spese)

    return email

def login_utente():
    database_utenti = _carica_utenti()
    
    email_l = input("Inserisci email: ")
    pwd_l = input("Inserisci password: ")
    
    if email_l in database_utenti:
        profilo_utente = database_utenti[email_l]
        
        if pwd_l == profilo_utente['pwd']:
            print(f"Benvenuto {profilo_utente['anagrafica']}!")
            return email_l 
        else:
            print("Password errata.")
            return None
    else:
        print("Utente non trovato.")
        return None