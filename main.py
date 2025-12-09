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

# --- FASE 2: PREPARAZIONE DATI ---
# Ricostruiamo il nome del file (senza cartelle)
nome_file_spese = re.sub(r'[@.]', '_', utente_corrente_email) + ".json"

# Carichiamo le spese
spese = gestione_files.carica_dati(nome_file_spese)

# --- FASE 3: GESTORE SPESE ---
while True:
    print(f"\n--Gestore Spese di {utente_corrente_email}--")
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