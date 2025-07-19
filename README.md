# 🦖 Pygame Dino Runner

Un clone personalizzato del classico *Chrome Dino Runner*, sviluppato con **Python** e **Pygame**. Include salti, ostacoli, livelli progressivi, animazioni e suoni. Il gioco si resetta cliccando su un pulsante dopo il Game Over.

---

## 🎮 Caratteristiche principali

- Controllo semplice con **barra spaziatrice** per saltare
- **Cactus** che appaiono casualmente
- **Livelli crescenti** di difficoltà (velocità e frequenza spawn)
- **Animazione** del personaggio in corsa
- **Effetti sonori** per salto, collisione e passaggio livello
- **Game Over** con possibilità di **ricominciare**
- **Debug mode** per mostrare le hitbox

---

## 🧱 Struttura del progetto

```
dino_runner/
├── main.py             # Codice principale
├── assets.py           # Immagini e suoni
├── config.py           # Costanti e setup Pygame
├── levels.py           # Dati livelli
├── README.md
└── assets/
    ├── terreno.png
    ├── nuvola.png
    ├── game over.png
    ├── ricomincia.png
    ├── cactus/
    │   └── cactus 1.png
    ├── sprite/
    │   ├── sprite 1.png
    │   ├── sprite 2.png
    │   ├── sprite 3.png
    │   └── sprite 4.png
    └── sound/
        ├── sfx_jump.mp3
        ├── hit.mp3
        └── score-reached.mp3
```

---

## ⚙️ Requisiti

- Python 3.8 o superiore
- [Pygame](https://www.pygame.org/)

Installa le dipendenze con:

```bash
pip install pygame
```

---

## ▶️ Come avviare il gioco

Esegui:

```bash
python main.py
```

### Comandi

- **Barra spaziatrice** → salta
- **Click del mouse** → ricomincia dopo il Game Over

---

## 📁 Descrizione dei file

### `main.py`

Contiene il **ciclo principale** del gioco:

- Gestione degli eventi
- Salto e gravità
- Movimento del terreno
- Gestione ostacoli
- Collisioni e Game Over
- Punteggio e passaggio di livello

### `assets.py`

Carica **immagini e suoni**:

```python
background = pygame.image.load("...")
suono_salto()  # Effetti sonori
```

### `config.py`

Contiene le **costanti** e l’**inizializzazione Pygame**:

- Dimensioni schermo
- FPS
- Colori
- Font
- `screen` e `clock`

### `levels.py`

Contiene i **dati dei livelli** in una lista di dizionari:

```python
livelli = [
    {"soglia": 100, "velocità": 7, "spawn_min": 90, "spawn_max": 220},
    {"soglia": 300, "velocità": 8, "spawn_min": 80, "spawn_max": 210},
    ...
]
```

---

## 🐞 Debug Mode

Attiva la modalità debug nel file `main.py`:

```python
debugging = True
```

Mostrerà le **hitbox** e informazioni di spawn/speed nella console.

---

## 📄 Licenza

Distribuito sotto la licenza **MIT**. Puoi usarlo, modificarlo e condividerlo liberamente.

---

## 👨‍💻 Autore

Sviluppato con 💻 e 🎮 usando **Python** + **Pygame**
