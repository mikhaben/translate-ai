# Translate ai

Using huggingface to download lightweight models in a local cache.
It stored than in: ~/.cache/huggingface/hub/{model}

### Install

```bash
    # create environment
    python -m venv env
    # activate environment
    source env/bin/activate
    # install dependencies
    pip install -r requirements.txt 
    # freeze dependencies
    pip freeze > requirements.txt
```

### Edit user_config.py

Choose languages from available languages **[fr, en]** or check file **src/config.py**

### Run

```bash
    python3 index.py
```
