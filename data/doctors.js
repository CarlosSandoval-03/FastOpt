let listaDoctores = new LinkedStack();

if (
	localStorage.getItem("doctores") === null ||
	localStorage.getItem("doctores") === undefined
) {
	localStorage.setItem("doctores", JSON.stringify(doctorsData));
}

let data = JSON.parse(localStorage.getItem("doctores"));

for (let i in data) {
	listaDoctores.push(data[i]);
}
