import subprocess

# Run linux commands
# subprocess.run(["ls", "-l"])

# start python terminal
# subprocess.call(["python3"])

# check terminal history
s = subprocess.check_output(["echo", "Hello World!"])

print(s)
