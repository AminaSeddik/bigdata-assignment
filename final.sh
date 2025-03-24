# Define the bash script content
final_script = """#!/bin/bash
mkdir -p bd-a1/service-result
cp res_dpre.csv eda-in-*.txt vis.png k.txt bd-a1/service-result/
docker stop my_container
"""

# Check if the script file can be created and written to
try:
    # Open and write the script to a file
    with open("final.sh", "w") as f:
        f.write(final_script)
    
    print("Bash script final.sh created!")

    # Make the script executable if you're on a Unix-like OS
    import os
    os.chmod("final.sh", 0o755)  # This will make the script executable

except Exception as e:
    print(f"Error creating the bash script: {e}")
