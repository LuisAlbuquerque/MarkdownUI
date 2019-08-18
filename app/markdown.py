import io
from base64 import b64encode
import eel
import os


eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}


@eel.expose
def create_file(file_content):
    #print(file_content)
    name_file = "newfile." 
    with open(name_file + "md","w+") as fd:
        fd.write(file_content)

    os.system("pandoc " + name_file + "md -o " + name_file + "pdf")


#eel.start('index.html', size=(1000, 600))
eel.start('input_text.html', size=(1000, 600))
