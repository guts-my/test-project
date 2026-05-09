import allure
import requests

def attach_log(name, content):
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )

# https://pokeapi.co/api/v2/pokemon/pikachu
@allure.feature("PokeAPI")
def test_pokemon_type_validation():
    with allure.step("Get Pikachu data"):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
        data = response.json()
    
    with allure.step("Verify Pikachu is Electric type"):
        types = [t['type']['name'] for t in data['types']]
        assert "electric" in types, f"Expected 'electric' in {types}"
    
    with allure.step("Verify name is pikachu"):
        assert data['name'] == "pikachu"