class Aqua:
    name = "Вода"

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm
        elif isinstance(other, Fire):
            return Steam
        elif isinstance(other, Terra):
            return Dirt
        return None


class Wind:
    name = "Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning
        elif isinstance(other, Terra):
            return Dust
        elif isinstance(other, Aqua):
            return Storm
        return None


class Fire:
    name = "Огонь"

    def __add__(self, other):
        if isinstance(other, Terra):
            return Lava
        elif isinstance(other, Aqua):
            return Steam
        elif isinstance(other, Wind):
            return Lightning
        return None


class Terra:
    name = "Земля"

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Dirt
        elif isinstance(other, Wind):
            return Dust
        elif isinstance(other, Fire):
            return Lava
        return None


class Storm:
    name = "Шторм"


class Steam:
    name = "Пар"


class Dirt:
    name = "Грязь"


class Lightning:
    name = "Молния"


class Dust:
    name = "Пыль"


class Lava:
    name = "Лава"


aqua = Aqua()
wind = Wind()
fire = Fire()
terra = Terra()

storm = aqua + wind
steam = aqua + fire
dirt = aqua + terra
lightning = wind + fire
dust = wind + terra
lava = fire + terra

print(f"{aqua.name} + {wind.name} = {storm.name}")
print(f"{aqua.name} + {fire.name} = {steam.name}")
print(f"{aqua.name} + {terra.name} = {dirt.name}")
print(f"{wind.name} + {fire.name} = {lightning.name}")
print(f"{wind.name} + {terra.name} = {dust.name}")
print(f"{fire.name} + {terra.name} = {lava.name}")

