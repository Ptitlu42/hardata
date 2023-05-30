import os
import subprocess

def getDiskData():
    total_space = 0
    used_space = 0

    df_output_lines = subprocess.check_output(['df']).decode('utf-8').split('\n')

    for line in df_output_lines[1:]:
        if not line:
            continue
        values = line.split()
        if values[0].startswith(('tmpfs', 'devtmpfs', 'udev')):
            continue
        total_space += int(values[1])  
        used_space += int(values[2])

    free_space = total_space - used_space

    used_percent = (used_space / total_space) * 100
    free_percent = 100 - used_percent

    return total_space, used_space, free_percent, used_percent, free_space
    

