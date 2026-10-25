# Pokémon Smeraldo - Sinnoh Expansion (Gen 4 Edition v1.0.0)

**Rom Hack Base:** `pokeemerald-expansion` (Commit `f594a462`)  
**Architettura & Supervisione:** Progetto interamente supervisionato e certificato da **Argon** (Gemini Web Pro / Medium Thinking) via `argon-bridge`.  
**Build Finale:** `pokeemerald.gba`  
**Dimensione Binario:** 33.554.432 bytes (32 MB)  
**SHA1 Hash:** `A2254A7306C2486D0B75539FEB2C6E0C75F05896`  
**Stato Certificazione:** `STATUS: APPROVED` (Tutte le 6 Fasi verificate con 0 issue critiche)

---

### Caratteristiche del Mod:
- **Zero Pokémon di 3ª Generazione:** Eliminati integralmente (#252 - #386) da tutti i percorsi, tabelle incontri, eventi, uova, fossili, scambi, roster allenatori, Parco Lotta, Gare e script.
- **Sostituzione 1:1 con 4ª Generazione:** Integrati tutti i 107 Pokémon di Sinnoh (#387 - #493).
- **Starter di Sinnoh:** Turtwig, Chimchar e Piplup con animazioni, backsprite, frontsprite e palette perfettamente registrate nella borsa del Prof. Birch.
- **Incontri Selvatici:** 6.459 slot selvatici bonificati su ogni mappa, erba, grotta, acqua, pesca, Safari Zone e alberi di miele.
- **Roster Allenatori:** 856 squadre di allenatori (Capipalestra, Superquattro, Campione, rivali Brendon/May/Wally, team Idro/Magma) completamente convertite a Gen 4 con mosse, abilità e strumenti coerenti.
- **Eventi Statici & Leggendari:**
  - Duo Lunare Simmetrico: Scelta TV Rosso -> Cresselia vagante / Darkrai a Isola Remota; Scelta TV Blu -> Darkrai vagante / Cresselia a Isola Remota (con supporto Soul Dew aggiornato).
  - Trinità dei Draghi: Giratina alla Torre dei Cieli, Dialga alla Grotta Terra, Palkia alla Grotta Marina.
  - Guardiani dei Laghi & Titani: Uxie, Azelf e Heatran nei tre templi dei Regi; Arceus all'Isola Materna.
  - Spiritomb (Devon Scope al Percorso 120), Rotom (Istituto Meteo), Riolu (regalo di Rocco a Verdeazzupoli), Happiny (uovo Cuordilava), Cranidos/Shieldon (Fossili Cranio e Armatura).
- **Parco Lotta & Gare:** 291 Pokémon del Battle Frontier, 123 dei Tendoni Lotta, 116 della Piramide Lotta, 99 dell'Apprendista, 62 della Collina Lotta e tutte le 7 squadre degli Assi del Parco (Argento e Oro) migrate a Gen 4. 52 avversari delle Gare Pokémon convertiti.
- **Sistemi di Gioco:** Comparse massicce TV, bonus Roulette Casinò, Quiz Lady, fratelli misuratori di Sootopolis (Cherubi e Buneary) e 135 vocaboli di chat aggiornati a Gen 4.

---

### Disclaimer Legale e Note sul Copyright (Intellectual Property)

Questo repository rispetta rigorosamente le norme sul diritto d'autore e le linee guida consolidate della community di decompilazione (*pret* e *rh-hideout*):

1. **Nessun file ROM proprietario distribuito:** Questo repository contiene **esclusivamente codice sorgente open-source, script e documentazione**. In piena conformità con le normative internazionali sul copyright (DMCA) e con i Termini di Servizio di GitHub, **non viene ospitato, linkato né distribuito alcun file binario commerciale protetto da copyright (`.gba`)**. Il file `.gitignore` del progetto esclude esplicitamente qualsiasi binario compilato.
2. **Proprietà Intellettuale & Marchi:** *Pokémon*, *Pokémon Smeraldo*, i nomi delle specie, dei personaggi e i relativi marchi sono di proprietà esclusiva di **Nintendo Co., Ltd.**, **Creatures Inc.** e **Game Freak Inc.** Questo progetto è una modifica amatoriale senza fini di lucro realizzata per scopi educativi, di ricerca informatica e di reverse engineering etico. Non è in alcun modo affiliato, sponsorizzato, approvato né supportato da Nintendo, Game Freak o The Pokémon Company.
3. **Distribuzione e Giocabilità Legale:** Gli utenti che desiderano provare la modifica possono:
   - Compilare autonomamente il codice sorgente con `make` (richiede MSYS2 con `arm-none-eabi-gcc`).
   - Generare o applicare una patch differenziale `.bps` (creabile tramite lo script incluso in `tools/create_bps_patch.py`) sulla propria copia personale e legalmente acquisita di *Pokémon Smeraldo (USA)* tramite tool gratuiti come [Rom Patcher JS](https://marcrobledo.com/RomPatcher.js/).

---

# About `pokeemerald-expansion`

![Gif that shows debugging functionality that is unique to pokeemerald-expansion such as rerolling Trainer ID, Cheat Start, PC from Debug Menu, Debug PC Fill, Pokémon Sprite Visualizer, Debug Warp to Map, and Battle Debug Menu](https://github.com/user-attachments/assets/cf9dfbee-4c6b-4bca-8e0a-07f116ef891c) ![Gif that shows overworld functionality that is unique to pokeemerald-expansion such as indoor running, BW2 style map popups, overworld followers, DNA Splicers, Gen 1 style fishing, OW Item descriptions, Quick Run from Battle, Use Last Ball, Wild Double Battles, and Catch from EXP](https://github.com/user-attachments/assets/383af243-0904-4d41-bced-721492fbc48e) ![Gif that shows off a number of modern Pokémon battle mechanics happening in the pokeemerald-expansion engine: 2 vs 1 battles, modern Pokémon, items, moves, abilities, fully customizable opponents and partners, Trainer Slides, and generational gimmicks](https://github.com/user-attachments/assets/50c576bc-415e-4d66-a38f-ad712f3316be)

<!-- If you want to re-record or change these gifs, here are some notes that I used: https://files.catbox.moe/05001g.md -->

**`pokeemerald-expansion`** is a GBA ROM hack base that equips developers with a comprehensive toolkit for creating Pokémon ROM hacks. **`pokeemerald-expansion`** is built on top of [pret's `pokeemerald`](https://github.com/pret/pokeemerald) decompilation project. **It is not a playable Pokémon game on its own.**

# [Features](FEATURES.md)

**`pokeemerald-expansion`** offers hundreds of features from various [core series Pokémon games](https://bulbapedia.bulbagarden.net/wiki/Core_series), along with popular quality-of-life enhancements designed to streamline development and improve the player experience. A full list of those features can be found in [`FEATURES.md`](FEATURES.md).

# [Credits](CREDITS.md)

 [![](https://img.shields.io/github/all-contributors/rh-hideout/pokeemerald-expansion/upcoming)](CREDITS.md)

If you use **`pokeemerald-expansion`**, please credit **RHH (Rom Hacking Hideout)**. Optionally, include the version number for clarity.

```
Based off RHH's pokeemerald-expansion 1.17.1 https://github.com/rh-hideout/pokeemerald-expansion/
```

Please consider [crediting all contributors](CREDITS.md) involved in the project!

# Choosing `pokeemerald` or **`pokeemerald-expansion`**

- **`pokeemerald-expansion`** supports multiplayer functionality with other games built on **`pokeemerald-expansion`**. It is not compatible with official Pokémon games.
- If compatibility with official games is important, use [`pokeemerald`](https://github.com/pret/pokeemerald). Otherwise, we recommend using **`pokeemerald-expansion`**.
- **`pokeemerald-expansion`** incorporates regular updates from `pokeemerald`, including bug fixes and documentation improvements.

# [Getting Started](INSTALL.md)

❗❗ **Important**: Do not use GitHub's "Download Zip" option as it will not include commit history. This is necessary if you want to update or merge other feature branches.

If you're new to git and GitHub, [Team Aqua's Asset Repo](https://github.com/Pawkkie/Team-Aquas-Asset-Repo/) has a [guide to forking and cloning the repository](https://github.com/Pawkkie/Team-Aquas-Asset-Repo/wiki/The-Basics-of-GitHub). Then you can follow one of the following guides:

## 📥 [Installing **`pokeemerald-expansion`**](INSTALL.md)
## 🏗️ [Building **`pokeemerald-expansion`**](INSTALL.md#Building-pokeemerald-expansion)
## 🚚 [Migrating from **`pokeemerald`**](INSTALL.md#Migrating-from-pokeemerald)
## 🚀 [Updating **`pokeemerald-expansion`**](INSTALL.md#Updating-pokeemerald-expansion)

# [Documentation](https://rh-hideout.github.io/pokeemerald-expansion/)

For detailed documentation, visit the [pokeemerald-expansion documentation page](https://rh-hideout.github.io/pokeemerald-expansion/).

# [Contributions](CONTRIBUTING.md)
If you are looking to [report a bug](CONTRIBUTING.md#Bug-Report), [open a pull request](CONTRIBUTING.md#Pull-Requests), or [request a feature](CONTRIBUTING.md#Feature-Request), our [`CONTRIBUTING.md`](CONTRIBUTING.md) has guides for each.

# [Community](https://discord.gg/6CzjAG6GZk)

[![](https://dcbadge.limes.pink/api/server/6CzjAG6GZk)](https://discord.gg/6CzjAG6GZk)

Our community uses the [ROM Hacking Hideout (RHH) Discord server](https://discord.gg/6CzjAG6GZk) to communicate and organize. Most of our discussions take place there, and we welcome anybody to join us!
