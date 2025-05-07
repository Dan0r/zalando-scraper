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

# Automatisierung unter Linux
Ein cronjob automatisiert das Skript unter Linux. Sie erstellen ein
Shellskript namens cron_main.sh. Das lässt sich im Terminal
ausführbar machen mit chmod +x cron_main.sh. Weil ein cronjob in einer minimalen Anwendungsumgebung läuft, kann es das GUI von Chrome nicht öffnen. Das lässt sich mit der Bibliothek pythonvirtualdisplay lösen, die das GUI simuliert. Sie installieren diese mit pipenv install pyvirtualdisplay, und in main.py kommentieren Sie folgenden Code aus:


```
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024,768))

# Das virtuelle Display öffnen
display.start()

# Am Ende des Skripts das virtuelle Display schließen
display.stop()
```

Danach stellen Sie die Automatisierung ein: crontab -e. Um es jede Minte auszuführen:

```
* * * * * /bin/bash /home/szo/zalando-scraper/cron_main.sh 
```

Stand: Mai 2025
