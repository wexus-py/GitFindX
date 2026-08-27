import requests
ключ = input("Ключевые слова: ")
формула = {
    "q": ключ,
    "sort": "stars",
    "order": "desc" 
}   
api = "https://api.github.com/search/repositories"
try: 
    запрос = requests.get(api, params=формула)
    if запрос.status_code == 200:
        data = запрос.json()
        print(f"\n Найдено: {data['total_count']} репозиториев\n")
        print("-------------------------------------\n")
        for repo in data["items"][:5]:
            print(f" {repo['name']}\n\n")
            print(f"ссылка = {repo['html_url']}\n\n")
            print(f"кол-во звезд = {repo['stargazers_count']}\n\n")
            print(f"описание = {repo['description'] or 'Нет описания'}\n")
            print("-------------------------------------\n")
    else:
        print("Ошибка:", запрос.status_code)
except Exception as e:
    print(f"Плохое соединение: {e}")
