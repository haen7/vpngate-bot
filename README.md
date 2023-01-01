# [vpngate-bot](https://vpngate.net) on [render](https://render.com)

I used [this](https://github.com/Eldinnie/ptb-heroku-skeleton) python app to create a vpngate Bot on render.com that fetches openvpn profiles (OVPN) from [vpngate.net](https://vpngate.net)

## How to deploy:
* Create a render Web Service.
* Get a token from [@BotFather](https://t.me/botfather) and pass it to the app by setting an environment variable (TOKEN).
* Assign a name for app by setting an environment variable (APP_NAME).
* Set Build Command: `$ pip install -r requirements.txt`
* Set Start Command: `$ python vpngateBot.py`
* Set webhook for telegram bot: `https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://{APP_NAME}.onrender.com/{TOKEN}`
* Check webhook: `https://api.telegram.org/bot{TOKEN}/getWebhookInfo`
* Deploy to render.com.
