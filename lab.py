# import json
# from pathlib import Path
# path_file = Path(r'./Dataset/data/string.txt')
# with open(path_file, 'r', encoding='utf-8') as f:
#     line = f.read()
#     pyresponse = json.loads(line.split('\t'))
#
# # print(lines)
# # print(json.loads(lines))
# print(pyresponse)

# Data to be written
import json

dictionary = [
    {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    },
    {
        "name": "2",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "3"
    }
]
# Serializing json
json_object = json.dumps(dictionary)

# Writing to sample.json
with open("sample.txt", "w") as outfile:
    outfile.write(json_object)
