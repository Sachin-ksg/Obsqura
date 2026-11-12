import json
#Python provides a built in module called json to work with json data

with open("file.json","r") as f:
    data=json.load(f)
    print(data)
    print(data["name"])

#json.dump()- write a python data into a json file
#json.dumps -convert a python data into json string
#json.loads- convert a json strings into python data

student={"mark":90, "location":"ekm"}
with open("file.json","w") as f:
    json.dump(student,f)

