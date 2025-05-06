# Zalando Scraper 👟 
Dank geht an ola@heise.de für die modulare Aufteilung des Codes in Funktionen und der Korrektur.

# Installation
Python venv aufsetzen und Skript starten.
```
pipenv install
```

Das Skript benötigt eine .env-Datei, die so strukturiert ist:
```
passwort="doan beispiel axi etwa"
absender="hommingbergergepardenforelle@gmail.com"
empfaenger="donald@entenhausen.de"
smtp_port=465
smtp_server="smtp.gmail.com"
```
In config.py geben Sie die Variablen Ihres gewünschten Schuhs an.
Standardgemäß ist das der Asics Japan S black.

Das Skript setzt auf Chrome. Es startet nach:
```
pipenv run python main.py
```
Stand: Mai 2025
