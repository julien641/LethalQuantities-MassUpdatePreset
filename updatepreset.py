import json
from customlibrary import createfile,loadfile

Preset= loadfile('./config/Presetsupdated.json')
config= loadfile('./config/config.json')
print(Presets.keys())
print(Presets["levels"].keys())


for moon,moonvalue in config.items():
    for entitykey,entityvalue in moonvalue.items():
        for entity in entityvalue:
            currentindex = -1
            for index, value in enumerate(Preset["preset"][moon][entitykey]): 
                if Preset["preset"][moon][entitykey][index]["id"] == entity["id"] :
                    currentindex = index
                    break
            if currentindex != -1 :
                Preset["preset"][moon][entitykey][index] = entity
            else:
                Preset["preset"][moon][entitykey].append(entity)
createfile(f"./output/{fileprefix}/new_preset.json",entity)

#print(originalpreset["presets"])
