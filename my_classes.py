from datetime import datetime

class Person:
    def __init__(self, name, gender, birthdate):
        self.name = name
        self.gender = gender
        self.__birthdate = birthdate  # privates Attribut

    def calculate_age(self):
        today = datetime.today()
        birth = datetime.strptime(self.__birthdate, "%Y-%m-%d")
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


class Subject(Person):
    def __init__(self, name, gender, birthdate, weight=None, height=None, resting_hr=None):
        super().__init__(name, gender, birthdate)
        self.weight = weight
        self.height = height
        self.resting_hr = resting_hr

    def estimate_max_hr(self):
        return 220 - self.calculate_age()


class Supervisor(Person):
    def __init__(self, name, gender, birthdate, email):
        super().__init__(name, gender, birthdate)
        self.email = email


class Experiment:
    def __init__(self, experiment_id, date, subject, supervisor):
        self.experiment_id = experiment_id
        self.date = date
        self.subject = subject
        self.supervisor = supervisor



        