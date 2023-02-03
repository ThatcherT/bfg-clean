# BFG-Clean

All you need is Docker and Make to clear your git history of secrets.

## Usage

1. `git clone --mirror <repo-url>` to clone your repositories into the top level directory of this project. Don't forget to manually add `.env` file for each repository.`
2. `make` to aggregate .env secrets into a single file.
3. `make bfg` to clean up your git history.
4. `git push` within the cloned repository to push your changes to the remote.

## References

[Bfg Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)  
[Install Docker](https://docs.docker.com/get-docker/)  
Install Make `sudo apt-get update && sudo apt-get -y install make`  
And if you haven't installed WSL for Windows... why not? [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

## Gotcha

If you're using Github, you might've committed a secret via pull request. Your git history is clean, but the secret is still in the pull request.
