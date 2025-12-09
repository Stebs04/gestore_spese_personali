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
    
def recupera_password():
    database_utenti = _carica_utenti()
    
    print("\n--- Recupero Password ---")
    email = input("Inserisci la tua email di registrazione: ")
    
    # 1. Controlliamo se la mail esiste
    if email in database_utenti:
        profilo = database_utenti[email]
        
        # 2. Chiediamo il token segreto
        token_input = input("Inserisci il tuo token segreto: ")
        
        # 3. Controlliamo se il token corrisponde a quello salvato
        if token_input == profilo['token']:
            print("Token corretto! Puoi reimpostare la password.")
            
            # 4. Facciamo inserire la nuova password (stesso ciclo di controllo della registrazione)
            while True:
                nuova_pwd = input("Inserisci la nuova password (min 8 caratteri): ")
                if len(nuova_pwd) < 8:
                    print("Password troppo corta! Riprova.")
                else:
                    break
            
            # 5. Aggiorniamo la password nel dizionario e salviamo
            profilo['pwd'] = nuova_pwd
            database_utenti[email] = profilo # Aggiorniamo il profilo dell'utente
            _salva_utenti(database_utenti)
            
            print("Password aggiornata con successo! Ora puoi accedere.")
            return True
            
        else:
            print("Token errato! Impossibile recuperare la password.")
            return False
    else:
        print("Email non trovata nel sistema.")
        return False