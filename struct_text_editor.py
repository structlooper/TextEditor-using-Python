# starting code..........///.
# importing modules...
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog,messagebox
import os

main_appliction = tk.Tk()
main_appliction.geometry('1000x600')
main_appliction.title('struct_text editor')
main_appliction.wm_iconbitmap('icon.ico')
# main menu.........................
main_menu = tk.Menu()
# file icons
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

file = tk.Menu(main_menu, tearoff = False)

# edit icons
copy_icon = tk.PhotoImage(file='icons/copy.png')
past_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

 
edit = tk.Menu(main_menu, tearoff = False)

# view icons
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

view = tk.Menu(main_menu, tearoff = False)

# color icons
light_default_icon=tk.PhotoImage(file= 'icons/light_default.png')
light_plus_icon=tk.PhotoImage(file= 'icons/light_plus.png')
dark_icon=tk.PhotoImage(file= 'icons/dark.png')
night_blue_icon=tk.PhotoImage(file= 'icons/night_blue.png')
red_icon=tk.PhotoImage(file= 'icons/red.png')
monokai_icon=tk.PhotoImage(file= 'icons/monokai.png')

theme_var = tk.StringVar()

color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Night Blue':('#ededed','#6b9dc2'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
}

color_theme = tk.Menu(main_menu, tearoff = False)

# cascade
main_menu.add_cascade(label='file',menu=file)
main_menu.add_cascade(label='edit',menu=edit)
main_menu.add_cascade(label='view',menu=view)
main_menu.add_cascade(label='color theme',menu=color_theme)

# toolbar.................................
tool_bar=ttk.Label(main_appliction)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font_box
font_tuple=tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,sticky=tk.W,padx=3,pady=3)

#size_box 
size_var = tk.StringVar()
font_size = ttk.Combobox(tool_bar, width=14 ,textvariable= size_var,state='readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=3)

# bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn= ttk.Button(tool_bar,text='old',image=bold_icon,compound=tk.LEFT)
bold_btn.grid(row=0,column=3)

# italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar,text='talic',image=italic_icon,compound=tk.LEFT)
italic_btn.grid(row=0,column=4)

# underline button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar,text='nderline',image=underline_icon,compound=tk.LEFT)
underline_btn.grid(row=0,column=5)

# font color button
font_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn= ttk.Button(tool_bar,image=font_icon)
font_color_btn.grid(row=0,column=6,padx=5)

# alin buttons
alin_left_icon = tk.PhotoImage(file='icons/align_left.png')
alin_left_btn = ttk.Button(tool_bar,image=alin_left_icon)
alin_left_btn.grid(row=0,column=7)

alin_center_icon = tk.PhotoImage(file='icons/align_center.png')
alin_center_btn = ttk.Button(tool_bar,image=alin_center_icon)
alin_center_btn.grid(row=0,column=8)

alin_right_icon = tk.PhotoImage(file='icons/align_right.png')
alin_right_btn = ttk.Button(tool_bar,image=alin_right_icon)
alin_right_btn.grid(row=0,column=9)

#text_editor..............................
text_editor= tk.Text(main_appliction)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_appliction)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# function of text editor
current_font_family = 'Arial'
current_font_size = 16

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

# button fucnality..............

# bold functionality..
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
bold_btn.configure(command=change_bold)

# italic functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))
    
italic_btn.configure(command=change_italic)

# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)

# change font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

# alin functionality
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

alin_left_btn.configure(command=align_left)


def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

alin_center_btn.configure(command=align_center)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

alin_right_btn.configure(command=align_right)


text_editor.configure(font=('Arial',16))
#statusbar.............. .................

status_bar = ttk.Label(main_appliction, text='A Editor by Structlooper')
status_bar.pack(side=tk.BOTTOM,fill=tk.X)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed =  True
        words = len(text_editor.get(1.0,'end-1c').split())
        char = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f"characters : {char} words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>", changed)


# main funality...........................
# new file
url = ''
def new_file(event=None):
    
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

# open func
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0, rf.read())
    except FileNotFoundError:
        return
    except:
        return
    main_appliction.title(os.path.basename(url))


