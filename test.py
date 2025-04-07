from my_classes import Subject, Supervisor, Experiment

subject1 = Subject("S01", "m", 25, 60)

supervisor1 = Supervisor("Dr. Müller", "mueller@example.com")

experiment1 = Experiment("EXP001", "2025-04-07", subject1, supervisor1)

print(f"Subject ID: {subject1.subject_id}")
print(f"Geschätzte maximale Herzfrequenz: {subject1.estimate_max_hr()}")
print(f"Supervisor: {experiment1.supervisor.name}")
