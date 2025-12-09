# 💰 Gestore Spese Personali (Multi-Utente)

Un'applicazione CLI (Command Line Interface) scritta in Python per gestire le proprie spese quotidiane.
Partito come un semplice esercizio di logica, il progetto si è evoluto nella **Versione 1.1** diventando un gestionale **multi-utente** con sistema di autenticazione e salvataggio dati separato.

## 🚀 Novità della Versione 1.1

* 🔐 **Sistema di Login e Registrazione:** Accesso sicuro tramite email e password.
* 👥 **Supporto Multi-Utente:** Più persone possono usare il programma sullo stesso PC; ognuno vedrà *solo* le proprie spese.
* 💾 **Database Dinamici:** Il programma genera automaticamente un file JSON separato per ogni utente registrato (es. `nome_cognome.json`).
* 🛡️ **Controlli di Sicurezza:** Validazione della lunghezza password in fase di registrazione.

## ✨ Funzionalità Principali

* **Aggiungi Spesa:** Inserisci importo, descrizione e data.
* **Visualizza Spese:** Guarda il tuo estratto conto personale.
* **Calcola Totale:** Somma automatica di tutte le tue spese.
* **Ricerca Avanzata:** Trova le spese effettuate in una data specifica.
* **Elimina Spesa:** Rimuovi una voce errata o non necessaria.
* **Persistenza Dati:** Tutto viene salvato automaticamente su file JSON.

## 🛠️ Requisiti

* Python 3.x installato.
* Nessuna libreria esterna richiesta (usa solo librerie standard: `json`, `re`).

## ▶️ Come usare il programma

1.  Scarica la cartella del progetto.
2.  Apri il terminale nella cartella.
3.  Esegui il comando:
    ```bash
    python main.py
    ```
4.  **Al primo avvio:** Scegli l'opzione **2) Registrati** per creare il tuo utente.
5.  Effettua il **Login** con le credenziali appena create.
6.  Gestisci le tue spese dal menu principale!

## 📂 Struttura del Progetto

* `main.py`: Il punto di ingresso. Gestisce il flusso Login -> Menu Spese.
* `utenti.py`: Gestisce la logica di registrazione, login e sicurezza credenziali.
* `logica.py`: Contiene le funzioni "core" (creazione, calcoli, ricerca spese).
* `gestione_files.py`: Modulo flessibile per leggere/scrivere su diversi file JSON.
* `utenti.json`: Database crittografato (in futuro) contenente le credenziali degli utenti.
* `*_*.json`: File generati automaticamente che contengono le spese dei singoli utenti.

## 🔮 Sviluppi Futuri

* [ ] Aggiunta di Categorie per le spese (Cibo, Trasporti, Svago).
* [ ] Hashing della password (per non salvarla in chiaro nel JSON).
* [ ] Esportazione in CSV/Excel.
* [ ] Funzione "Recupera Password" tramite Token.

## ✍️ Autore

**Stefano Bellan** - Progetto Portfolio Python