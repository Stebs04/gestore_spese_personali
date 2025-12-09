# 💰 Gestore Spese Personali (Secure & Organized)

Un'applicazione CLI (Command Line Interface) scritta in Python per gestire le proprie spese quotidiane in modo sicuro e organizzato.
Il progetto si è evoluto alla **Versione 1.2**, introducendo crittografia delle password, recupero credenziali e una gestione avanzata dei file in sottocartelle.

## 🚀 Novità della Versione 1.2

* 🔒 **Sicurezza Avanzata:** Le password non vengono più salvate in chiaro, ma criptate usando l'algoritmo **SHA-256**.
* 📂 **File System Ordinato:** Il programma crea e gestisce automaticamente le sottocartelle:
    * `utenti/`: contiene il database crittografato degli utenti.
    * `spese/`: contiene i file JSON personali di ogni singolo utente.
* 🆘 **Recupero Password:** Hai dimenticato la password? Puoi reimpostarla usando il tuo **Token Segreto** salvato in fase di registrazione.
* 🏷️ **Categorie:** Selezione guidata della categoria di spesa (Cibo, Trasporti, Svago, ecc.).

## ✨ Funzionalità Principali

* **Login Multi-Utente:** Accesso separato per ogni persona.
* **Privacy Totale:** Ogni utente vede solo il proprio file delle spese.
* **Gestione Completa:** Aggiungi, visualizza, cerca ed elimina le spese.
* **Calcoli Automatici:** Ottieni il totale delle tue uscite in un istante.
* **Resilienza:** I dati vengono salvati automaticamente su disco.

## 🛠️ Requisiti

* Python 3.x installato.
* Librerie standard utilizzate: `json`, `re`, `os`, `hashlib`.

## ▶️ Come usare il programma

1.  Scarica la cartella del progetto.
2.  Apri il terminale nella cartella principale.
3.  Esegui il comando:
    ```bash
    python main.py
    ```
4.  **Al primo avvio:** Il programma creerà automaticamente le cartelle `spese` e `utenti`.
5.  Registrati inserendo Email, Password (min 8 caratteri) e un Token di recupero.
6.  Accedi e inizia a tracciare le tue spese!

    ## 📂 Struttura del Progetto
    
    ```text
    gestore_spese/
    │
    ├── main.py            # Entry point: Gestisce login e creazione cartelle
    ├── utenti.py          # Logica di autenticazione, hashing e recupero pwd
    ├── logica.py          # Funzioni core (CRUD spese e categorie)
    ├── gestione_files.py  # Driver per lettura/scrittura JSON
    │
    ├── utenti/            # Cartella database utenti
    │   └── utenti.json    # File con credenziali (Password hashate)
    │
    └── spese/             # Cartella database spese
        ├── nome_cognome.json
        └── altro_utente.json
## 🔮 Sviluppi Futuri
    
* [ ] Esportazione report in Excel/CSV.
* [ ] Grafici delle spese (es. torta per categorie).
* [ ] Budget mensile con avvisi di superamento soglia.
    
## ✍️ Autore
    
**Stefano Bellan**
