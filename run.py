import os
venvdir = "venv"
if os.path.isdir(venvdir) == False:
    
    f = open("make_venv.bat", "w")
    makevenvbat = f'''python -m venv {venvdir}
    cls
    call {venvdir}/Scripts/activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt'''
    f.write(makevenvbat)
    f.close()
    os.system("make_venv.bat")
else:
    os.system(f"call {venvdir}/Scripts/activate.bat")

os.system("python main.py")
    