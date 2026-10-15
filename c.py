1. Install curl

sudo apt update

sudo apt install curl -y

2. Install Python and virtual environment tools

sudo apt install python3 python3-pip python3-venv -y

3. Install Ollama

curl -fsSL https://ollama.com/install.sh | sh

4. Check Ollama installation

ollama --version

5. Download and run the Llama 3.2 1B model

ollama run llama3.2:1b

6. Create a Python virtual environment

python3 -m venv .venv

7. Activate the virtual environment

source .venv/bin/activate

8. Install Ollama and Requests Python libraries

python -m pip install ollama requests

9. Deactivate the virtual environment

deactivate
