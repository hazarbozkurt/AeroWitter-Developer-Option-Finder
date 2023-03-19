import os
import json

folder_path = "/decompiled/apk/AeroWitter"
output_file_path = "/decompiled/apk/AeroWitter.json"
search_text = "Lvlu;->b(Ljava/lang/String;Z)Z"
output_list = []
counter = 1

for filename in os.listdir(folder_path):
    if filename.endswith(".smali"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as f:
            lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i]
            if search_text in line:
                for j in range(i-1, -1, -1):
                    if "const-string" in lines[j]:
                        value_line = lines[j]
                        value = value_line.split(",")[1].strip().strip('"')
                        output_list.append({"title": f"Value {counter}", "description": value})
                        counter += 1
                        break
                        
with open(output_file_path, "w") as output_file:
    json.dump(output_list, output_file)
