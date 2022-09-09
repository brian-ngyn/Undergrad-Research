import pandas as pd
import numpy as np
import hashlib
import tkinter as tk
from pyarrow import csv
from tkinter import filedialog
import time

###### Start Intepreting the code from #1 to #11 for easier walkthrough #####

# GUI Library - tkinter

from tkinter import *
root = Tk()
root.title('Bloom-Filter Encoding')
root.geometry("565x160")

def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()

def closeProgram():
    root.destroy()

def closePopup(window):
    window.destroy()

def resetProgram():
    encryptionCodeEntry.delete(0, END)
    button_browse_file.grid_forget()
    button_file_parameters.grid_forget()
    
def saveFile():
    # 12: Save file and allow the user to continue or close the program.
    saveasfilename = filedialog.asksaveasfilename(initialdir='/', initialfile=".csv", defaultextension='.csv', title='Save File', filetypes=(('Comma-separated values', '*.csv'), ('All Files', '*.*')))
    # File saved as csv 
    df_to_encrypt.to_csv(saveasfilename, index=False)
    # readFile.to_pickle(saveasfilename+'.pkl',protocol=4)
    # Previous implementation saved as pkl - do we need this still?
    finished_popup.destroy()

    exit_popup = Toplevel(root)
    exit_popup.title("Bloom-Filter Encoding")
    exit_popup.geometry("550x130")
    exit_popup.attributes('-alpha', 0.0)
    centerWindow(exit_popup)
    exit_popup.attributes('-alpha', 1.0)
    
    exit_popup_label = Label(exit_popup, text="File has been saved.\nWould you like to encrypt another file?")
    exit_popup_label.pack(pady=5)

    button_continue_program_frame = Frame(exit_popup)
    button_continue_program_frame.pack(pady=5)
    button_continue_program = Button(button_continue_program_frame, text="Yes", command=lambda: [resetProgram(), closePopup(exit_popup)])
    button_continue_program.grid(row=0, column=0)

    button_close_program_frame = Frame(exit_popup)
    button_close_program_frame.pack(pady=5)
    button_close_program = Button(button_close_program_frame, text="Exit", command=closeProgram)
    button_close_program.grid(row=0, column=0)

def bloom_filter(plnTxt, saltStr, qGrmLen=2, filterLen=32):
    
    plnTxt = f'_{plnTxt}_'
    bloomFilter = 0
    
    for i in range(len(plnTxt)-qGrmLen+1):
        byteStr = (saltStr + plnTxt[i:i+qGrmLen]).encode('utf-8','replace')
    
        idxMd5 = int( hashlib.md5(byteStr).hexdigest(), 16) % filterLen
        idxSha = int( hashlib.sha256(byteStr).hexdigest(), 16) % filterLen
        
        bloomFilter |= 1 << idxMd5
        bloomFilter |= 1 << idxSha
        
    return bloomFilter

def startEncryption():
    # 10: Loops through the columns that have been selected and encrypts each value
    global df_to_encrypt
    df_to_encrypt = readFile.copy()

    for i in range(len(cols_selected)):
        if (cols_selected[i].get() == 1):
            curr_col_name = df_to_encrypt.columns[i]
            curr_col_df = df_to_encrypt.loc[:, curr_col_name]

            j = 0
            for row_val in curr_col_df:
                encrypted_val = bloom_filter(row_val, salt)
                df_to_encrypt.at[j, curr_col_name] = format(encrypted_val, 'x')
                j+=1

    encrypt_popup.destroy()
    
    # 11: Popup to let user know that encryption has finished prompt to save the file
    global finished_popup

    finished_popup = Toplevel(root)
    finished_popup.title("Bloom-Filter Encoding")
    finished_popup.geometry("500x90")
    finished_popup.attributes('-alpha', 0.0)
    centerWindow(finished_popup)
    finished_popup.attributes('-alpha', 1.0)
    
    finished_popup_label = Label(finished_popup, text="The encryption has sucessfully finished. Please save the file.\nSaving may take a while. Please do not exit the process.")
    finished_popup_label.pack(pady=5)

    save_file_button_frame = Frame(finished_popup)
    save_file_button_frame.pack(pady=5)
    save_file_button = Button(save_file_button_frame, text="Save File", command=saveFile)
    save_file_button.grid(row=0, column=0)

