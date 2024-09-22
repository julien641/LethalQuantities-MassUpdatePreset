import json
from customlibrary import createfile,loadfile,getallmoons,makeoutputdir
import sys
from entityjson import enemiesjson,trapjson,scrapjson,flowsjson,defaultmoon,defaultenemiesjson
filename = sys.argv[1] if len(sys.argv)> 1 else "Presets.json"
makeoutputdir(filename.split('.')[0])
Preset = loadfile(f"./config/{filename}")
moons= getallmoons(Preset)

presetmoons = []
for moon in moons:
    presetmoons.append(moon["id"])
defaultpresets = Preset["defaults"]
defaultenemies = defaultpresets["enemies"]
defaultitems = defaultpresets["items"]
defaulttraps = defaultpresets["traps"]
defaulLevel = defaultpresets["levels"]
defaultdungeon_flows = defaultpresets["dungeon_flows"]
currentpresets = Preset["presets"]

def daytime_enemies(monstersid,currentmoonenemies,defaultenemies,defaultvalue):
    for enemies in currentmoonenemies:
        if monstersid==enemies["id"]:
            return enemies
    return enemiesjson(defaultenemies,monstersid,defaultvalue)


for moon in presetmoons:
    defaultcurrentlevel = defaulLevel[moon]
    currentmoon = currentpresets.get(moon)
    default = {}
    if currentmoon == None:
        default = defaultmoon(moon,defaultcurrentlevel,defaultenemies,defaultitems,defaulttraps,defaulLevel,defaultdungeon_flows)
    else:
        #print(currentmoon["daytimeEnemies"])
        currentscrap = {scrap["id"]:scrap for scrap in currentmoon["scrap"]["value"]}
        currentdaytimeEnemies = {daytimeEnemies["id"]:daytimeEnemies for daytimeEnemies in currentmoon["daytimeEnemies"]["value"]}
        currentdungeonFlows = {dungeonFlows["id"]:dungeonFlows for dungeonFlows in currentmoon["dungeonFlows"]["value"]}
        currentenemies = {enemies["id"]:enemies for enemies in currentmoon["enemies"]["value"]}
        currentoutsideEnemies = {outsideEnemies["id"]:outsideEnemies for outsideEnemies in currentmoon["outsideEnemies"]["value"]}
        currenttraps = {traps["id"]:traps for traps in currentmoon["traps"]["value"]}

        print( defaultcurrentlevel["daytime_enemies"].items()  )
        print(currentdaytimeEnemies.items())
        print( defaultcurrentlevel["daytime_enemies"].update(currentdaytimeEnemies) )
        print(currentdaytimeEnemies.items())


        alldaytime_enemies = defaultcurrentlevel["daytime_enemies"].copy()
        alldaytime_enemies.update(currentdaytimeEnemies)
        allenemies = defaultcurrentlevel["enemies"].copy()
        allenemies.update(currentenemies)
        defaultflow={flowid:"" for flowid in defaultdungeon_flows}
        allflows = defaultflow.copy()
        allflows.update(currentdungeonFlows)
        alloutsideenemies = defaultcurrentlevel["outside_enemies"]
        alloutsideenemies.update(currentoutsideEnemies)

        print(alloutsideenemies)
        allscrap = defaultcurrentlevel["scrap"]
        allscrap.update(currentscrap)
        alltraps = defaultcurrentlevel["spawnable_map_objects"].copy()
        alltraps.update(currenttraps)


        default = {
            "name":defaultcurrentlevel["planet_name"],
            "parent":"default-global",
            "levelDescription": {
                    "value": defaultcurrentlevel["description"],
                    "set": True
                },
            "riskLevel": {
                "value": defaultcurrentlevel["risk_level"],
                "set": True
            },
            "daytimeEnemies": {
                    "value": [value if isinstance(value,dict) else enemiesjson(defaultenemies[monsters], monsters, value)  for monsters , value in alldaytime_enemies.items() ],
                    "set": True
                },
            "daytimeSpawnCurve": {
                "value":  defaultcurrentlevel["daytime_enemy_spawn_curve"],
                "set": True
            },
            "daytimeSpawnProbabilityRange": {
                "value": defaultcurrentlevel["daytime_enemy_spawn_probability_range"],
                "set": True
            },
            "dungeonFlows": {
                "value": [ values if values != "" else flowsjson(ids) for ids,values in allflows.items()],
                "set": True
            },
            "enemies": {
                "value": [ value if isinstance(value,dict) else enemiesjson(defaultenemies[monsters], monsters, value) for monsters , value in allenemies.items()],
                "set": True
            },
            "mapSizeMultiplier": {
                "value": defaultcurrentlevel["factory_size_multiplier"],
                "set": True
            },
            "maxDaytimePowerCount": {
                "value": defaultcurrentlevel["max_daytime_power_count"],
                "set": True
            },
            "maxOutsidePowerCount": {
                "value": defaultcurrentlevel["max_outside_power_count"],
                "set": True
            },
            "maxPowerCount": {
                "value": defaultcurrentlevel["max_power_count"],
                "set": True
            },
            "maxScrap": {
                "value": defaultcurrentlevel["max_scrap"],
                "set": True
            },
            "minScrap": {
                "value": defaultcurrentlevel["min_scrap"],
                "set": True
            },
            "outsideEnemies": {
                "value": [ rarity if isinstance(rarity,dict) else enemiesjson(defaultenemies.get(monsters,defaultenemiesjson(monsters)),monsters,rarity)  for monsters , rarity in alloutsideenemies.items()],
                "set": True
                },
            "outsideSpawnCurve": {
            "value": defaultcurrentlevel["outside_enemy_spawn_curve"],
            "set": True
            },
            "price": {
                "value": [],
                "hidden": False,
                "set": False
            },
            "scrap": {
                "value": [ rarity if isinstance(rarity,dict) else scrapjson(defaultitems[scrap],scrap,rarity)  for scrap , rarity in allscrap.items()],
                "set": True
            } ,
            "scrapAmountMultiplier": {
                "value": 1.2,
                "set": True
            },  "scrapValueMultiplier": {
                "value": 0.4,
                "set": True
            },
            "spawnCurve": {
                "value": defaultcurrentlevel["enemy_spawn_curve"],
                "set": True
                },
            "spawnProbabilityRange": {
                "value": defaultcurrentlevel["enemy_spawn_probability_range"],
                "set": True
            },
            "traps": {
            "value": [value if isinstance(value,dict) else trapjson(defaulttraps[trap],trap,value) for trap , value in alltraps.items()] ,
            "set": True
            },
            "id": moon
        
        }
    Preset["presets"][moon] = default
createfile(f"./output/{filename.split('.')[0]}/Presets.json", Preset, indent=None)