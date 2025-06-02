import requests
from bs4 import BeautifulSoup
from typing import List


def scrape_practices(city: str) -> List[str]:
    """Beispiel-Funktion, die nach Praxen in einer Stadt sucht.

    Dies ist nur ein Platzhalter, da die tatsaechlichen Webseiten
    moeglicherweise unterschiedlich aufgebaut sind. In einer realen
    Anwendung muesste der HTML-Aufbau analysiert werden.
    """
    url = f"https://www.beispiel-arztsuche.de/{city}?fachgebiet=nuklearmedizin"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    practices = []
    for item in soup.select(".praxis-item"):
        name = item.select_one(".praxis-name").get_text(strip=True)
        address = item.select_one(".praxis-adresse").get_text(strip=True)
        practices.append(f"{name} - {address}")
    return practices


def search_appointments(practice_url: str) -> List[str]:
    """Sucht nach freien Terminen auf der Praxis-Webseite.

    Auch dies ist nur ein Beispiel. Viele Praxen bieten Online-
    Terminsysteme an, die ueber iframes oder externe Anbieter
    eingebunden sein koennen.
    """
    response = requests.get(practice_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    appointments = []
    for slot in soup.select(".free-appointment"):
        appointments.append(slot.get_text(strip=True))
    return appointments


if __name__ == "__main__":
    cities = ["berlin", "brandenburg"]
    all_practices = []
    for city in cities:
        try:
            practices = scrape_practices(city)
            all_practices.extend(practices)
        except Exception as e:
            print(f"Fehler beim Abrufen der Praxen in {city}: {e}")

    for practice in all_practices:
        print(practice)
        # Hier koennte man den Link zur Praxis-Webseite ermitteln
        # und mit search_appointments nach freien Terminen suchen

