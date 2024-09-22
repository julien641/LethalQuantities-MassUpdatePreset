def defaultenemiesjson(Name):
    defaultenemies={
               "max_enemy_count": 0,
                "power_level": 0,
                "spawn_chance_curve": [
                    {
                        "time": 0.0,
                        "value": 0.0
                    }
                ],
                "stun_time_multiplier": 0,
                "door_speed_multiplier": 0,
                "stun_game_difficulty_multiplier": 0,
                "stunnable": True,
                "killable": True,
                "enemy_hp": 0,
                "spawn_falloff_curve": [
                    {
                        "time": 0.0,
                        "value": 1.0
                    }
                ],
                "use_spawn_falloff": True,
                "name": Name,
                "spawn_in_groups_of": 0
    }

    return defaultenemies

def enemiesjson(defaultmonster,monstername,rarity):
    enemies = {
        "name": defaultmonster.get("name",""),
        "doorSpeedMultiplier": {
            "value": defaultmonster["door_speed_multiplier"],
            "set": True
        },
        "enemyHp": {
            "value": defaultmonster["enemy_hp"],
            "set": True
        },
        "rarity": {
            "value": rarity,
            "set": True
        },
        "killable": {
            "value": defaultmonster["killable"],
            "set": True
        },
        "maxEnemyCount": {
            "value": defaultmonster["max_enemy_count"],
            "set": True
        },
        "powerLevel": {
            "value": defaultmonster["power_level"],
            "set": True
        },
        "groupSpawnCount": {
            "value": defaultmonster["spawn_in_groups_of"],
            "set": True
        },
        "spawnChanceCurve": {
            "value": defaultmonster["spawn_chance_curve"],
            "set": True
        },
        "spawnFalloffCurve": {
            "value": defaultmonster["spawn_falloff_curve"],
            "set": True
        },
        "stunGameDifficultyMultiplier": {
            "value": defaultmonster["stun_game_difficulty_multiplier"],
            "set": True
        },
        "stunTimeMultiplier": {
            "value": defaultmonster["stun_time_multiplier"],
            "set": True
        },
        "stunnable": {
            "value": defaultmonster["stunnable"],
            "set": True
        },
        "useSpawnFalloff": {
            "value": defaultmonster["use_spawn_falloff"],
            "set": True
        },
        "id": monstername
    }
    return enemies
def flowsjson(dungeonid):
    dungeon =   {
                "name": dungeonid,
                "factorySizeMultiplier": {
                    "value": 1.5,
                    "set": True
                },
                "rarity": {
                    "value": 50,
                    "set": True
                },
                "id": dungeonid
                }
    return dungeon
def scrapjson(defaultitem,itemid,rarity):
    scrap =    {
        "name": defaultitem["name"],
        "scrap": defaultitem["scrap"],
        "conductive": {
            "value": defaultitem["conductive"],
            "set": True
        },
        "minValue": {
            "value": defaultitem["min_value"],
            "set": True
        },
        "maxValue": {
            "value": defaultitem["max_value"],
            "set": True
        },
        "weight": {
            "value": defaultitem["weight"],
            "set": True
        },
        "rarity": {
            "value": rarity,
            "set": True
        },
        "id": itemid
    }
    return scrap
def trapjson(defaultitem,itemid,value):
    trap =      {
                "name":defaultitem["name"],
                "description": defaultitem["description"],
                "spawnCurve": {
                    "value": value,
                    "set": True
                },
                "spawnFacingAwayFromWall": defaultitem["spawn_facing_away_from_wall"],
                "id": itemid
            }
    return trap

def defaultmoon(moon,defaultcurrentlevel,defaultenemies,defaultitems,defaulttraps,defaulLevel,defaultdungeon_flows):

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
        "id": moon,
    }
    return default