
from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Jetzt auch "resting_hr" und andere Attribute übergeben
    subject = Subject(subject_id="S1", gender="male", age=21, resting_hr=60, name="Simon Otto", weight=70, height=175)
    supervisor = Supervisor(name="Linus Maurer", email="linus@maurer.com")

    experiment = Experiment(experiment_id="H1", date="2025-03-24", supervisor=supervisor, subject=subject)

    print("Maximale Herzfrequenz von", subject.name, "ist:", subject.estimate_max_hr())

    print("\nExperiment-Daten:")
    print(f"Experiment-ID: {experiment.experiment_id}")
    print(f"Datum des Experiments: {experiment.date}")
    print(f"Supervisor: {experiment.supervisor.name}")
    print(f"Subject: {experiment.subject.name}")



