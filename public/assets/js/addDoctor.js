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

	let keys = Object.keys(directorioDoctores);
	let id = keys[keys.length - 1] + 1;

	directorioDoctores[id] = newDoctor;

	localStorage.setItem("doctores", JSON.stringify(directorioDoctores));

	window.history.back();
};
