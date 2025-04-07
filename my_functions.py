def estimate_max_hr(age_years: int, sex: str) -> int:
    """
    Schätzt die maximale Herzfrequenz basierend auf Alter und Geschlecht.
    Quelle: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/
    """
    if sex == "male":
        max_hr_bpm = 223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age_years
    else:
        # Falls das Geschlecht nicht bekannt ist, wird der Nutzer gefragt
        max_hr_bpm = input("Enter maximum heart rate:")
    
    return int(max_hr_bpm)


def build_person(first_name: str, last_name: str, sex: str, age: int) -> dict:
    """Erstellt ein Dictionary mit Informationen über eine Person."""
    person_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "estimate_max_hr": estimate_max_hr(age, sex)
    }
    return person_dict


def build_experiment(experiment_name: str, date: str, supervisor: dict, subject: dict) -> dict:
    """Erstellt ein Dictionary mit Informationen über ein Experiment."""
    experiment_dict = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject
    }
    return experiment_dict
