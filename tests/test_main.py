import allure
import requests
import random

def attach_log(name, content):
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )

num = random.randint(1, 1300)
api = "https://pokeapi.co/api/v2/pokemon/"+ str(num)
@allure.feature("PokeAPI")
def test_pokemon_type_validation():
    with allure.step("Get Random Pokemon"):
        response = requests.get(api)
        data = response.json()
    
    with allure.step("Verify Pokemon is Electric type"):
        types = [t['type']['name'] for t in data['types']]
        assert "electric" in types, f"Expected 'electric' in {types}"
    
    with allure.step("Whats the Pokemon"):
        attach_log(data['name'],"Pokemon")
        assert data['name'] == "pikachu"