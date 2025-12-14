# PyanoBuddy
Connect your synth to Midi. First midi input is used.
Need latest python
```
pip install -r requirements.txt
pyinstaller --onefile main.py --hidden-import=mido.backends.rtmidi
```

Try to copy the machine.
Increase difficulty by increasing self._note_count variable.
Order of notes is currently not checked.

Scale change is code change. Best of luck with that.
Use the below variables:
    root = keys['C']
    scale = scales['MAJOR_CHORD']