# typeSim
Typing dynamics simulator. Copy and paste your text and it will be displayed as it is being typed manually.

Ideal for YouTube tutorials whose creators opt for typing on screen instead of speaking. With a script you can simply copy and paste you paragraphs into the program and click run to simulate typing dynamics.

## Running the script on Ubuntu
```
python3 typeSim.py
```

## Running the script on Windows
```
python.exe .\typeSim.py.txt
```

## Creating an executable on Ubuntu
```
pip install pytinstaller
pyinstaller --onefile --noconsole testSim.py
```

The executable is located at ```./dist/typeSim```.

## Creating an executable on Windows
```
pip install pyinstaller
pyinstaller.exe --onefile --noconsole testSim.py.txt
```

The executable is located at ```.\dist\typeSim.exe```.
