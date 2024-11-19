emploees=[
    ("suma","accounts",200000),("sreehari","finance",100000),("sreya","cyber security",150000),
    ("jo","HR", 250000)
    ]
threshold=int(input("enter a threshold:"))
for employ in emploees:
    employ_name,department,monthly_salary=employ

    if monthly_salary> threshold:
        print(employ_name)
