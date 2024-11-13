import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.hp =None
        self.power=None
        self.super_power=None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['forms'][0]['name']  # Bir Pokémon'un adını döndürme
                else:
                    return "pokeball"  # İstek başarısız olursa varsayılan adı döndürür
    
    
    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][0]['base_stats']  # Bir Pokémon'un adını döndürme
                else:
                    return 1 # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_power(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][1]['base_stats']  # Bir Pokémon'un adını döndürme
                else:
                    return 0  # İstek başarısız olursa varsayılan adı döndürür   
                
    async def get_super_power(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][3]['base_stats']  # Bir Pokémon'un adını döndürme
                else:
                    return 0  # İstek başarısız olursa varsayılan adı döndürür   
    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
        
        if not self.hp:
            self.name = await self.get_hp()  # Henüz yüklenmemişse bir adın geri alınması
        

        if not self.power:
            self.name = await self.get_power()  # Henüz yüklenmemişse bir adın geri alınması
        return f"Pokémonunuzun ismi: {self.name} \n Pokémonunuzun sağlığı: {self.hp} \n  Pokémonunuzun gücü: {self.power} "


    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data["sprites"]["other"]["official-artwork"]["front_default"]
                else:
                    return None

    async def attack(self, enemy):
        if isinstance(enemy ,Wizard):
            change = random.randint(1,5)
            if change <3:
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı .\n@{enemy.pokemon_trainer}kalkan kullandı.\n@{enemy.pokemon_trainer}'nin sağlık durumu{enemy.hp}"
        else:
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu{enemy.hp}"
            else:
                enemy.hp = 0
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi!"

                

class Wizard(Pokemon) :
    async def attack(self, enemy):
        return await super().attack(enemy)
    

class Fighter(Pokemon) :
    async def attack(self, enemy):
        super_power = await super().get_super_attack()
        self.güç += super_power
        sonuc = await super().attack(enemy)  
        self.güç -= super_power
        return sonuc + f"\nDövüşçü Pokémon süper saldırı kullandı. Eklenen güç: {super_power}"

if __name__ =="__main__":
    wizard=Wizard("username1")
    fighter=Fighter("username2")
    print(wizard.info)
    print()
    print(fighter.info)
    print()
    print(fighter.attack(wizard))

