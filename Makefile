get_secrets:
	python get_secrets.py
	echo "Run 'make bfg' to run the BFG Repo-Cleaner on your repository."
bfg:
	docker build -t bfg .  # builds a Docker image with the tag "bfg" using the current directory as context.
clean:
	# removes the Docker image "bfg" from local cache
	docker rmi bfg