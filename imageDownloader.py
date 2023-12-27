import requests

def download_image(pokemon_number):
    url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_number}.png'
    response = requests.get(url)

    if response.status_code == 200:
        with open(f'C:\\DEV\MEUS_PROJETOS\\pokenext\\public\\images\\pokemons\\{pokemon_number}.png', 'wb') as file:
            file.write(response.content)
        print(f'Imagem {pokemon_number}.png baixada com sucesso.')
    else:
        print(f'Erro ao baixar a imagem {pokemon_number}.')

# Exemplo: Baixar a imagem do Pokémon número 10
for pokemon_number in range(1, 252):
    download_image(pokemon_number)
