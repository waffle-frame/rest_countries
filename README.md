# Rest Countries

---

External dependencies:

- Redis 5.x.x +


## Installation

---

### Redis

Quick installation of `redis`:

```bash
apt update && apt upgrade   # Update and install system dependencies
apt-get install redis       # Install redis
```

Check `redis` version:

```bash
redis-cli
```

More information can be found at the link: https://redis.io/

### Setup env

Install python dependencies:

```bash
pip3 install -r requirements.txt
```

Create env:

```bash
python3 -m venv env
```

Apply virtual environment:

```bash
source env/bin/activate
```


Fill in the environment variables `.env` according to the template from the file `.env-example`
Or user command:

```bash
cp .env-example .env
```

Run application:

```bash
python3 run app.py
```
