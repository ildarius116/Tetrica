"""

"""
import csv
import requests

WIKI_API_URL = "https://ru.wikipedia.org/w/api.php"
CATEGORY_TITLE = "Категория:Животные по алфавиту"


def get_pages_from_category(category_title):
    session = requests.Session()
    session.headers.update({'User-Agent': 'MyBot/1.0'})
    pages = []
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": category_title,
        "cmlimit": "500",
        "format": "json"
    }

    while True:
        try:
            response = session.get(url=WIKI_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети: {e}")
            break
        except ValueError:
            print("Не удалось распарсить JSON.")
            print("Ответ сервера:", response.text[:200])
            break

        members = data.get("query", {}).get("categorymembers", [])
        pages.extend(members)

        if "continue" not in data:
            break
        params.update(data["continue"])

    return pages


def main():
    pages = get_pages_from_category(CATEGORY_TITLE)
    if not pages:
        print("Не удалось получить данные.")
        return

    letter_count = {}
    for page in pages:
        title = page["title"]
        first_char = title[0].upper()
        letter_count[first_char] = letter_count.get(first_char, 0) + 1
    sorted_letters = sorted(letter_count.items())

    with open("beasts.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sorted_letters)
    print(f"Файл beasts.csv успешно создан. Найдено записей: {len(pages)}")


if __name__ == "__main__":
    main()
