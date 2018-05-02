# Slack botti

Kurssille Ohjelmistotekniikan menetelmät.

Ohjelma helpottaa Slack palvelussa jaettujen tiedostojen lataamista omalle koneelle, sekä tarjoaa ominaisuuden omien komentojen tekemisen botille johon botti vastaa haluamallasi tavalla.

# Dokumentaatio 

[Käyttöohje](/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](/dokumentaatio/testaus.md)

[Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)

[Ohjelman asentaminen gitistä](/dokumentaatio/asentaminen.md)

# Releaset

[Viikko 5](https://github.com/laurivaananen/otm-harjoitustyo/releases/tag/viikko5)

[Viikko 6](https://github.com/laurivaananen/otm-harjoitustyo/releases/tag/viikko6)

# Komentorivitoiminnot

Asenna ohjelma ensiksi -> [Ohjelman asentaminen gitistä](/dokumentaatio/asentaminen.md)

## Checkstyle

Suorita Checkstyle. Virheilmoitukset tulostuvat terminaaliin.

` (venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ pycodestyle application/ --format='%(path)s %(row)d %(text)s' `

## Ohjelman testaus

Testikattavuusraportin generointi

` (venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ py.test --cov-report html --cov=application test/ `

Testikattavuusraporttia voi tarkastella avaamalla selaimella  tiedoston htmlcov/index.html

` (venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ chromium-browser htmlcov/index.html `

## Automaattisen dokumentaation generoiminen

Dokumentaatiota voi tarkastella avaamalla selaimella tiedoston slack_bot/_build/html/index.html

`~/otm-harjoitustyo/slack-bot$ chromium-browser _build/html/index.html`

Dokumentaation generoiminen

`~/otm-harjoitustyo/slack-bot$ make html`

## Suorituskelpoisen tiedoston tekeminen

` (venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot$ pyinstaller run.py -n slack_bot --onefile --windowed`

Jos sinulla tulee virhe tiedostoa tehdessä lataa ensiki oman python versiosi dev versio.
Esimerkiksi jos python versiosi on 3.6.3

`sudo apt install python3.6-dev`

Tiedosto rakentuun kansion dist sisälle.

Ohjelman suorittaminen:

` (venv) lauri@ubuntu-pc:~/otm-harjoitustyo/slack-bot/dist$ ./slack_bot `
