from jsonschema import Draft202012Validator as Validator
import json

VISION_DAQ = {
    "type" : "object",
    "properties" : {
        "yaw" : {"type":"number"},
        "pitch" : {"type":"number"},
        "rpm" : {"type":"number"},
        "speed" : {"type":"number"},
        "depth" : {"type":"number"},
        "battery" : {"type":"boolean"},
    }
}

validator = Validator(schema=VISION_DAQ)

my_json = json.loads('{"yaw":0,"pitch":0,"rpm":0,"speed":0,"depth":0,"battery":true}')

json_is_valid = validator.is_valid(my_json)

print(json_is_valid, my_json)
