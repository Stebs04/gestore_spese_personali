import logica
import gestione_files
import utenti
import re 
import os 

#--- FASE 0: SETUP INIZIALE ---
if not os.path.exists("spese"):
    os.makedirs("spese")
if not os.path.exists("utenti"):
    os.makedirs("utenti")
    
# Variabile per ricordarci chi è loggato
utente_corrente_email = None

# --- FASE 1: LOOP DI LOGIN ---
while True:
    print("\n--- BENVENUTO ---")
    print("1) Accedi")
    print("2) Registrati")
    print("3) Esci")
    scelta = input("Scelta: ")

    if scelta == "1":
        utente_corrente_email = utenti.login_utente()
        if utente_corrente_email: 
            break 
            
    elif scelta == "2":
        nuovo_utente = utenti.registra_utente()
        if nuovo_utente: 
            utente_corrente_email = nuovo_utente
            break
        else:
            print("Registrazione non andata a buon fine. Riprova.")
        
    elif scelta == "3":
        print("Uscita in corso...")
        exit() 
    
    else:
        print("Scelta non valida!")

# --- FASE 2: PREPARAZIONE DATI (CORREZIONE QUI!) ---
# 1. Ricostruiamo il nome del file grezzo
nome_file_grezzo = re.sub(r'[@.]', '_', utente_corrente_email) + ".json"

# 2. Costruiamo il percorso COMPLETO: cartella "spese" + nome file
# Questo era il pezzo mancante!
nome_file_spese = os.path.join("spese", nome_file_grezzo)

# 3. Carichiamo le spese
spese = gestione_files.carica_dati(nome_file_spese)

# --- FASE 3: GESTORE SPESE ---
# (Il resto del codice va bene, usa già la variabile nome_file_spese che abbiamo corretto sopra)
while True:
    print(f"\n--Gestore Spese di {utente_corrente_email}--")
    # ... resto del tuo codice ...
    # Ricorda solo di assicurarti che le chiamate a salva_dati usino nome_file_spese
    # Esempio: gestione_files.salva_dati(spese, nome_file_spese)
    
    # ... copia pure il resto del tuo while loop precedente ...
    # Ti rimetto qui solo l'inizio per chiarezza
    print("1) Aggiungi spesa")
    print("2) Visualizza spese")
    print("3) Calcolo totale spese")
    print("4) Elimina una spesa")
    print("5) Cerca una spesa")
    print("6) Esci e Salva")
    
    user_input = input("Fai la tua scelta: ")
    
    try: 
        if user_input == '1':
            print("Hai scelto di aggiungere una spesa!!!\n")
            # Nota: Ho visto che hai aggiornato logica.py con le categorie, ottimo!
            nuova_spesa = logica.crea_spesa()
            spese.append(nuova_spesa)
            gestione_files.salva_dati(spese, nome_file_spese)
            print("Spesa aggiunta e salvata")
            
        elif user_input == '2':
            print("\nEcco la lista delle tue spese:")
            logica.stampa_spesa(spese)
            
        elif user_input == '3':
            print("Calcolo in corso...")
            totale = logica.calcola_totale(spese)
            print(f"Il totale calcolato è: {totale}€")
            
        elif user_input == '4':
            logica.elimina_spesa(spese)
            gestione_files.salva_dati(spese, nome_file_spese)
            
        elif user_input == '5':
            logica.ricerca_spesa(spese)
            
        elif user_input == '6':
            gestione_files.salva_dati(spese, nome_file_spese)
            print("Dati salvati. Arrivederci!")
            break

        else:
            print("Scelta non valida, riprova!")
            
    except Exception as e:
        print(f"Si è verificato un errore: {e}")