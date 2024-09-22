import json
import os

def loadfile(filepath):
    with open(filepath) as f:
        return json.loads(f.read())

def writingpreset(filepath,content):
    with open(filepath, "w") as f:
            f.write(json.dumps(content))


def createfile(filepath,content,indent = 2):
    with open(filepath, "w") as f:
        if indent:
            f.write(json.dumps(content, indent=2))
        else:
            f.write(json.dumps(content)) 
def getallenemies(preset):
    rc=[]
    for key, value in preset["defaults"]["enemies"].items():
        try:
            rc.append({"id":key,"Name":preset["defaults"]["enemies"][key].get("name","")}) 
        except Exception as exc:
            print(exc)
            print(key, value)
            raise Exception from  exc
    return rc
def getallitems(preset):
    rc = []
    for key, value in preset["defaults"]["items"].items():
        try:
            rc.append({"id":key,"Name":preset["defaults"]["items"][key].get("name","")}) 
        except Exception as exc:
            print(exc)
            print(key, value)
            raise Exception from  exc
    return rc
def getallflows(preset):
    return preset["defaults"]["dungeon_flows"]
    
def getallmoons(preset):
    rc = []
    for key, value in preset["defaults"]["levels"].items():
        try:
            rc.append({"id":key,"Name":preset["defaults"]["levels"][key].get("planet_name","")}) 
        except Exception as exc:
            print(exc)
            print(key, value)
            raise Exception from  exc
    return rc
def makeoutputdir(fileprefix):
    try:
        os.makedirs(os.path.join('output',fileprefix))
    except FileExistsError as exc:
        print(exc)