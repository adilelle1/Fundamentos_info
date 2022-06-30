class Vehicle:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self) -> str:
        return super().__str__()

    def print_info(self):
        print(f"Vehicle's name: {self.name}"
              f"Vehicle's year: {self.year}")

    def move_forward(self):
        print(f"La/el {self.name} está avanzando...")


class Auto(Vehicle):
    def __init__(self, name, year, model, engine, wheels, doors, fuel_tank):
        super().__init__(name, year)
        self.model = model
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
        self.fuel_tank = fuel_tank

    def refueling(self):
        refuel = int(input("How many ounces of fuel: "))
        self.fuel_tank += refuel
        print(f"Your tank has now: {self.fuel_tank}")

    def flat_tire(self):
        self.wheels -= 1

    def fix_flat_tire(self):
        if self.wheels == 4:
            print("All of your tires are ok, you don't need to fix them")
        else:
            self.wheels +=1
            print(f"Your {self.name} now has {self.wheels} tires working")

    def move_forward(self):
        if self.fuel_tank < 3:
            print("It's not possible to move forward, your tank does not have enough fuel")
        elif self.fuel_tank == 3:
            if self.wheels < 4:
                print("It's not possible to move forward, al least one of your tires is flat")
            else:
                self.fuel_tank -= 3
                print(f"WARNING you are running out of gas: {self.fuel_tank}")
        else:
            if self.wheels < 4:
                print("It's not possible to move forward, al least one of your tires is flat")
            else:
                self.fuel_tank -= 3
                print("Your are moving now")


class Moto(Vehicle):
    def __init__(self, name, year, model, engine, wheels, fuel_tank):
        super().__init__(name, year)
        self.model = model
        self.engine = engine
        self.wheels = wheels
        self.fuel_tank = fuel_tank

    def refueling(self):
        refuel = int(input("How many ounces of fuel:"))
        self.fuel_tank += refuel
        print(f"Your tank has now: {self.fuel_tank}")

    def flat_tire(self):
        self.wheels -= 1

    def fix_flat_tire(self):
        if self.wheels == 2:
            print("All of your tires are ok, you don't need to fix them")
        else:
            self.wheels +=1
            print(f"Your {self.name} now has {self.wheels} tires working")

    def move_forward(self):
        if self.fuel_tank < 3:
            print("It's not possible to move forward, your tank does not have enough fuel")
        elif self.fuel_tank == 3:
            if self.wheels < 2:
                print("It's not possible to move forward, al least one of your tires is flat")
            else:
                self.fuel_tank -= 3
                print(f"WARNING you are running out of gas: {self.fuel_tank}")
        else:
            if self.wheels < 2:
                print("It's not possible to move forward, al least one of your tires is flat")
            else:
                self.fuel_tank -= 3
                print("Your are moving now")


class Velero(Vehicle):
    def __init__(self, name, year, foot, mainmast, engine, fuel_tank):
        super().__init__(name, year)
        self.foot = foot
        self.mainmast = mainmast
        self.engine = engine
        self.fuel_tank = fuel_tank

    def refueling(self):
        refuel = int(input("How many ounces of fuel:"))
        self.fuel_tank += refuel
        print(f"Your tank has now: {self.fuel_tank}")


class Bicicleta(Vehicle):
    def __init__(self, name, year, type, changes, wheels):
        super().__init__(name, year)
        self.type = type
        self.changes = changes
        self.wheels = wheels

    def flat_tire(self):
        self.wheels -= 1

    def fix_flat_tire(self):
        if self.wheels == 2:
            print("All of your tires are ok, you don't need to fix them")
        else:
            self.wheels +=1
            print(f"Your {self.name} now has {self.wheels} tires working")

    def move_forward(self):
        if self.wheels < 2:
            print("It's not possible to move forward, al least one of your tires is flat")
        else:
            print("Your are moving now")
