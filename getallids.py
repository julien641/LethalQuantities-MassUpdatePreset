from customlibrary import loadfile,getallenemies,getallitems,getallflows,getallmoons,createfile
import sys
import os
filename = sys.argv[1] if len(sys.argv)> 1 else "Presets.json"
foldersuffix = sys.argv[2] if len(sys.argv) > 2 else ""
fileprefix = filename.split(".")[0] + foldersuffix
try:
    os.makedirs(os.path.join('output',fileprefix))
except FileExistsError as exc:
    print(exc)


preset = loadfile(f"./config/{filename}")
enemies = getallenemies(preset)
createfile(f"./output/{fileprefix}/enemies.json",enemies)
items = getallitems(preset)
createfile(f"./output/{fileprefix}/items.json",items)
flows = getallflows(preset)
createfile(f"./output/{fileprefix}/flows.json",flows)
moons = getallmoons(preset)
createfile(f"./output/{fileprefix}/moons.json",moons)

configtemplate = {}
for moon in moons:
    x = {"enemies":[],"scrap":[],"daytimeEnemies":[],"dungeonFlows":[],"outsideEnemies":[],"traps":[]}
    configtemplate[moon["id"]] = x
createfile(f"./output/{fileprefix}/configtemplate.json",configtemplate)

