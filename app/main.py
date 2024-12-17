class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None :
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{Name: " + f"{self.name}, Health: " \
            + f"{self.health}, Hidden: " + str(self.hidden) + "}"


class Herbivore(Animal):
    def hide(self) -> None :
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Herbivore) -> None :
        if isinstance(animal, Carnivore):
            return
        if animal.hidden:
            return

        animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
