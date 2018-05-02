# Ohjelman asentaminen

Lataa tiedosto [slack_bot](https://github.com/laurivaananen/otm-harjoitustyo/releases/tag/viikko5)

Käynnistä ohjelma 

`(venv) lauri@ubuntu-pc:~$ ./slack_bot`

Lataa ja asenna ngrok ohjelma https://ngrok.com/

Käynnistä ngrok porttiin 3000

`lauri@ubuntu-pc:~$ ./ngrok http 3000`

![slack_8](/dokumentaatio/images/slack_8.png)

Seuraavaksi tehdään uusi Slack App.

Avaa internet selain ja mene osoitteeseen https://slack.com/ ja paina nappia Create Workspace. Seuraa ohjeita kunnes olet tehnyt tunnkset sekä työtilan.

Mene osoitteeseen https://api.slack.com/apps?new_app=1 ja valitse haluamasi nimi ja työtila.

![slack_10](/dokumentaatio/images/slack_10.png)

Paina Create App ja siirry valikosta kohtaan Event Subscriptions. Kopioi ngrok ohjelmasta saamasi osoite kohtaan Request URL. Tekstikentän päälle pitäisi ilmestyä teksti Verified. Jos siihen ilmestyi Your URL didn't respond with the value of the challenge parameter. Varmista että ohjelma on käynnissä.

HUOM! Ngrok ohjelman antama osoite muuttuu joka kerta kun käynnistät sen uudelleen.

![slack_9](dokumentaatio/images/slack_9.png)

Alempaa sivua löytyy osio Subscribe to Workspace Events. Paina Add Workspace Event ja valitse messages.channel

![slack_11](dokumentaatio/images/slack_11.png)]

Paina save changes ja siirry valikosta kohtaan Bot Users. Paina Add a Bot User. Valitse botille nimi ja paina Add Bot User.

![slack_12](/dokumentaatio/images/slack_12.png)

Siirry valikkoon Interactive Components. Kopioi ngrok ohjelmasta saamasi osoite kenttään Request URL ja lisää sen perään /component

![slack_18](/dokumentaatio/images/slack_18.png)

Paina Enable Interactive Components ja siirry OAuth & Permissions valikkoon. Valitse Select Permission Scopes valikosta kohta files:read 

![slack_13](/dokumentaatio/images/slack_13.png)

Paina Save Changes ja siirry sivua ylöspäin ja paina Install App to Workspace.

Lisätään tarvittavat OAuth tokenit.

![OAuth](/dokumentaatio/images/oauth.png)

# Ohjelman graafisen käyttöliittymän käyttäminen

## Tiedostojen lataaminen

Siirry siihen työympäristöön Slackissa mihin asensit botin. Kun jaat jonkun tiedoston niin botti vastaa viestillä, missä on tiedoston nimi ja nappi, missä lukee Download

![slack_17](/dokumentaatio/images/slack_17.png)

Jos painat nappia Download niin viesti päivittyy ja tiedosto latautuu kansioon slack-bot/downloads/

![slack_19](/dokumentaatio/images/slack_19.png)

Liian isojen tiedostojen lataaminen ei välttämättä onnistu. Jos sinun nettiyhteytesi on hidas, botti saattaa vastata useamman kerran.

## Botin automaattinen vastaaminen

Set bot triggers osiossa voit valita eri regular expression triggereitä botille ja sen vastauksia. Jos käyttäjän lähettämä viesti slackissa vastaa jotain triggeriä niin botti vastaa Response viestillä. Seuraavassa tapauksessa jos käyttäjä kirjoittaa `Hello` tai `hello` niin botti vastaa `World`.

![gui_0](/dokumentaatio/images/gui_0.png)

![extra_0](/dokumentaatio/images/extra_0.png)

List bot triggers osiossa on listaus kaikista triggereistä mitä olet tallentanut tietokantaan. Jos valitset niistä jonkun ja painat Delete Row se poistetaan tietokannasta.

![gui_1](/dokumentaatio/images/gui_1.png)