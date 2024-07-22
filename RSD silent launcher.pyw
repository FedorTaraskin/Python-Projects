import subprocess

def run_silent_subprocess():
	# Placeholder for the exact subprocess command and arguments
	command = [r"C:\Windows\Ram Shit Deleter\EmptyStandbyList.exe"]  # Replace with your actual command and arguments
	
	# Create the subprocess and run it silently
	subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
	run_silent_subprocess()

input()
