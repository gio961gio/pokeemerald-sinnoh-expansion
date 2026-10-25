# Pokémon Smeraldo - Edizione Sinnoh (Gen 4 Porting)
## Release v1.0.0-sinnoh-gold

Questa release trasforma integralmente **Pokémon Smeraldo** (`pokeemerald-expansion`) rimuovendo il 100% delle specie di Terza Generazione e implementando al loro posto l'intero ecosistema della Quarta Generazione (Sinnoh Platinum Regional Pokédex), sotto la supervisione tecnica formale di **Argon** (`STATUS: APPROVED`).

---

### Caratteristiche Principali

#### 1. Pokédex Regionale di Sinnoh
- **107 Pokémon di Quarta Generazione attivi** (`P_GEN_4_POKEMON = TRUE`).
- **0 Pokémon di Terza Generazione attivi** (`P_GEN_3_POKEMON = FALSE`).
- Ibridi cross-gen (Gallade, Roserade, Budew, Probopass, Dusknoir, Chingling, Froslass) pienamente operativi con apprendimento mosse ed evoluzioni preservate, mentre i membri originali di Hoenn sono disabilitati a livello di preprocessore C.
- Pokédex regionale riorganizzato secondo l'ordinamento ufficiale del Pokédex di Sinnoh Platino (183 specie totali).

#### 2. Starter & Scelte Iniziali
- Starter di Hoenn sostituiti con gli starter di Sinnoh nella borsa del Prof. Birch:
  - **Turtwig** (Erba)
  - **Chimchar** (Fuoco)
  - **Piplup** (Acqua)
- Squadre del Rivale (Brendan / May) e di Wally allineate in tutte le 38 varianti narrative del gioco.

#### 3. Incontri Selvatici nei Biomi di Hoenn
- Riconfigurati 6.459 slot in `wild_encounters.json`:
  - **Zone marine e costiere:** Shellos Mare Ovest (Route 103-109) e Shellos Mare Est (Route 118-129), Finneon, Lumineon, Buizel, Floatzel.
  - **Foreste e percorsi alberati:** Burmy, Wormadam, Mothim, Kricketot, Kricketune, Cherubi, Combee, Pachirisu, Starly.
  - **Montagne e grotte:** Shinx, Luxio, Cranidos, Shieldon, Gible, Gabite, Bronzor, Bronzong, Riolu, Lucario, Hippopotas.
  - **Zone lacustri e acquitrini:** Bidoof, Bibarel, Croagunk, Toxicroak, Shellos, Gastrodon.
  - **Alberi da miele & Safari:** Munchlax, Carnivine, Skorupi, Drapion.
  - **Pokémon Vaganti (Roamers):** Mesprit e Cresselia pattugliano le mappe di Hoenn dopo la Lega.

#### 4. Squadre degli Allenatori & Capipalestra
- 856 allenatori e 1.864 Pokémon riscritti in `trainers.party`:
  - **Petra (Roccia):** Geodude, Shieldon, Cranidos (Ace).
  - **Fiammetta (Fuoco):** Magcargo, Houndoom, Monferno, Magmortar.
  - **Norman (Normale):** Bibarel, Ambipom, Lopunny, Snorlax.
  - **Rocco Petri (Campione / Partner):** Bronzong e Lucario (Lotta in doppio contro il Team Magma).
  - **Superquattro & Campione:** Ribilanciati con team tematici competitivi di Sinnoh.

#### 5. Eventi Statici, Scambi & Leggendari
- **Casa di Rocco (Mossdeep):** Pokédono sul tavolo con Riolu Lv 5 e lettera personalizzata di Rocco.
- **Istituto Meteo (Route 119):** Dono statico Rotom Lv 25 (con Acqua Magica).
- **Terme di Lavaridge:** Uovo consegnato dall'anziana contenente Happiny (Pietraovale).
- **Kecleon invisibili (Devon Scope):** Sostituiti da Spiritomb Lv 30.
- **Fossili Devon Corp:** Fossilcranio -> Cranidos Lv 20; Fossilarmatura -> Shieldon Lv 20.
- **Puzzle Braille (Sala Incisa):** Lumineon al primo posto del party e Finneon all'ultimo posto per aprire le porte dei Regi.
- **Leggendari di Copertina:**
  - *Grotta Marina:* Palkia Lv 70 (con sprite mappa dedicato).
  - *Grotta Terra:* Dialga Lv 70 (con sprite mappa dedicato).
  - *Torre dei Cieli:* Giratina Lv 70 (con sprite mappa dedicato).
  - *Trio dei Regi:* Uxie (Desert Ruins), Heatran (Island Cave), Azelf (Ancient Tomb).
  - *Isola Remota:* Darkrai (Isola Sud Latios) e Cresselia (Isola Sud Latias).
  - *Isola Materna:* Arceus Lv 80 (invece di Deoxys).

---

### Specifiche Tecniche del Binario

- **File ROM:** `pokeemerald.gba`
- **Dimensione:** 33.554.432 byte (32.0 MB esatti)
- **Exit Code Compilazione:** 0 (Clean build)
- **Allocazione ROM:** 25.293.380 bytes / 32 MB (75.38% utilizzato, 6.7 MB di headroom)
- **Allocazione EWRAM:** 226.416 bytes / 256 KB (86.37%)
- **Allocazione IWRAM:** 28.376 bytes / 32 KB (86.60%)
- **Compatibilità:** 100% compatibile con emulatore mGBA, VBA-M, RetroArch (mGBA core) e flashcart hardware per Game Boy Advance (EZ-Flash Omega, EverDrive-GBA X5).
