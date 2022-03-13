'''
Build with "pyinstaller --onefile park_ptz.py"
'''
import json
from pathlib import Path
from visca_over_ip import Camera

# path of the config file
config_path = Path("config.json")

# get the path of the script file
config = json.loads((Path(__file__).parent / config_path).read_text(encoding="utf8"))

# create the camera object
cam = Camera(config["ptz"]["ip"])

# send the "park" position to the camera
cam.pantilt(pan_speed=24, tilt_speed=24, pan_position=int(config["position"]["pan"], 16), tilt_position=int(config["position"]["tilt"], 16), relative=False)