import os
import json

folder_path = "/decompiled/apk/AeroWitter"
output_file_path = "/decompiled/apk/AeroWitter.json"
search_text = "Lvlu;->b(Ljava/lang/String;Z)Z"

output_list = []
counter = 1

total_files = sum([len(files) for _, _, files in os.walk(folder_path)])
processed_files = 0

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".smali"):
            file_path = os.path.join(root, filename)
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

            processed_files += 1
            completion_percentage = processed_files / total_files * 100
            print(f"Processing {processed_files}/{total_files} ({completion_percentage:.2f}%)")

print("Processing completed.")

with open(output_file_path, "w") as output_file:
    json.dump(output_list, output_file)
