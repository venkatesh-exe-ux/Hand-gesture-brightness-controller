import tkinter as tk

def open_main_ui():
    import prop

root = tk.Tk()
root.title("Control Panel")


root.configure(bg='#f0f8ff')  


start_button = tk.Button(
    root, 
    text="Start Brightness Control", 
    command=open_main_ui, 
    font=("Helvetica", 14), 
    bg='#4CAF50',  
    fg='white', 
    padx=20,       
    pady=10,       
    relief='raised' 
)
start_button.pack(pady=20)


exit_button = tk.Button(
    root, 
    text="Exit", 
    command=root.quit, 
    font=("Helvetica", 14), 
    bg='#f44336',  
    fg='white',    
    padx=20,       
    pady=10,       
    relief='raised' 
)
exit_button.pack(pady=10)

root.mainloop()
