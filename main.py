import os
import platform
from tkinter import messagebox
import tkinter as tk

def get_env_list():
    # get all ENV if entry is empty
    if env_input.get() is None or env_input.get() == '':
        # then fetch all ENV
        for value in get_all_env(onlykeys=True):
            result_listbox.insert(tk.END, value)
        return
    
    env_result = os.getenv(str(env_input.get()).upper()) 
    if env_result is None:
      print('Something went wrong')
      # show message box
      messagebox.showerror('Error', f'{str(env_input.get()).upper()} not found.')
      return
    
    env_result = os.getenv(str(env_input.get()).upper()) 
    # if listbox contain a previous result, then delete all
    if result_listbox.size() > 0:
       clear_listbox()
    
    try:
      separator = None
      # if mac os, then use ':' else use ';'
      if platform.system() == 'Darwin':
        separator = ':'
      elif platform.system() == 'Windows':
        separator = ';'
      
      for value in env_result.split(separator):
        # then insert result into listbox
        result_listbox.insert(tk.END, value)
        
    except:
      messagebox.showerror('Error', 'Something went wrong.')  
      print('Error')

def get_all_env(onlykeys: bool = False) -> list:
  if onlykeys is True:
    return os.environ.keys()
  else:
    return os.environ.items()     

def clear_listbox():
  # clear listbox
  result_listbox.delete(0, tk.END)
  # clear entry (input)
  env_input.delete(0, tk.END)

if __name__ == '__main__':
    app = tk.Tk()
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.title('ENV Finder')
    
    try:
      # print platform (os)
      print(f'os name -> {os.name}; platform -> {platform.system()}; release -> {platform.release()}')
    except:
      pass  # do nothing

    # label
    label = tk.Label(app, text='ENV Name. (such as Home, PATH)', anchor='w')
    label.grid(row=0, column=0, columnspan=3)

    # text input
    env_input = tk.Entry(app)
    env_input.grid(row=1, column=0)

    # find button
    find_button = tk.Button(text='Find', bg='blue', fg='white', command=get_env_list)
    find_button.grid(row=1, column=1)

    # clear listbox button
    clear_listbox_button = tk.Button(text='Clear', command=clear_listbox)
    clear_listbox_button.grid(row=1, column=2)

    # listbox,
    # the result will show here
    result_listbox = tk.Listbox(app)
    result_listbox.grid(row=2, column=0, columnspan=3, sticky='nsew')

    # init listbox with ENV keys
    if not result_listbox.size():
      for value in get_all_env(onlykeys=True):
        result_listbox.insert(tk.END, value)

    app.mainloop()
