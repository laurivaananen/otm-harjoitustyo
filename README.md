# Slack botti

Kurssille Ohjelmistotekniikan menetelmät.

# Dokumentaatio 

[Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Testaus](/dokumentaatio/testaus.md)

# Ohjelman asentaminen ja käyttäminen

Tämä ohjelma on ohjelmoitu Pythonilla versio 3.6.3

Tarkista oma python versio komennolla `python -V` tai `python3 -V`

Ohjelman käyttämiseen tarvitset tunnukset Slack palveluun ja oman työtilan jonne voit asentaan tämän sovelluksen.

Avaa internet selain ja mene osoitteeseen https://slack.com/ ja paina nappia Create Workspace. Seuraa ohjeita kunnes olet tehnyt tunnkset sekä työtilan.

Lataa ja asenna ngrok ohjelma https://ngrok.com/

Käynnistä ngrok porttiin 3000

`lauri@ubuntu-pc:~$ ./ngrok http 3000`

![slack_08](/dokumentaatio/images/slack_08.png)

Kopioi annettu https osoite..ngrok.io

Kloonaa tämä git repository omalle koneelle. Siirry kansioon slack-bot ja tee uusi virtuaaliympäristö ja aktivoi se.

`lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$ python -m venv venv`

`lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$ source venv/bin/activate`

`(venv) lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$`

lataa vaadittavat lisäosat pip ohjelman avulla

`(venv) lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$ pip install -r requirements.txt`

Käynnistä ohjelma 

`(venv) lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$ python run.py`

Seuraavaksi tehdään uusi Slack App. https://api.slack.com/apps?new_app=1 Valitse haluamasi nimi ja työtila.

![slack_1](/dokumentaatio/slack_1.png)

Lisätään uusi Event Subscription. Liitä ngrok ohjelmasta saamasi https osoite request url kohtaan. Lisää Workspace Event message.channels . Huom! Jos käynnistät ngrok ohjelman uudestaan joudut liittämään sen luoman uuden https osoitteen tähän.

![slack_2](/dokumentaatio/slack_2.png)

Lisätään uusi Bot User. Valitse haluamasi nimi.

![slack_3](/dokumentaatio/slack_3.png)

Siirry OAuth & Permissions valikkoon. Paina Install App to Workspace nappia.

![slack_4](/dokumentaatio/slack_4.png)

Kopioi Bot User OAuth Access Token.

![slack_5](/dokumentaatio/slack_5.png)

Sulje ohjelma painamalla ctrl+c

Lisää Bot User OAuth Access Token ympäristömuuttujaksi

`(venv) lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$ export BOT_OAUTH=liitä-tähän-bot-user-oauth-token`

Käynistä ohjelma uudestaan 

`(venv) lauri@ubuntu-pc:~/slackbot/otm-harjoitustyo/slack-bot$ python run.py`

Kun kirjoitat valitsemaasi työtilan chattiin jotain niin botti vastaa sinulle

![slack_6](/dokumentaatio/slack_6.png)

Jos sinulla on hidas nettiyhteys niin botti saattaa vastata useamman kerran




# Ohjelman asentaminen ja käyttäminen

![slack_8](/dokumentaatio/images/slack_8.png)

Ohjelman käyttämiseen tarvitset tunnukset Slack palveluun ja oman työtilan jonne voit asentaan tämän sovelluksen.

Avaa internet selain ja mene osoitteeseen https://slack.com/ ja paina nappia Create Workspace. Seuraa ohjeita kunnes olet tehnyt tunnkset sekä työtilan.

Mene osoitteeseen https://api.slack.com/apps?new_app=1 ja valitse sovelluksellesi haluamasi nimi, ja valitse työtilaksi juuri tekemäsi työtila. Paina Create App.




