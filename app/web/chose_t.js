
function set_template_default() {
        template.innerText = "Default";
        eel.set_template("Default");
}

function set_template_stylepdf() {
        template.innerText = "Stylized PDF";
        eel.set_template("Stylized_PDF");
}

function set_template_pp() {
        template.innerText = "Power Point PDF";
        eel.set_template("Power_Point_PDF");
}

function set_template_latex() {
        template.innerText = "LaTex";
        eel.set_template("LaTex");
}

function set_template() {
	var text = document.getElementById("template").value
	document.getElementById("template").value = "Default";
}
