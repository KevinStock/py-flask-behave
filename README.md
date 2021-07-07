# py-flask-behave
Demonstration of microservice using Python, Flask, Behave, and Docker

## Install Dependencies
### Docker / Docker Compose
1. `sudo apt-get remove docker docker-engine docker.io containerd runc` Uninstall old versions
1. `sudo apt-get update` Update apt package index
2. `sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release` Install packages to allow apt to use a repository over HTTPS
3. `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg` Add Docker's official GPG key
4. `echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \`
`$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null` Set up the stable repository of Docker Engine
5. `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose` Download current stable release of Docker Compose
6. `sudo chmod +x /usr/local/bin/docker-compose` Apply executale permissions to the binary
7. `docker-compose --version` Test the installation

## Execute Micro Service

Run `docker-compose up` to start

Run `docker-compose exec backend sh` to enter bash on the container

Run `docker system prune -a` to flush docker cache

Run `behave` to execute tests