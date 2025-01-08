# Translate ai

### Note:

We are using huggingface to download models like packages
It stored than in: ~/.cache/huggingface/hub/{model}

### Install

```bash
    # Conda
    conda create -n translate-ai python=3.8
    conda activate translate-ai
    conda install --file requirements.txt
    conda env export > environment.yml
    
    # Venv and pip
    python -m venv translate-ai
    source translate-ai/bin/activate
    pip install -r requirements.txt 
    pip freeze > requirements.txt
```

### Run

```bash
    python3 index.py
```
