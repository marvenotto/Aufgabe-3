
class Subject:
    def __init__(self, subject_id, gender, age, resting_hr):
        self.subject_id = subject_id
        self.gender = gender
        self.age = age
        self.resting_hr = resting_hr

    def estimate_max_hr(self):
        return 220 - self.age

class Supervisor:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Experiment:
    def __init__(self, experiment_id, date, subject, supervisor):
        self.experiment_id = experiment_id
        self.date = date
        self.subject = subject
        self.supervisor = supervisor