function send_filejs() {
	var file = document.getElementById("file_content").value
	eel.create_file(file);
        //document.location.href = "chose_template.html";
        //window.location = "chose_template.html";
        //location.replace("https://www.w3schools.com")
}

function title_() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "\n#";
}

function subtitle() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "\n##";
}

function subsubtitle() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "\n###";
}

function add_image() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "![tag image](path image)"
}

function add_table() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "|   |   |   |   |   |\n |---|---|---|---|---|\n |   |   |   |   |   |\n |   |   |   |   |   |\n |   |   |   |   |   |"
}

function new_line() {
	var text = document.getElementById("file_content").value;
	document.getElementById("file_content").value = text + "\n \\newline \n";
}

function add_indice() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "\n \\tableofcontents";
}

function add_header() {
	var text = document.getElementById("file_content").value
	document.getElementById("file_content").value = text + "---\n title: \"\"\n author: [Author Name]\n date: \"\"\n subject: \"Markdown\"\n keywords: [Markdown, Example]\n subtitle: \"\"\n lang: \"en\"\n titlepage: true\n titlepage-color: \"06386e\"\n titlepage-text-color: \"FFFFFF\"\n titlepage-rule-color: \"FFFFFF\"\n titlepage-rule-height: 1\n ...\n";
}

