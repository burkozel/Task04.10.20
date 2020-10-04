class geese:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_eggs(self, eggs):
        eggs = eggs + 1
        return f"Гуси отложили {eggs} яиц."

    def give_food(self, food):
        food = food + 1
        return f"Мы дали им {food} килограмм."

class cow:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_milk(self, milk):
        milk = milk + 1
        return f"Корова дала {milk} литров молока."

    def give_food(self, food):
        food = food + 1
        return f"Мы дали ей {food} килограмм."


class sheep:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_wool(self, wool):
        wool = wool + 1
        return f"Овцы дали {wool} шерсти."

    def give_food(self, food):
        food = food + 1
        return f"Мы дали им {food} килограмм."


class goat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_milk(self, milk):
        milk = milk + 1
        return f"Козы дали {milk} литров молока."

    def give_food(self, food):
        food = food + 1
        return f"Мы дали им {food} килограмм."


class duck:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_eggs(self, eggs):
        eggs = eggs + 1
        return f"Утки отложили {eggs} яиц."

    def give_food(self, food):
        food = food + 1
        return f"Мы дали им {food} килограмм."


class chicken:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_eggs(self, eggs):
        eggs = eggs + 1
        return f"Курицы отложили {eggs} яиц."

    def give_food(self, food):
        food = food + 1
        return f"Мы дали им {food} килограмм."

def get_weight():
    s = 0
    for classes in farm:
        s += classes.weight
    print(s)

def get_heaviest():
    max_ = 0
    a = ''
    for animals in farm:
        if animals.weight > max_:
            max_ = animals.weight
            a = animals.name
    print(a)


def get_all():
    for animals in farm:
        print(f"{animals.name} весит {animals.weight} кг")

def commands():
    while True:
        command = input("Введите команду ")
        if command == "w":
            get_weight()
        if command == "m":
            get_heaviest()
        if command == "a":
            get_all()

farm = []
def get_farm():
    farm.append(geese("Белый", 5))
    farm.append(geese("Серый", 6))
    farm.append(cow("Манька", 300))
    farm.append(sheep("Барашек", 78))
    farm.append(sheep("Кудрявый", 90))
    farm.append(chicken("Ко-ко", 3))
    farm.append(chicken("Кукареку", 1))
    farm.append(goat("Рога", 70))
    farm.append(goat("Копыта", 58))
    farm.append(duck("Кряква", 2))

get_farm()
commands()

