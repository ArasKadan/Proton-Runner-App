# La-la-la-lava, ch-ch-ch-chicken
# Steve's Lava Chicken, yeah, it's tasty as hell
# Ooh, mamacita, now you're ringin' the bell
# Crispy and juicy, now you're havin' a snack
# Ooh, super spicy, it's a lava attack
import tkinter as tk
from tkinter import filedialog, messagebox
from proton.proton_runner import ProtonRunner
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_with_proton(proton_path, executable_path):
    try:
        runner = ProtonRunner(proton_path=proton_path)
        runner.run_executable(executable_path)
        messagebox.showinfo("Success", "Executable ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run executable: {e}")

def check_executable_exists(executable_path):
    return os.path.isfile(executable_path)

def prepare_command(proton_path, executable_path):
    if not os.path.isfile(proton_path):
        raise ValueError(f"Proton executable not found at: {proton_path}")
    if not os.path.isfile(executable_path):
        raise ValueError(f"Executable not found at: {executable_path}")
    
    return [proton_path, "run", executable_path]

def browse_file(entry_field):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, file_path)

def create_ui():
    root = tk.Tk()
    root.title("Proton Runner")
    tk.Label(root, text="Proton Path:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    proton_path_entry = tk.Entry(root, width=50)
    proton_path_entry.grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(proton_path_entry)).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Executable Path:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    executable_path_entry = tk.Entry(root, width=50)
    executable_path_entry.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(executable_path_entry)).grid(row=1, column=2, padx=10, pady=5)

    tk.Button(
        root,
        text="Run",
        command=lambda: run_with_proton(proton_path_entry.get(), executable_path_entry.get())
    ).grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
