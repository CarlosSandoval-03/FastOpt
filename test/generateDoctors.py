import json

from faker import Faker
from faker.providers import DynamicProvider

especialidades = []
with open("test/especialidades.txt", "r") as file:
    for line in file:
        especialidades.append(line.strip())
    file.close()
1
medical_professions_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=especialidades,
)

fake = Faker()
fake.add_provider(medical_professions_provider)


doctors = {}

with open("data/randomUserData.json", "r") as file:
    data = json.load(file)

    results = data["results"]

    for i in range(2500, 2550):
        current = results[i]

        doctors[str(i-2500)] = {
            "nombre": current["name"]["first"],
            "apellido": current["name"]["last"],
            "especialidad": fake.medical_profession(),
            "mail": current["email"],
            "foto": current["picture"]["large"],
        }
    file.close()

with open("data/doctors.json", "w") as file:
    json.dump(doctors, file, indent=4)
    file.close()
