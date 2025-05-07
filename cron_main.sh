#!/bin/bash

# Wählt den Bildschirm aus
export DISPLAY=:0

# Statt szo Ihren Nuterznamen angeben
cd /home/szo/zalando-scraper
pipenv run python3 main.py

# 0. Nicht vergessen in main.py den Code für die Eintellung des cronjob auszukommentieren.
# 1. cronjob ausführbar machen im Terminal:
# chmod +x cron_main.sh
# 2. cronjob aktivieren:
# crontab -e
# 3. nach unten scrollen und cronjob einstellen, etwa für jede Minute:
# * * * * * /bin/bash /home/szo/zalando-scraper/cron_main.sh
