import subprocess

from .version import get_commit_sha


def run():
    sha_long = get_commit_sha()
    sha = sha_long[:7]
    commit_url = f"https://github.com/MaaAssistantArknights/MaaAssistantArknights/commit/{sha_long}"
    subprocess.run(f'echo "commit_sha_full={sha_long}" >> "$GITHUB_ENV"', shell=True)
    subprocess.run(f'echo "commit_sha={sha}" >> "$GITHUB_ENV"', shell=True)
    subprocess.run(f'echo "commit_url={commit_url}" >> "$GITHUB_ENV"', shell=True)

    print(f"Commit Short Sha: {sha}")
    print(f"Commit Sha: {sha_long}")
    print(f"Commit URL: {commit_url}")
