import subprocess

command = "ls -l"

command_output = subprocess.run(command, shell=True, capture_output=True, text=True)

print("command output:\n",command_output.stdout)

print("Errors:", command_output.stderr)

print("Return code:", command_output.returncode)