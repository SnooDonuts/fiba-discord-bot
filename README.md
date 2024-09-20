# FIBA Discord Bot

Tento Discord bot je navržen pro správu uživatelských zůstatků a hazardní hry jako ruleta.

## Funkce

- **Správa zůstatků**: Sledování a aktualizace uživatelských zůstatků.
- **Hazardní příkazy**: Podpora sázek a hazardních her.
- **Reset účtu**: Možnost resetování zůstatku.

## Příkazy

- `/balance`: Zkontroluje zůstatek uživatele.
- `/maty`: Uzavře výchozí sázku 10$.
- `/ruleta`: Zahraje hru ruleta.

## Instalace

1. Klonujte repozitář:
   ```bash
   git clone https://github.com/SnooDonuts/fiba-discord-bot.git
   ```
2. Vytvořte a aktivujte virtuální prostředí:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows použijte: venv\Scripts\activate
   ```
3. Nainstalujte závislosti:
   ```bash
   pip install -r requirements.txt
   ```
4. Spusťte bota:
   ```bash
   python main.py
   ```

## Požadavky

- Python 3.12
- Discord.py
- SQLite

## Licence

Projekt je licencován pod MIT licencí.
