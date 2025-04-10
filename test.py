from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    subject = Subject(name="Simon Otto", gender="male", birthdate="2003-05-15", weight=70, height=175, resting_hr=60)
    supervisor = Supervisor(name="Linus Maurer", gender="male", birthdate="1980-08-01", email="linus@maurer.com")

    experiment = Experiment(experiment_id="H1", date="2025-03-24", subject=subject, supervisor=supervisor)

    print("Maximale Herzfrequenz von", subject.name, "ist:", subject.estimate_max_hr())

    print("\nExperiment-Daten:")
    print(f"Experiment-ID: {experiment.experiment_id}")
    print(f"Datum des Experiments: {experiment.date}")
    print(f"Supervisor: {experiment.supervisor.name}")
    print(f"Subject: {experiment.subject.name}")




