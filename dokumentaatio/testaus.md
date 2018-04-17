# Tee testi raportti

Aja kaikki testit kansiosta otm-harjoitustyo/slack-bot

` py.test --cov-report html --cov=application test/ `

# Katso testi raportti

` chromium-browser htmlcov/index.html `

# Aja testit ja tulosta terminaaliin

` py.test --cov-report term-missing --cov=application test/ `