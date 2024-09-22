import json
from customlibrary import createfile, loadfile
from entityjson import enemiesjson, trapjson, scrapjson, flowsjson
import sys
filename = sys.argv[1] if len(sys.argv)> 1 else "Presets.json"
Preset = loadfile(f"./config/{filename}")
moons  = getallmoons(preset)
allmoons = []
for moon in moons:
    allmoons.append(moon["id"])

presetmoons = []
for key, levels in Preset["presets"].items():
    presetmoons.append(key)

print(allmoons)
print(presetmoons)
missingmoons = []
for moons in allmoons:
    if moons not in presetmoons:
        missingmoons.append(moons)
print(missingmoons)

defaultpresets = Preset["defaults"]
defaultenemies = defaultpresets["enemies"]
defaultitems = defaultpresets["items"]
defaulttraps = defaultpresets["traps"]
defaulLevel = defaultpresets["levels"]
defaultdungeon_flows = defaultpresets["dungeon_flows"]


for missing in missingmoons:
    defaultcurrentlevel = defaulLevel[missing]
    default = {
        "name": defaultcurrentlevel["planet_name"],
        "parent": "default-global",
        "levelDescription": {"value": defaultcurrentlevel["description"], "set": True},
        "riskLevel": {"value": defaultcurrentlevel["risk_level"], "set": True},
        "daytimeEnemies": {
            "value": [
                enemiesjson(defaultenemies[monsters], monsters, value)
                for monsters, value in defaultcurrentlevel["daytime_enemies"].items()
            ],
            "set": True,
        },
        "daytimeSpawnCurve": {
            "value": defaultcurrentlevel["daytime_enemy_spawn_curve"],
            "set": True,
        },
        "daytimeSpawnProbabilityRange": {
            "value": defaultcurrentlevel["daytime_enemy_spawn_probability_range"],
            "set": True,
        },
        "dungeonFlows": {
            "value": [flowsjson(dungeon) for dungeon in defaultdungeon_flows],
            "set": True,
        },
        "enemies": {
            "value": [
                enemiesjson(defaultenemies[monsters], monsters, value)
                for monsters, value in defaultcurrentlevel["enemies"].items()
            ],
            "set": True,
        },
        "mapSizeMultiplier": {
            "value": defaultcurrentlevel["factory_size_multiplier"],
            "set": True,
        },
        "maxDaytimePowerCount": {
            "value": defaultcurrentlevel["max_daytime_power_count"],
            "set": True,
        },
        "maxOutsidePowerCount": {
            "value": defaultcurrentlevel["max_outside_power_count"],
            "set": True,
        },
        "maxPowerCount": {"value": defaultcurrentlevel["max_power_count"], "set": True},
        "maxScrap": {"value": defaultcurrentlevel["max_scrap"], "set": True},
        "minScrap": {"value": defaultcurrentlevel["min_scrap"], "set": True},
        "outsideEnemies": {
            "value": [
                enemiesjson(defaultenemies[monsters], monsters, rarity)
                for monsters, rarity in defaultcurrentlevel["outside_enemies"].items()
            ],
            "set": True,
        },
        "outsideSpawnCurve": {
            "value": defaultcurrentlevel["outside_enemy_spawn_curve"],
            "set": True,
        },
        "price": {"value": [], "hidden": False, "set": False},
        "scrap": {
            "value": [
                scrapjson(defaultitems[scrap], scrap, rarity)
                for scrap, rarity in defaultcurrentlevel["scrap"].items()
            ],
            "set": True,
        },
        "scrapAmountMultiplier": {"value": 1.2, "set": True},
        "scrapValueMultiplier": {"value": 0.4, "set": True},
        "spawnCurve": {"value": defaultcurrentlevel["enemy_spawn_curve"], "set": True},
        "spawnProbabilityRange": {
            "value": defaultcurrentlevel["enemy_spawn_probability_range"],
            "set": True,
        },
        "traps": {
            "value": [
                trapjson(defaulttraps[trap], trap, value)
                for trap, value in defaultcurrentlevel["spawnable_map_objects"].items()
            ],
            "set": True,
        },
        "id": missing,
    }
    results = default.copy()
    # del results["id"]
    # del results["levelDiscription"]
    # print(default)
    Preset["presets"][missing] = default
    # Preset["results"][missing]= results

    # print(Preset["presets"][missing])
createfile(f"./output/{filename.split(".")[0]}/{filename}", Preset, indent=None)
