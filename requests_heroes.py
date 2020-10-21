import requests

heroes_dict = {}


class Hero:
    def __init__(self, name, TOKEN):
        self.name = name
        self.TOKEN = TOKEN

    def initialization(self):
        link = requests.get(
            f"https://superheroapi.com/api/{self.TOKEN}/search/{self.name}"
        )
        params = link.json()["results"][0]["powerstats"]["intelligence"]
        params = int(params)
        heroes_dict[self.name] = params
        return f"интеллект героя {self.name} составляет {params}"


Captain_America = Hero("Captain America", 2619421814940190)
Captain_America = Captain_America.initialization()
Thanos = Hero("Thanos", 2619421814940190)
Thanos = Thanos.initialization()
Hulk = Hero("Hulk", 2619421814940190)
Hulk = Hulk.initialization()

print(Captain_America)
print(Thanos)
print(Hulk)
inverse = [(value, key) for key, value in heroes_dict.items()]
print(f"самый умный герой среди них это:{max(inverse)[1]}")