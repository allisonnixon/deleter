# deleter

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)

Lightweight Discord selfbot that deletes your sent messages after an X amount of time

## Configuration

Both the `DISCORD_TOKEN` and the `DELETE_AFTER_SECONDS` durations should be in .env

## Run

It is recommended that you run the project in a virtual environment

```bash
git clone https://codeberg.org/alli/deleter.git

cd deleter
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
```

Fill out .env and config, then

```bash
python bot.py
```

## Notice

Usage of this tool may get your Discord account terminated as it breaks the [Discord Terms of Service](https://discord.com/tos)