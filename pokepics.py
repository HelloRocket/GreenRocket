from pokebase import pokemon
from requests import get
from PIL import Image
from io import BytesIO

def fetch():
    name = input('Which Pokemon do you want to fetch? ')
    poke = pokemon(name)
    pic = get(poke.sprites.front_default).content
    image = Image.open(BytesIO(pic))
    image.save(f'{poke}.gif')

fetch()

