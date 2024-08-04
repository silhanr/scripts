#Enter Python code here and hit the Run button.
import json

data = {"key1" : "value1", "key2" : "value2"}

output = json.dumps(data)

print("data = {}".format(output))

# Enter Python code here and hit the Run button.
import json

from json import JSONEncoder

sampleDict = {"key1": "value1", "key2": "value2"}
# write code to print the value of key2

input = json.dumps(sampleDict, indent=2, separators=(",", " = "))

print(input)

sampleDict2 = {"id": 1, "name": "value2", "age": 29}

input2 = json.dumps(sampleDict2, indent=2, sort_keys=True)
print(input2)

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

inputDict = json.loads(sampleJson)

print("Salary is {}".format(inputDict["company"]["employee"]["payble"]["salary"]))


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# vehicleJson = json.dumps(vehicle.__dict__,indent=2)

vehicleJson = json.dumps(vehicle, indent=2, cls=VehicleEncoder)

print(vehicleJson)