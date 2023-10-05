import requests

def get_superhero_data(name):
    url = f"https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    superheroes = response.json()
    
    for superhero in superheroes:
        if superhero['name'] == name:
            return superhero

    return None


superheroes = ['Hulk', 'Captain America', 'Thanos']

intelligence_scores = {}


for superhero in superheroes:
    data = get_superhero_data(superhero)
    if data:
        intelligence = data['powerstats']['intelligence']
        intelligence_scores[superhero] = intelligence


smartest_superhero = max(intelligence_scores, key=intelligence_scores.get)

print(f"Самый умный супергерой из {superheroes}: {smartest_superhero}")