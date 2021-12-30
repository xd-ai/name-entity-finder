# name-entity-finder
A small Flask app for identifying named entities in a sentence using spaCy

First, we will need to install poetry(any other python environment manager will also suffice, refer to pyproject.toml for dependencies):
https://python-poetry.org/docs/master/#installing-with-the-official-installer

After that, clone the repo and initialize the poetry environment:
```
git clone https://github.com/xd-ai/name-entity-finder.git
cd name-entity-finder
poetry install
```

Now we need to download the spaCy language model:
```
poetry shell
python3 -m spacy download en_core_web_sm
```

The app is now ready to be run:
```
python3 app.py
```

![Alt Text](https://i.imgur.com/Url97h4.png)
