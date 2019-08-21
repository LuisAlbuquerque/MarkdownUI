import io
from base64 import b64encode
import eel
import os


eel.init('web')

TEMPLATE = ""

TEMPLATES = [ "Default",
              "Stylized_PDF",
              "Power_Point_PDF",
              "LaTex"]

STATE = "init"
STATES = [  "init",
            "zathura_run",
         ]

@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def set_template(template):
    TEMPLATE = template
    print(TEMPLATE)
    with open("template","w+") as fd:
        fd.write(template)

    #eel.start('input_text.html', size=(1000, 600))

def relaod_zathura(name_file):
    output = os.popen("ps -a | grep 'zathura'").read()
    print(output)
    if(output != ""):
        pid = output.split()[0] 
        os.system("kill "+ pid)
    os.system("zathura "+ name_file + "pdf")

@eel.expose
def create_file(file_content):
    print(file_content)
    name_file = "newfile." 
    with open("web/markdowns/" + name_file + "md","w+") as fd:
        fd.write(file_content)

    with open("template","r") as fd:
        TEMPLATE = fd.read()

    print(" TEMPLATE :: "+ TEMPLATE)
    """ DEFAULT """
    if (TEMPLATE == TEMPLATES[0]):
        print("DEFAULT")
        os.system("pandoc web/markdowns/" + name_file + "md -o web/pdfs/" + name_file + "pdf")

    # TODO
    """ Stylized PDF"""
    if (TEMPLATE == TEMPLATES[1]):
        print("Stylized PDF")
        #os.system("pandoc -t html5 --css mdstyle.css web/markdowns/" + name_file + "md -o web/pdfs/" + name_file + "pdf")
        os.system("pandoc web/markdowns/"+name_file + "md -o web/pdfs/" + name_file + "pdf --from markdown --template eisvogel.tex --listings")

    # TODO
    """ Power Point PDF"""
    if (TEMPLATE == TEMPLATES[2]):
        print("PP PDF")
        #os.system("pandoc web/markdowns/" + name_file + "md -o web/pdfs/" + name_file + "pdf")
        #os.system("pandoc -t beamer web/markdowns/" + name_file + "md -o web/pdfs/" + name_file + "pdf")
        os.system("pandoc -s -t beamer  -o web/pdfs/" + name_file + "pdf web/markdowns/" + name_file + "md -V theme:metropolis -V themeoptions:subsectionpage=progressbar")

    # TODO
    """ LaTex """
    if (TEMPLATE == TEMPLATES[3]):
        print("latex")
        os.system("pandoc web/markdowns/" + name_file + "md -o web/pdfs/" + name_file + "pdf")

    #relaod_zathura(name_file)

#eel.start('input_text.html', size=(1000, 600))
eel.start('chose_template.html', size=(1000, 600))
