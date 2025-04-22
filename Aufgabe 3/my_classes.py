from datetime import datetime
import requests 

BASE_URL = "http://127.0.0.1:5000" 

class Person:
    def __init__(self, name, gender, birthdate):
        self.name = name
        self.gender = gender
        self.__birthdate = birthdate

    def calculate_age(self):
        today = datetime.today()
        birth = datetime.strptime(self.__birthdate, "%Y-%m-%d")
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def put(self):
        """Legt diese Person per POST /person auf dem Server an."""
        url = f"{BASE_URL}/person"
        data = {
            "name": self.name,
            "gender": self.gender,
            "birthdate": self._Person__birthdate
        }
        resp = requests.post(url, json=data)
        print(f"PUT  {resp.status_code} – {resp.text}")

class Subject(Person):
    def __init__(self, name, gender, birthdate, weight=None, height=None, resting_hr=None, email=None):
        super().__init__(name, gender, birthdate)
        self.weight = weight
        self.height = height
        self.resting_hr = resting_hr
        self.email = email 

    def estimate_max_hr(self):
        return 220 - self.calculate_age()

    def update_email(self):
        """Updated die Email dieser Person per PUT /person/{name}."""
        if not self.email:
            print("Keine E-Mail gesetzt.")
            return
        url = f"{BASE_URL}/person/{self.name}"
        data = {"email": self.email}
        resp = requests.put(url, json=data)
        print(f"UPDATE  {resp.status_code} – {resp.text}")

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
