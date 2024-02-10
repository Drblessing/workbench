import subprocess


class BashRunner:
    def __init__(self, script):
        self.script = script

    def run(self):
        """
        Executes the stored Bash script and returns the output and error.
        """
        # Summoning the process
        process = subprocess.Popen(
            ["bash"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Whispering the incantations to the void
        stdout, stderr = process.communicate(self.script)

        # The spirits respond
        return stdout, stderr


# Your Bash script, a spell woven in strings
bash_script = """
echo "Hello from the other side"
ls -l /nonexistentdirectory 2>&1
"""

# The invocation
wizard = BashRunner(bash_script)
output, errors = wizard.run()

print("Output:", output)
if errors:
    print("Errors:", errors)
else:
    print("No errors, the spell was perfect!")
