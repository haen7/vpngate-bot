# [vpngate-bot](https://vpngate.net) on [Heroku](https://www.heroku.com/)

I used [this](https://github.com/Eldinnie/ptb-heroku-skeleton) python app to create a vpngate Bot on Heroku that fetches openvpn profiles (OVPN) from [vpngate.net](https://vpngate.net)

## How to deploy:
* Create a heroku app: `$ heroku create <appname>`
* Get a token from [@BotFather](https://t.me/botfather) and pass it to the app by setting an environment variable (TOKEN).
* Assign a name for app by setting an environment variable (APP_NAME).
* Set webhook for telegram bot: `https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://{APP_NAME}.herokuapp.com/{TOKEN}`
* Check webhook: `https://api.telegram.org/bot{TOKEN}/getWebhookInfo`
* Deploy to heroku.
