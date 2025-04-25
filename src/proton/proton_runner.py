import subprocess
import os

class ProtonRunner:
    def __init__(self, proton_path):
        if not os.path.isfile(proton_path):
            raise ValueError(f"Invalid Proton path: {proton_path}")
        self.proton_path = proton_path

    def run_executable(self, executable_path):
        if not os.path.isfile(executable_path):
            raise ValueError(f"Invalid executable path: {executable_path}")

        env = os.environ.copy()
        env["STEAM_COMPAT_DATA_PATH"] = os.path.expanduser("~/.proton-compatdata")
        env["STEAM_COMPAT_CLIENT_INSTALL_PATH"] = os.path.expanduser("~/.steam/steam") 

        try:
            subprocess.run([self.proton_path, "run", executable_path], env=env, check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Proton failed to run the executable: {e}")
