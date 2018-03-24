from tkinter import filedialog
import tkinter as tk
import os
import shutil


def submit():
    global sounds_dir
    global xml_string
	
    #Tilde expand to the gnome sounds directory
    sounds_dir = os.path.expanduser('/usr/share/sounds/gnome/default/alerts/')

    #Copy the sound file into the appropriate directory and print success message
    shutil.copyfile(filepath, sounds_dir + filename)
    print("File copied")

    text_entry_name = text_entry.get()
    print(text_entry_name)
    
    xml_formatted = """<sound deleted="false"> 
    <name>"""+ text_entry_name +"""</name> 
    <filename>"""+ sounds_dir + filename +"""</filename> 
    </sound>
    </sounds>"""

    print(xml_formatted)
    delete_list = ["</sounds>"]

    myfile = open("/usr/share/gnome-control-center/sounds/gnome-sounds-default.xml", "r")
    list_of_lines = [line.strip('\n') for line in myfile]
    myfile.close()
    print(list_of_lines)
    del list_of_lines[-1]
    print(list_of_lines)
    
    myfile = open("/usr/share/gnome-control-center/sounds/gnome-sounds-default.xml", "w")
    for item in list_of_lines:
        myfile.write("%s\n" % item)
    myfile.close()
    
    myfile = open("/usr/share/gnome-control-center/sounds/gnome-sounds-default.xml", "a")
    myfile.write(xml_formatted)
    
    quit()
    
    
       


#Create button with callback
def callback():
    global filepath
    global filename
	
	#Show path dialog box to select the sound file you want and print the file path
    filepath = filedialog.askopenfilename() 
    print(filepath)

    #Extract only the file name from the previously provided path and print it
    filename = os.path.basename(os.path.normpath(filepath))
    print(filename)


#Create the tk root
root = tk.Tk()

step1_label = tk.Label(root, text="1.- Select an audio file you want to add to gnome alerts.")
step1_label.pack()
select_button = tk.Button(root, text="Browse", command=callback)
select_button.pack()

step2_label = tk.Label(root, text="2.- Change it's default name.")
step2_label.pack()
text_entry = tk.Entry(root)
text_entry.pack()

step3_label = tk.Label(root, text="3.- Click OK.")
step3_label.pack()
ok_button = tk.Button(root, text="OK", command=submit)
ok_button.pack()

root.mainloop()

