import os

def create_secrets_file():
    """
    This function searches the entire repo for .env files
    and creates a .txt file with the secret values.
    The .txt file is created in the root directory and
    used for BFG Repo-Cleaner.
    """
    # Define the root directory
    root_dir = "."
    # check if secrets.txt exists, delete if it does
    if os.path.exists("secrets.txt"):
        print("secrets.txt already exists. Deleting...")
        os.remove("secrets.txt")

    # Iterate over the root directory
    env_files = 0
    for root, dirs, files in os.walk(root_dir):
        # Iterate over each file in the root directory
        for file in files:
            # Check if the file is a .env file
            if file.endswith(".env"):
                env_files += 1
                # Define the path to the .env file
                env_path = os.path.join(root, file)
                # read the .env file
                with open(env_path, 'r') as env_file:
                    # for each line in the .env file
                    for line in env_file:
                        # get the value of pattern <secret>=<value>
                        secret = line.split("=")[1]
                        # append the value to the .txt file
                        with open("secrets.txt", "a") as secrets_file:
                            secrets_file.write(secret)
    print(f"Found {env_files} .env files.")
    print("Check secrets.txt for any values that do not need to be cleaned from Git history.")

# Call the function
if __name__ == "__main__":
    create_secrets_file()