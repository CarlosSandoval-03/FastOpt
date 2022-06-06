let listaPacientes = new LinkedStack();

if (
	localStorage.getItem("pacientes") === null ||
	localStorage.getItem("pacientes") === undefined
) {
	localStorage.setItem("pacientes", JSON.stringify(patientsData));
}

let data = JSON.parse(localStorage.getItem("pacientes"));

for (let i in data) {
	listaPacientes.push(data[i]);
}
