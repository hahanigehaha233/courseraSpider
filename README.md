# Coursera Spider
Base on Python scrapy

##How to run

---
###Clone this repo
```
git clone https://github.com/hahanigehaha233/courseraSpider
```

###Create vritual env
```
cd courseraSpider
python -m venv
source /venv/bin/activate
pip install -r requirements.txt
```
###Init DataBase
Make sure you already have MySQL database

you can change the connection info in `/courseraSpider/config.py`


```
python initdb.py
```




