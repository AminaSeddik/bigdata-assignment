final_script = """#!/bin/bash
mkdir -p bd-a1/service-result
cp res_dpre.csv eda-in-*.txt vis.png k.txt bd-a1/service-result/
docker stop my_container
"""
with open("final.sh", "w") as f:
    f.write(final_script)
print("Bash script final.sh created!")