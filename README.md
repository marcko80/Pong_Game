# Pong Game in Pygame

Questo progetto è una versione del classico gioco Pong, realizzato utilizzando la libreria Pygame. Il gioco include funzionalità per il punteggio, il movimento delle racchette e della palla, e un processo di onboarding per chiedere i nomi dei giocatori. 

## Caratteristiche

- **Onboarding dei Giocatori**: All'avvio del gioco, viene richiesto ai due giocatori di inserire i propri nomi. Il giocatore 1 gioca a sinistra e il giocatore 2 gioca a destra.
- **Movimento delle Racchette**: Le racchette possono essere controllate usando i tasti `W` e `S` per il giocatore di sinistra e i tasti freccia su e giù per il giocatore di destra.
- **Movimento della Palla**: La palla rimbalza sulle racchette e sui bordi superiori e inferiori dello schermo.
- **Punteggio**: Il punteggio aumenta solo per il giocatore che riesce a colpire la palla con la sua racchetta. Il punteggio viene visualizzato in alto nello schermo di gioco.
- **Effetti Sonori**: Quando la palla colpisce una racchetta o un bordo, viene riprodotto un suono.

## Requisiti

- Python 3.x
- Pygame

## Installazione

1. Clona questo repository:
    ```bash
    git clone https://github.com/tuo-username/pong-game.git
    cd pong-game
    ```

2. Installa Pygame:
    ```bash
    pip install pygame
    ```

3. Assicurati di avere il file audio `ping_pong_8bit_plop.ogg` nella stessa directory dello script. Se non hai questo file, puoi scaricarne uno simile o modificarne il nome nel codice.

## Esecuzione

Esegui lo script Python per avviare il gioco:
```bash
python pong_game.py
```

## Struttura del Codice

- **onboarding()**: Chiede i nomi dei giocatori tramite input da tastiera.
- **disegna_oggetti()**: Disegna le racchette, la palla e il punteggio sullo schermo.
- Ciclo principale del gioco: Gestisce gli eventi di input, il movimento delle racchette e della palla, le collisioni e l'aggiornamento dello schermo.

## Contribuzione

Sono benvenuti i contributi per migliorare il gioco! Sentiti libero di fare un fork del progetto, apportare modifiche e creare una pull request.

---

Spero che questo progetto ti piaccia e che ti diverta a giocare a Pong con Pygame!

## Licenza

Questo progetto è concesso in licenza sotto i termini della licenza MIT.

---

Se hai domande o suggerimenti, non esitare a contattarmi.

Buon divertimento!

---
