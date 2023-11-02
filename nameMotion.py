from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
motion_descriptions = {}


@app.route("/")
def index():
    # copy the live2d directory from ./output into ./static
    os.system("cp -r ./output ./static")
    # delete the original static/live2d directory
    os.system("rm -rf ./static/live2d")
    # rename the directory to live2d
    os.rename("./static/output", "./static/live2d")

    # get the motion list from the database
    with open("./static/live2d/model.json", "r") as f:
        model = json.load(f)
    motions = list(model["motions"].keys())
    return render_template("index.html", motions=motions)


@app.route("/description", methods=["POST"])
def user_description():
    # Get the motion and description from the POST request
    motion = request.form["motion"]
    description = request.form["description"]

    # Add it to our dictionary
    motion_descriptions[motion] = description
    print(f"Added {motion} to the database with description {description}")
    # return a success message
    return "Success!"


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
