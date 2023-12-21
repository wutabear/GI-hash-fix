import os
import sys
import json
import re


def main():
    filetoprocess = "hash.json"

    for filename in os.listdir(os.getcwd()):
        if filename == filetoprocess:
            foldername = os.getcwd().split('\\')[-1]
            try:
                print(f"found: {filename}")
                with open(filename, "r", encoding="utf-8") as f:
                    data = f.read()
                    json_data = json.loads(data)
                    texcoord_vb = json_data[0]["texcoord_vb"]
                    blend_vb = json_data[0]["blend_vb"]
                    position_vb = json_data[0]["position_vb"]
                    draw_vb = json_data[0]["draw_vb"]
                    new_ib = json_data[0]["ib"]
                    object_indexes = json_data[0]["object_indexes"]  # array
                    object_classifications = json_data[0]["object_classifications"]  # array

                json_output = f'''  {{
    "old_ib": "",
    "texcoord_vb": "{texcoord_vb}",
    "blend_vb": "{blend_vb}",
    "position_vb": "{position_vb}",
    "draw_vb": "{draw_vb}",
    "new_ib": "{new_ib}",
    "new_draw_vb": "",
    "path": "./EnemyData/{foldername}/hash.json",
    "folder": "./EnemyData/{foldername}",
    "component_name": "",
    "name": "{foldername}"
  }}'''

                with open("hash_output.json", "x") as nf:
                    nf.write(json_output)



            except:
                print("Error processing file")


if __name__ == "__main__":
    main()