def confirmSelection():
    # 8: Popup window listing the selections that will be encrypted from the last step
    global encrypt_popup

    encrypt_popup = Toplevel(root)
    encrypt_popup.geometry("420x410")
    encrypt_popup.attributes('-alpha', 0.0)
    centerWindow(encrypt_popup)
    encrypt_popup.attributes('-alpha', 1.0)
    
    popup_label = Label(encrypt_popup, text="The following columns will be encrypted:")
    popup_label.pack(pady=5)

    # display columns that were selected in the previous step in a scroll panel.
    scrollFrame = Frame(encrypt_popup)
    canvas = Canvas(scrollFrame)
    scrollbar = Scrollbar(scrollFrame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for i in range(len(cols_selected)):
        if ((cols_selected[i].get()) == 1):
            Label(scrollable_frame, text=readFile.columns[i]).pack(side=TOP, fill=X)
    
    scrollFrame.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 9: Continue and cancel button to start/stop the encryption process
    button_encrypt_frame = Frame(encrypt_popup)
    button_encrypt_frame.pack(pady=5)
    button_encrypt = Button(button_encrypt_frame, text="Encrypt", command=startEncryption)
    button_encrypt.grid(row=0, column=1)

    # If cancel is selected, go back to step 6 and re-select columns that will be encrypted.
    button_encrypt_cancel_frame = Frame(encrypt_popup)
    button_encrypt_cancel_frame.pack(pady=5)
    button_encrypt_cancel = Button(button_encrypt_cancel_frame, text="Cancel", command=lambda: [closePopup(encrypt_popup), fileParameters()])
    button_encrypt_cancel.grid(row=0, column=0)

    encryption_warning_label = Label(encrypt_popup, text="Encryption may take a while. Please do not exit the process")
    encryption_warning_label.pack(pady=5)

def fileParameters():
    # 6: Display columns in the read file and let user select which columns will be encrypted
    finished_selecting = tk.IntVar()

    popup = Toplevel(root)
    popup.geometry("410x345")
    popup.attributes('-alpha', 0.0)
    centerWindow(popup)
    popup.attributes('-alpha', 1.0)
    
    popup_label = Label(popup, text="Please select which columns will be encrypted.")
    popup_label.pack(pady=5)
    finished_selecting.set(0)

    # Display check boxes in a scroll pane
    scrollFrame = Frame(popup)
    canvas = Canvas(scrollFrame)
    scrollbar = Scrollbar(scrollFrame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Loop through the dataframe and create checkboxes for each column in a scroll pane
    global cols_selected
    cols_selected = []
    i = 0
    for col in readFile.columns:
        cols_selected.append(IntVar(value=0))
        c = Checkbutton(scrollable_frame, text=col, variable=cols_selected[i])
        c.pack(side=TOP, fill=X)
        i+=1
    
    scrollFrame.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 7: Upon pressing continue, open the confirmation screen.
    continue_button_frame = Frame(popup)
    continue_button_frame.pack(pady=5)
    continue_button = Button(continue_button_frame, text="Continue", command=lambda:[closePopup(popup), confirmSelection()])
    continue_button.grid(row=0, column=0)

def BrowseFile():
    
    # 4: Open Dialog Box to read CSV file anywhere from the local machine (only CSV implementation currently)
    root.filename = filedialog.askopenfilename(initialdir='/',title="Select A File",filetypes=(("all files","*.*"),("csv",".*csv")))
    global readFile

    error = True
    error_message = ""
    start_time = time.time()
    try: # make sure there's not an error when reading the file
        readFile = pd.read_csv(root.filename, engine="pyarrow")
    except Exception as e:
        error = True
        error_message = repr(e)
    else:
        error = False
    total_time = time.time() - start_time

    popup = Toplevel(root)
    if (error == False):
        popup.geometry("755x125")
        popup.attributes('-alpha', 0.0)
        centerWindow(popup)
        popup.attributes('-alpha', 1.0)
        
        popup_label = Label(popup, text="File has been loaded, took " + "{:.2f}".format(total_time) + " seconds. \nFile Selected: " + root.filename + "\n\nPlease set the file-specific parameters.")
        popup_label.pack(pady=5)

        continue_button_frame = Frame(popup)
        continue_button_frame.pack(pady=5)
        continue_button = Button(continue_button_frame, text="Continue", command=lambda: closePopup(popup))
        continue_button.grid(row=0, column=0)

        # 5: Enable file-specific parameters button
        global button_file_parameters
        button_file_parameters = Button(buttons_frame,text='Set file-specific parameters',command=fileParameters)
        button_file_parameters.grid(row=2,column=0)
    else:
        popup.geometry("350x100")
        popup.attributes('-alpha', 0.0)
        centerWindow(popup)
        popup.attributes('-alpha', 1.0)

        # 5: Error while loading the file popup
        popup_label = Label(popup, text="There was an error loading the file. Please try again.\n\nError message: " + error_message)
        popup_label.pack(pady=5)

        continue_button_frame = Frame(popup)
        continue_button_frame.pack(pady=5)
        continue_button = Button(continue_button_frame, text="Continue", command=lambda: closePopup(popup))
        continue_button.grid(row=0, column=0)
    
def readSalt():
    # 2: Set the salt parameter for the run
    global salt
    salt = encryptionCodeEntry.get()
    
    # Confirmation popup
    if salt == "":
        popup = Toplevel(root)
        popup.title("Bloom-Filter Encoding")
        popup.geometry("350x75")
        popup.attributes('-alpha', 0.0)
        centerWindow(popup)
        popup.attributes('-alpha', 1.0)
        popup_label = Label(popup, text="Encryption code cannot be empty. Please try again.")
        popup_label.pack(pady=5)

        continue_button_frame = Frame(popup)
        continue_button_frame.pack(pady=5)
        continue_button = Button(continue_button_frame, text="Continue", command=lambda: closePopup(popup))
        continue_button.grid(row=0, column=0)
    else: 
        # 3: Enable next button to Browse for a CSV file
        global button_browse_file
        button_browse_file = Button(buttons_frame,text='Select CSV File',command=BrowseFile)
        button_browse_file.grid(row=1,column=0)
    
# 1: Initial Screen with 1 entry box to accept encryption key (salt)

root.grid_columnconfigure(0, minsize=200)

encryptionCodeLabel = Label(root, text='Encryption Key')
encryptionCodeLabel.grid(row=0, column=0)
encryptionCodeEntry = Entry(root, width=50, borderwidth=1)
encryptionCodeEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

button_next = Button(root,text='Ok',command=readSalt)
button_next.grid(row=0,column=2) 

buttons_frame = Frame(root)
buttons_frame.grid(row=1,column=0)

root.attributes('-alpha', 0.0)
centerWindow(root)
root.attributes('-alpha', 1.0)
root.mainloop()