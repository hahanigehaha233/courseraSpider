# Coursera Spider
Base on Python Scrapy

## How to run

---
### Clone this repo
```
$git clone https://github.com/hahanigehaha233/courseraSpider
```

### Create vritual env
```
$cd courseraSpider
$python -m venv
$source /venv/bin/activate
$pip install -r requirements.txt
```

### Init DataBase
Make sure you already have MySQL database

you can change the connection info in `/courseraSpider/config.py`


```
$cd ..
$python initdb.py
```

###Set IP Proxy and User-Agent(If necessary)
```
$cd courseraSpider
$python proxies.py
```

###Run Spider
```
$scrapy crawl getcourseid
$scrapy crawl getcoursedetail
$scrapy crawl getcoursefeedback

```


### Init table increment_field
```
$python initincrement.py
```

