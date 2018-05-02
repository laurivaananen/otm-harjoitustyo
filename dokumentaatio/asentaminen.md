# Ohjelman asentaminen omalle tietokoneelle

Kloonaa tämä git omalle koneellesi.

Varmista, että käytössä on python 3.6.3

```
lauri@ubuntu-pc:~$ python -V
Python 3.6.3
```
tai

```
lauri@ubuntu-pc:~$ python3.6 -V
Python 3.6.3
```

Tee uusi virtuaaliympäristö ja aktivoi se

```
lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ python -m venv venv
lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ source venv/bin/activate
(venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ 
```

Lataa tarvittavat paketit

`(venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ pip install -r requirements.txt`
