# Zalando Scraper 👟 

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

# Automatisierung unter Linux
Ein cronjob automatisiert das Skript unter Linux. Das chron_main.sh lässt sich ausfühbar machen:

```
chmod +x chron_main.sh
```

Danach vergewissern, dass pyvirtualdesktop installiert ist und folgenden Code in main.py auskommentieren:

```
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024,768))

# Das virtuelle Display öffnen
display.start()

# Am Ende des Skripts das virtuelle Display schließen
display.stop()
```

Danach stellen Sie die Automatisierung ein:
```
crontab -e
```

Um es jede Minte auszführen zu lassen:
```
* * * * * /bin/bash /home/szo/zalando-scraper/cron_main.sh 
```

Stand: Mai 2025
