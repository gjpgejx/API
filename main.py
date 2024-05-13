import requests


def fetch_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    if response.status_code == 200:
        fact_data = response.json()
        if 'fact' in fact_data:
            return fact_data['fact']
        else:
            return "Failed to retrieve cat fact"
    else:
        return "Failed to get data. Status code: " + str(response.status_code)


while True:
    user_input = input("Введите 'факт' чтобы получить случайный факт о кошках или 'выход' чтобы завершить программу: ")

    if user_input.lower() == 'факт':
        fact = fetch_cat_fact()
        print("Случайный факт о кошках: ", fact)
    elif user_input.lower() == 'выход':
        print("Программа завершена.")
        break
    else:
        print("Неизвестная команда. Пожалуйста, введите 'факт' или 'выход'.")