# save file
def save_file(event=None):
    global url
    try:
     if url:
         content = str(text_editor.get(1.0,tk.END))
         with open(url, 'w', encoding='utf-8') as fw:
             fw.write(content)
        
     else:
         url = filedialog.asksaveasfile(mode = 'w', defaultextension=' .txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
         content2 = text_editor.get(1.0,tk.END)
         url.write(content2)
         url.close()
    except:
        return       

# save_as
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension=' .txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return

# exit_functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url, 'w', encoding='utf-8') as rf:
                        rf.write(content)
                        main_appliction.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension=' .txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    main_appliction.destroy()
            elif mbox is False:
                main_appliction.destroy()
        else:
            main_appliction.destroy()
    except:
        return




# file_commands
file.add_command(label='New',image=new_icon,compound=tk.LEFT, accelerator = 'ctrl+N',command=new_file)
file.add_command(label='open',image=open_icon,compound=tk.LEFT, accelerator = 'ctrl+O',command= open_file)
file.add_command(label='save',image=save_icon,compound=tk.LEFT, accelerator = 'ctrl+S',command= save_file)
file.add_command(label='save as',image=save_as_icon,compound=tk.LEFT, accelerator = 'ctrl+alt+S',command=save_as)
file.add_command(label='exit',image=exit_icon,compound=tk.LEFT, accelerator = 'ctrl+Q',command=exit_func)

# edit functions

#  find function working
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word :
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos} + {len(word)}c"
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos= end_pos
                text_editor.tag_config('match',foreground='#d3b774',background='blue')


    def replace():
        word = find_input.get()
        replace_txt = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word, replace_txt)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0,new_content)



    find_dailogue = tk.Toplevel()
    find_dailogue.geometry('450x250+500+200')
    find_dailogue.title('Find')
    find_dailogue.resizable(0,0)

    # frame
    find_frame = ttk.LabelFrame(find_dailogue, text = 'Find/Replace')
    find_frame.pack(pady=20)

    # labels
    text_find_label =  ttk.Label(find_frame, text='Find')
    text_replace_label = ttk.Label(find_frame, text = 'Replace')

    # entry box
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # button
    find_btn = ttk.Button(find_frame, text = 'Find', command=find)
    replace_btn = ttk.Button(find_frame, text = 'Replace', command=replace)

    # griding
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0, padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4) 
    replace_input.grid(row=1,column=1,padx=4,pady=4) 

    find_btn.grid(row=4,column=0)     
    replace_btn.grid(row=4,column=1)

    find_dailogue.mainloop()     


# edit_commands
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator = 'ctrl+C',command= lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Past',image=past_icon,compound=tk.LEFT,accelerator = 'ctrl+V',command= lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator = 'ctrl+X',command= lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear all',image=clear_all_icon,compound=tk.LEFT,accelerator = 'ctrl+alt+X',command= lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator = 'ctrl+F',command=find_func)

#view_commands_in_check_btn
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)

def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar = True

def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        status_bar.pack(side= tk.BOTTOM)
        show_status_bar =True


view.add_checkbutton(label='Tool bar',onvalue=True,offvalue=False,image=tool_bar_icon,compound=tk.LEFT,variable=show_tool_bar,command=hide_tool_bar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,image=status_bar_icon,compound=tk.LEFT,variable=show_status_bar,command=hide_status_bar)

# color theme commands_in_radio_btn

def change_theme():
    change_theme = theme_var.get()
    color_tuple = color_dict.get(change_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)




# color_theme.add_radiobutton(label='Light default',image=light_default_icon,compound=tk.LEFT,variable=theme_var,command=change_theme)
# color_theme.add_radiobutton(label='Light plus',image=light_plus_icon,compound=tk.LEFT,variable=theme_var,command=change_theme)
color_theme.add_radiobutton(label='Dark',image=dark_icon,compound=tk.LEFT,variable=theme_var,command=change_theme)
# color_theme.add_radiobutton(label='Night blue',image=night_blue_icon,compound=tk.LEFT,variable=theme_var,command=change_theme)
color_theme.add_radiobutton(label='Red',image=red_icon,compound=tk.LEFT,variable=theme_var,command=change_theme)
color_theme.add_radiobutton(label='Monokai',image=monokai_icon,compound=tk.LEFT,variable=theme_var,command=change_theme)


main_appliction.config(menu = main_menu)
# bind shorcut keys

main_appliction.bind("<Control-n>", new_file)
main_appliction.bind("<Control-o>", open_file)
main_appliction.bind("<Control-s>", save_file)
main_appliction.bind("<Control-Alt-s>", save_as)
main_appliction.bind("<Control-q>", exit_func)
main_appliction.bind("<Control-f>", find_func)

main_appliction.mainloop()
# ending code................///..
