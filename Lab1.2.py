class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def introduce(self):
        print(f"Мене звати {self.name}, мені {self.__age} років.")

    def work(self):
        print("Людина працює.")


class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def work(self):
        print("Студент навчається.")

    def study(self):
        print(f"{self.name} навчається в {self.university}.")