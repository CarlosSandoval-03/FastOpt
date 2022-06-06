const dobContainer = document.getElementById("dobContainer");

const today = new Date(Date.now());

let inputDob = document.createElement("input");
inputDob.type = "date";
inputDob.classList.add("form-control");
inputDob.id = "dobPaciente";
inputDob.required = true;

if (today.getDate() != 1) {
	today.setDate(today.getDate() - 1);
}

let minDate = new Date(today.getFullYear() - 150, 01, 01);

/** REFERENCE: https://stackoverflow.com/questions/23593052/format-javascript-date-as-yyyy-mm-dd */
let maxValue = today.toISOString().split("T")[0];
let minValue = minDate.toISOString().split("T")[0];

inputDob.value = maxValue;
inputDob.max = maxValue;
inputDob.min = minValue;

dobContainer.appendChild(inputDob);

const generarPaciente = () => {
	const apellidoForm = document.getElementById("apellidoPaciente");
	const nombreForm = document.getElementById("nombrePaciente");
	const dobForm = document.getElementById("dobPaciente");
	const nacForm = document.getElementById("nacPaciente");
	const numIdForm = document.getElementById("numIdPaciente");
	const mailForm = document.getElementById("mailPaciente");
	const telefonoForm = document.getElementById("telefonoPaciente");

	const newPatient = {
		nombre: nombreForm.value,
		apellido: apellidoForm.value,
		fechaNacimiento: dobForm.value,
		nacionalidad: nacForm.value,
		numDocumento: numIdForm.value,
		mail: mailForm.value,
		telefono: telefonoForm.value,
		foto: undefined,
	};

	let directorioPactientes = JSON.parse(localStorage.getItem("pacientes"));

	let id = 0;
	for (let i in directorioPactientes) {
		id++;
	}

	directorioPactientes[id] = newPatient;

	localStorage.setItem("pacientes", JSON.stringify(directorioPactientes));

	window.history.back();
};
