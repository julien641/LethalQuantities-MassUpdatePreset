import json
def loadfile(filepath):
    with open(filepath) as f:
        return json.loads(f.read())
originalpreset =loadfile('./Presets.json')
config = loadfile('./config.json')

print(originalpreset.keys())
print(originalpreset["levels"].keys())
print(originalpreset["presets"])
