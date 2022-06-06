const generarDoctor = () => {
	const apellidoForm = document.getElementById("apellidoDoctor");
	const nombreForm = document.getElementById("nombreDoctor");
	const especialidadForm = document.getElementById("especialidadDoctor");
	const emailForm = document.getElementById("mailDoctor");

	const newDoctor = {
		nombre: nombreForm.value,
		apellido: apellidoForm.value,
		especialidad: especialidadForm.value,
		mail: emailForm.value,
	};

	let directorioDoctores = JSON.parse(localStorage.getItem("doctores"));

	let id = 0;
	for (let i in directorioDoctores) {
		id++;
	}

	directorioDoctores[id] = newDoctor;

	localStorage.setItem("doctores", JSON.stringify(directorioDoctores));

	window.history.back();
};
