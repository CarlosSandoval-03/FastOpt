import json

pacientes = {}

with open("data/randomUserData.json", "r") as file:
    data = json.load(file)

    results = data["results"]

    for i in range(50):
        current = results[i]

        pacientes[str(i)] = {
            "nombre": current["name"]["first"],
            "apellido": current["name"]["last"],
            "fechaNacimiento": current["dob"]["date"],
            "nacionalidad": current["nat"],
            "numDocumento": current["id"]["value"],
            "mail": current["email"],
            "telefono": current["phone"],
            "foto": current["picture"]["large"],
        }
    file.close()

with open("data/patients.json", "w") as file:
    json.dump(pacientes, file, indent=4)
    file.close()
