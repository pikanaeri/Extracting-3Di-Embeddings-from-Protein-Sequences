To run the contents of this Github on a Google Cloud Instance, run the following scripts on the CLI of the Virtual Machine:

```
sudo apt update
sudo apt-get install wget

wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh

sudo apt-get install git
sudo python3 get-pip.py

python3 --version
pip3 --version

wget https://github.com/pikanaeri/Extracting-3Di-Embeddings-from-Protein-Sequences/tree/main
```

- Test commands, and add commands that download Huggingface and Pip (so far, micro and medium computers are unable to support the above commands as the computers run out of storage)
