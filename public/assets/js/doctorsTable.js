function createActions() {
	let tdActtions = document.createElement("td");
	tdActtions.classList.add("text-center");
	tdActtions.classList.add("align-middle");

	tdActtions.style.maxHeight = "60px";
	tdActtions.style.height = "60px";

	// ACTION 1
	let action1 = document.createElement("a");
	action1.classList.add("btn");
	action1.classList.add("btnMaterial");
	action1.classList.add("btn-flat");
	action1.classList.add("primary");
	action1.classList.add("semicircle");
	action1.role = "button";

	action1.href = "#";

	let icon1 = document.createElement("i");
	icon1.classList.add("far");
	icon1.classList.add("fa-eye");

	action1.appendChild(icon1);

	// ACTION 2
	let action2 = document.createElement("a");
	action2.classList.add("btn");
	action2.classList.add("btnMaterial");
	action2.classList.add("btn-flat");
	action2.classList.add("success");
	action2.classList.add("semicircle");
	action2.role = "button";

	action2.href = "#";

	let icon2 = document.createElement("i");
	icon2.classList.add("fas");
	icon2.classList.add("fa-pen");

	action2.appendChild(icon2);

	// ACTION 3
	let action3 = document.createElement("a");
	action3.classList.add("btn");
	action3.classList.add("btnMaterial");
	action3.classList.add("btn-flat");
	action3.classList.add("accent");
	action3.classList.add("btnNoBorders");
	action3.classList.add("checkboxHover");
	action3.style.marginLeft = "5px";
	action3.role = "button";

	action3.href = "#";

	let icon3 = document.createElement("i");
	icon3.classList.add("fas");
	icon3.classList.add("fa-trash");
	icon3.classList.add("btnNoBorders");
	icon3.style.color = "#dc3545";

	action3.appendChild(icon3);

	// SAVE ALL
	tdActtions.appendChild(action1);
	tdActtions.appendChild(action2);
	tdActtions.appendChild(action3);

	return tdActtions;
}

const tabla = document.getElementById("cuerpoTablaDoctores");

let doctor = listaDoctores.head;
let i = 0;

while (doctor !== null) {
	let tr = document.createElement("tr");
	let tdID = document.createElement("td");
	let tdFirstName = document.createElement("td");
	let tdLastName = document.createElement("td");
	let tdSpecialty = document.createElement("td");
	let tdEmail = document.createElement("td");
	let tdState = document.createElement("td");
	let tdActtions = createActions();

	tdID.innerHTML = i;
	tdFirstName.innerHTML = doctor.data.nombre;
	tdLastName.innerHTML = doctor.data.apellido;
	tdSpecialty.innerHTML = doctor.data.especialidad;
	tdState.innerHTML = "Activo";
	tdEmail.innerHTML = doctor.data.mail;

	tr.appendChild(tdID);
	tr.appendChild(tdFirstName);
	tr.appendChild(tdLastName);
	tr.appendChild(tdSpecialty);
	tr.appendChild(tdEmail);
	tr.appendChild(tdState);
	tr.appendChild(tdActtions);

	tabla.appendChild(tr);

	doctor = doctor.next;
	i++;
}
