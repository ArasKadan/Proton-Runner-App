import os

def check_executable_exists(executable_path):
    return os.path.isfile(executable_path)

def prepare_command(proton_path, executable_path):
    if not os.path.isfile(proton_path):
        raise ValueError(f"Proton executable not found at: {proton_path}")
    if not os.path.isfile(executable_path):
        raise ValueError(f"Executable not found at: {executable_path}")
    
    return [proton_path, "run", executable_path]
