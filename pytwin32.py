import psutil
import tkinter as tk

root = tk.Tk()

# set the window title
root.title("Process Monitor")

# create a listbox widget
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

# create a button to kill the selected process
def kill_process():
    selection = listbox.curselection()
    if selection:
        process = psutil.Process(processes[selection[0]].pid)
        process.kill()
        listbox.delete(selection)

kill_button = tk.Button(root, text="Kill", command=kill_process)
kill_button.pack()

# Get a list of running processes
processes = list(psutil.process_iter())

# Print the name and status of each process
for process in processes:
    try:
        name = process.name()
        status = process.status()
        listbox.insert(tk.END, f"{name}: {status}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# start the GUI event loop
root.mainloop()