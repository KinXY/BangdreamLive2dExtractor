import os

def init_directory():
    # if there is no ./files directory, create one
    if not os.path.exists("./files"):
        os.mkdir("./files")
    # if there is no ./output directory, create one
    if not os.path.exists("./output"):
        os.mkdir("./output")
        # create a ./output/motions directory
        os.mkdir("./output/motions")
    else:
        # clear the ./output directory
        os.system("rm -rf ./output/*")
        os.mkdir("./output/motions")