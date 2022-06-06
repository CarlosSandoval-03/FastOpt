if (
	localStorage.getItem("turno") === null ||
	localStorage.getItem("turno") === undefined
) {
	localStorage.setItem("turno", 0);
}

const generarTurno = () => {
	const mailValue = document.getElementById("mailInput");

	if (mailValue.value === "" || mailValue.value.search("@") == -1) {
		alert("REGISTRE UN CORREO VALIDO");
	} else {
		let value = localStorage.getItem("turno");

		value = parseInt(value, 10) + 1;
		localStorage.setItem("turno", value);
		if (confirm(`El turno generado es ${value}`)) {
			window.history.back();
		}
	}
};
