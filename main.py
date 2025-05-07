#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config import product, product_name, size, my_limit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import ssl

# Cronjob: Zusätzliche Bibliothek, um das Skript ohne GUI auszuführen
# from pyvirtualdisplay import Display



# Funktionen 
def open_website(url: str):
    print(f"Öffnen der Webseite {url}")
    try:
        driver.get(url)
    except Exception as e:
        print(f"Fehler beim Öffnen: {e}")
        close_driver()
        raise


def close_driver():
    print("Beenden des Browser-Treibers ...")
    driver.quit()


def accept_cookies():
    try:
        print("Auf das Cookie-Banner warten ...")
        # Das Cookie-Banner ist ein Shadow-DOM-Element mit der ID "usercentrics-root"
        host = WebDriverWait(driver, 10).until(
            presence_of_element_located((By.ID, "usercentrics-root"))
        )

        print(
            "Prüfen, ob der Einwilligungsknopf vorhanden und anklickbar ist ..."
        )

        # Diese Funktion ist eine sogenannte "Erwartung" (Expectation) für Selenium.
        # Sie prüft, ob der Button im Shadow DOM vorhanden und anklickbar ist.
        # WebDriverWait.until() verwendet sie, um sicherzustellen, dass der Button
        # vorhanden ist, bevor darauf geklickt wird.
        def consent_button_clickable(_driver):
                element = host.shadow_root.find_element(By.CSS_SELECTOR, "[data-testid='uc-accept-all-button']")
                return (
                    element
                    if element.is_displayed() and element.is_enabled()
                    else False
                )

        consent_button = WebDriverWait(driver, 10).until(consent_button_clickable)
        consent_button.click()
    except Exception as e:
        print(f"Fehler beim Annehmen der Cookies: {e}")

def search_product(product_name: str):
    try:
        print("Auf das Suchfeld warten ...")
        search_box = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.ID, "header-search-input"))
        )
        search_box.click()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Fehler beim Suchen nach dem Produkt: {e}")


def select_product(product_name: str):
    try:
        print("Auf die Produktversion warten ...")
        product_element = WebDriverWait(driver, 10).until(
            presence_of_element_located((By.XPATH, f"//h3[text()='{product_name}']"))
        )
        product_element.click()
    except Exception as e:
        print(f"Error selecting product: {e}")


def select_product_size(size: str | int) -> bool:
    try:
        size_menu = WebDriverWait(driver, 10).until(
            presence_of_element_located((By.ID, "picker-trigger"))
        )
        size_menu.click()
        size_element = WebDriverWait(driver, 10).until(
            presence_of_element_located((By.XPATH, f"//span[text()='{size}']"))
        )
        size_element.click()
        print(f"Produktgröße '{size}' erfolgreich ausgewählt.")
        print("Auf Element für die Verfügbarkeit warten ...")
        ancestor = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, f"//span[text()='{size}']/ancestor::div[@data-is-selected]"))
        )
        return ancestor.get_attribute("data-is-selected") == "true"
    except Exception as e:
        print(f"Fehler beim Auswählen der Produktgröße: {e}")
    return False


def get_price() -> float | None:
    try:
        print("Produktpreis ermitteln ...")
        price_element = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.CSS_SELECTOR, "[data-testid='pdp-price-container'] span"))
        )
        price = price_element.text
        # Euro-Zeichen entfernen und Komma in Punkt umwandeln,
        # um den Preis in einen Float konvertieren zu können
        price = float(price.replace("€", "").replace(",", ".").strip())
        print(f"Preis: {price} €")
        return price
    except Exception as e:
        print(f"Fehler beim Ermitteln des Preises: {e}")
        return None


def send_email(subject: str, body: str) -> None:
    sender = os.getenv("absender")
    recipient = os.getenv("empfaenger")
    password = os.getenv("passwort")
    smtp_server = os.getenv("smtp_server")
    smtp_port = os.getenv("smtp_port")
    if not all([sender, recipient, password, smtp_server, smtp_port]):
        print("E-Mail-Konfiguration nicht vollständig.")
        return
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender, password)
            msg = EmailMessage()
            msg.set_content(body)
            msg["Subject"] = subject
            msg["From"] = sender
            msg["To"] = recipient
            server.send_message(msg)
            print(f"E-Mail erfolgreich an {recipient} gesendet.")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")


# Die .env-Datei laden, die die E-Mail-Konfiguration und die Suchparameter für den gewünschten Schuh enthält
load_dotenv()

# Cronjob Zusatz
# display = Display(visible=0, size=(1024,768))
# display.start()

# URL zu Zalando festlegen
url = "https://www.zalando.de/"

# Selenium-WebDriver initialisieren
options = Options()
## Setup chrome options für WSL2
homedir = os.path.expanduser("~/programming/squishyscraper")
options.binary_location = f"{homedir}/chrome-linux64/chrome"
webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")


# Wir wollen die Webseite mit deutscher Sprache öffnen.

# Das Überschreiben der Spracheinstellungen per Kommandozeilenargument
# funktioniert leider nicht zuverlässig, schadet aber auch nicht.
options.add_argument("--lang=de")
options.add_argument("--accept-languages=de")
# Den größten Erfolg verheißt, die Einstellungen des Browsers zu ändern,
# entweder auf "de" oder auf "de_DE".
options.add_experimental_option("prefs", {"intl.accept_languages": "de,de_DE"})

driver = webdriver.Chrome(options=options)

# Webdriver ausführen
# Die folgenden Variablen sind in der .config-Datei gespeichert
open_website(url)
accept_cookies()
search_product(product)
select_product(product_name)
available = select_product_size(size)
if not available:
    print(f"Produktgröße '{size}' ist nicht verfügbar.")
else:
    price = get_price()
    if price is not None:
        price_formatted = f"{price:.2f}".replace(".", ",")
        my_limit_formatted = f"{my_limit:.2f}".replace(".", ",")
        if price < my_limit:
            print(
                f"Preis {price} liegt unter dem Limit {my_limit_formatted} €. E-Mail wird gesendet ..."
            )
            send_email(
                f"Preisalarm für {product}",
                f"Der Preise für {product_name} in Größe {size} ist nun {price_formatted} € "
                f"und liegt damit unter deinem Limit von {my_limit_formatted} €.\n\n"
                f"Hier klicken, um zu shoppen: {driver.current_url}",
            )
        else:
            print(
                f"{price_formatted} € liegt über dem Limit {my_limit_formatted} €. Keine Mail verschickt."
            )
    else:
        print("Produktpreis konnte nicht ermittelt werden.")
close_driver()
# Cronjob Zusatz:
#display.stop()
