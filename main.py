import os
from getMotionList import get_motion_list
import requests
import json
from initDirectory import init_directory

chara_id = 14

if __name__ == "__main__":
    # initialize the directory
    init_directory()
    # find the file ended with 'physics.json' under the ./files directory
    files = os.listdir("./files")
    textures = []
    for file in files:
        if file.endswith(".json"):
            # copy the file to ./output and rename the file to 'physics.json'
            os.system(f"cp ./files/{file} ./output")
            os.rename(f"./output/{file}", "./output/physics.json")
        if file.endswith(".moc"):
            # copy the file to ./output and rename the file to 'model.moc'
            os.system(f"cp ./files/{file} ./output")
            os.rename(f"./output/{file}", "./output/model.moc")
        if file.endswith(".png"):
            textures.append(file)
            # copy the file to ./output and rename the file to 'textures_00.png'
            os.system(f"cp ./files/{file} ./output/{file}")

    # get the motion lists
    motion_list = get_motion_list(chara_id)
    for motion in motion_list:
        # download the motion file
        r = requests.get(motion)
        motion_name = motion.split("/")[-1]
        with open(f"./output/motions/{motion_name}", "wb") as f:
            f.write(r.content)
        print(f"Downloaded {motion_name}")

    # construct model.json
    model = {}
    model["model"] = "model.moc"
    model["physics"] = "physics.json"
    model["textures"] = textures
    model["motions"] = {}
    for motion in motion_list:
        motion_name = motion.split("/")[-1]
        motion_name = motion_name.split(".")[0]
        model["motions"][motion_name] = [{"file": f"motions/{motion_name}.mtn"}]
    # write model.json
    with open("./output/model.json", "w") as f:
        json.dump(model, f, indent=4)
