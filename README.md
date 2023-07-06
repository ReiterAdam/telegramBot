<a name="readme-top"></a>
<!-- ABOUT THE PROJECT -->
# TelegramBot


<p align="center">
  <img src="https://github.com/ReiterAdam/telegramBot/blob/main/images/hello.png">
</p>


   This Telegram bot, written in Python, serves as a versatile tool for accessing random information, currently related to:


### Formula 1

<p align="center">
  <img src="https://github.com/ReiterAdam/telegramBot/blob/main/images/f1.png">
</p>

### NASA's picture of the day


<p align="center">
  <img src="https://github.com/ReiterAdam/telegramBot/blob/main/images/nasa.png">
</p>

### delay of trains on my everyday commute. 


<p align="center">
  <img src="https://github.com/ReiterAdam/telegramBot/blob/main/images/trains.png">
</p>
   
   
   With the integration of the F1 and NASA APIs, the bot provides users with real-time informations on request. Additionally, the bot utilizes a web scraper to retrieve information regarding train delays, ensuring I am informed about any disruptions in train schedules every morning.






<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ReiterAdam/telegramBot.git
   ```
2. Install required packages
   ```sh
   cd telegramBot
   pip install -r requirements.txt
   ```
3. Get your Bot token here: https://core.telegram.org/bots#how-do-i-create-a-bot
4. Set BOT_TOKEN as environment variable:
   ```sh
   export BOT_TOKEN=your_token_value
   ```
5. Start bot
   ```sh
   python bot.py
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[hello-screenshot]: images/hello.png
[f1-screenshot]: images/f1.png
[trains-screenshot]: images/trains.png
[nasa-screenshot]: images/nasa.png
