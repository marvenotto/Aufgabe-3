from my_functions import build_person, build_experiment

if __name__ == "__main__":
    supervisor = build_person("Linus", "Maurer", "male", 45)

    subject = build_person("Simon", "Otto", "male", 21)

    experiment = build_experiment("Herzfrequenz-Test", "2025-03-24", supervisor, subject)

    print("Experiment-Daten:")
    print(experiment)

