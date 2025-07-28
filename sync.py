import subprocess

def git_pull():
    subprocess.run(["git", "pull"])

def git_push():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Add new message"], check=True)
    subprocess.run(["git", "push"], check=True)