# Zalando Scraper 👟 
Dank geht an ola@heise.de für die modulare Aufteilung des Codes in Funktionen und der Korrektur.

# Installation
Python venv aufsetzen:
```
python -m venv env

source env/bin/activate

pipenv install -r requirements.txt
```

Chrome installieren. Danach die .env-Datei aufsetzen. Einen Gmail-Account erstellen und dessen Daten in die .env setzen:
```
passwort="doan beispiel axi etwa"
absender="hommingbergergepardenforelle@gmail.com"
empfaenger="donald@entenhausen.de"
smtp_port=465
smtp_server="smtp.gmail.com"
```

Das Skript abspielen:
```
python main.py

```
Stand: Mai 2025
