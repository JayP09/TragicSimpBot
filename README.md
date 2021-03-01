<img src="https://github.com/JayP09/TragicSimpBot/blob/main/assets/logo.png" align="center" />
<br/>

---

<p align="center">
  <a href="https://github.com/JayP09/TragicSimpBot/graphs/contributors">
    <img src="https://img.shields.io/github/forks/JayP09/TragicSimpBot?color=blue&label=contributors&style=for-the-badge" alt="contributors">
  </a>
  <a href="https://github.com/JayP09/TragicSimpBot/network/members">
     <img alt="Forks" src="https://img.shields.io/github/forks/JayP09/TragicSimpBot?color=red&label=Forks&style=for-the-badge">
  </a>
  <a href="https://github.com/JayP09/TragicSimpBot/stargazers">
    <img alt="Stars" src="https://img.shields.io/github/stars/JayP09/discfactbot?color=Blue&style=for-the-badge">
  </a>
  <a href="https://github.com/JayP09/TragicSimpBot/blob/main/LICENSE">
     <img src="https://img.shields.io/github/license/JayP09/discfactbot?color=green&style=for-the-badge" alt="discord.py">
  </a>
  <a href="https://www.linkedin.com/in/jay-panchal-12565719a">
    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn">
  </a>
  <a href="https://www.linkedin.com/in/dhruv-khara-9190ab1aa/">
    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn">
  </a>
</p>

---
## Add to your server!

[![Uptime Robot status](https://img.shields.io/uptimerobot/status/m779430970-e7fbeac99e0f5b24c277880c.svg)](https://stats.uptimerobot.com/WPBJjHp26) &nbsp;
[![Uptime Robot ratio](https://img.shields.io/uptimerobot/ratio/m779430970-e7fbeac99e0f5b24c277880c.svg)](https://stats.uptimerobot.com/WPBJjHp26)

<a href="https://discord.com/api/oauth2/authorize?client_id=808695542501736479&permissions=8&scope=bot"><img src="assets/add_to_discord.png" width="300"/></a>

---
## Description

#### TragicSimp is a discord bot that can send memes, facts, jokes, quotes and track user stats. This bot has leveling system which rank user based on their commands in a channel created by Bot.

---

## Setup your own bot and database
Read [setup.md](https://github.com/JayP09/discfactbot/blob/main/setup.md) for more information! 

---
## Features

```
Here are list of the various commands of the bot.
```
---
- **Setup Commands :**
  - `pls setup` - Use this command when you add a bot to your server for first time. This command create text_channel where you can send commands for a meme, fact, quote, joke. This command also create certain roles for levelling system.
  - `pls prefix prefix` - This command change prefix for commands . default prefix is `pls `.
   <br>
  <img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plssetup.gif" width="400">                           
  <img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plsprefix.gif" width="365">
---
- **Joke Commands :**
  - `pls joke` - sends a random joke from [JokeAPI](https://v2.jokeapi.dev/).
  - `pls joke programming` - sends a joke on programming from JokeAPI
  - `pls joke misc` - sends misc joke from JokeAPI
  - `pls joke dark` - sends a dark joke from JokeAPI
  - `pls joke pun` - sends pun joke from JokeAPI
  - `pls joke spooky` - sends a spooky joke from JokeAPI
  - `pls joke christmas` - sends a christmas joke from JokeAPI
  - `pls joke dadjoke` - sends a random dadjoke from [icanhazdadjoke](https://icanhazdadjoke.com/)
   <p align="center"><img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plsjoke.gif" width="400"></p>
--- 
- **Facts Commands :**
  - `pls fact` - sends a random fact from [Uselessfacts](https://uselessfacts.jsph.pl/) API.
  - `pls fact number` - sends random number fact from [Numbersapi](http://numbersapi.com/#42).
  - `pls fact number` - sends fact for specific Number for Example:`pls fact 23` will send fact on number 23.
  - `pls fact date` - sends fact for specific Date for Example:`pls fact 06/09` will send fact on 9 june. format for date is `mm/dd`.
  - `pls fact dog` - sends a random Dog fact from [Some Random Api](https://some-random-api.ml/)
  - `pls fact cat` - sends a random Cat fact from Some Random Api
  - `pls fact panda` - sends a random Panda fact from Some Random Api
  - `pls fact fox` - sends a random Fox fact from Some Random Api
  - `pls fact bird` - sends a random Bird fact from Some Random Api
  - `pls fact koala` - sends a random koala fact from Some Random Api
    <p align="center"><img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plsfact.gif" width="400"></p>
---
- **Quotes Commands :**
  - `pls quote` - sends a random Quote from [Favqs](https://favqs.com/).
  - `pls quote category` - sends a random Quote from category list.`categary`=`MOTIVATION`,`inspiration`,`inspire`, `motivational`,`productive`
  - `pls quote qotd` - sends a quote of the Day form Favqs API.
    <p align="center"><img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plsquote.gif" width="400"></p>
---
- **Meme Commands :**
  - `pls meme` - sends a random Meme from a database. In this Database we have collected a top meme of week from [reddit](https://www.reddit.com/dev/api) API
  - `pls meme pagename` - sends a Meme from Page list.`Pages`= `funny`, `dankmemes`, `memes`, `teenagers`, `Chodi`, `DsyncTV`, `cursedcomments`, `holdup`,
                     `SaimanSays/`, `wholesomememes`, `IndianMeyMeys`, `indiameme`, `desimemes`, `Tinder`,
                     `2meirl4meirl`,
                     `ComedyCemetery`, `terriblefacebookmemes`
  - `meme pagename` - sends a Meme from user specified page name.
    <p align="center"><img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plsmeme.gif" width="400"></p>
---
- **Leveling System Commands :**
  - `pls rank` - sends your rank based on command you have sent in a channel created by Bot.
  - `pls learderboard` - sends a leaderboard of top 10 user in a server with the highest level.
    <p align="center"><img align="center" src="https://github.com/JayP09/discfactbot/blob/main/assets/plsrank.gif" width="400"></p>
---

see full list of documented commands by using the `pls help` command

## How does it work ?
we are using the discord.py library. This Discord.py library revolves around the concept of the event. An event is something you listen to and respond to an event. Discord.py is an asynchronous library so things are done with callbacks. the callback is a function that is called when something else happens. 
For Example: when the user types the command pls fact then in discord bot will receive an event about it then the bot responds to it with fact.When you add this bot to your server and you type pls setup command then it will create a text channel and certain roles for the levelling system.

### how does fact, joke, quote work ?
When the user types the command `pls fact`or `pls joke`or `pls quote` then the tragicsimp bot fetches the facts or joke from API and it creates an embed message then the bot sends that message to the user.

### how does meme work ?
When the user type command `pls meme` then the tragicsimp bot fetches the meme from the MongoDB database and it creates embed message and send it to the user. For a meme, we are using a database because fetching from the API takes some time to return a response as compared to the database. In the database, we are storing the top memes of the week. Every week bot deletes old memes and fetches new top memes of the week, adds them to the database. We have programmed the bot in such a way that its probability of repetition of the meme is increasing on every `pls meme` command.

### how does levelling system work ?
When the user type command for a joke, fact, quote, or meme bot will increase their XP based on that XP bot will calculate the level of the user. When the user will reach levels 5,10,15,20 then the bot will assign a certain role to a user. Based on their level and XP user rank is decided.

---  
## API Used

- **Joke :**
  - [JokeApi]( https://v2.jokeapi.dev/)
  - [icanhazdadjoke](https://icanhazdadjoke.com/)

- **Facts :**
  - [Useless fact API]( https://uselessfacts.jsph.pl/)
  - [numbersapi](http://numbersapi.com/)
  - [Some random api](https://some-random-api.ml/)
  
- **Quotes :**
  - [FavQs](https://favqs.com/)
  
- **Meme :**
  - [Reddit API]( https://www.reddit.com/dev/api)
  
---
## Libraries Used 

- **pymongo :**
  >PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. This documentation attempts to explain everything you need to know to use PyMongo.

- **Praw :**
  >PRAW, an acronym for “Python Reddit API Wrapper”, is a Python package that allows for simple access to Reddit’s API. PRAW aims to be easy to use and internally follows all of Reddit’s API rules. With PRAW there’s no need to introduce sleep calls in your code. Give your client an appropriate user agent and you’re set.

- **Re :**
  >This module provides regular expression matching operations similar to those found in Perl.

- **Random :**
  >This module implements pseudo-random number generators for various distributions.

- **[Discord.py]() :**
  >A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.This discord libraryy revolves around the concept of event.

- **Requests :**
  >The requests library is the de facto standard for making HTTP requests in Python

---
## Contributing 

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch ``` git checkout -b feature/AmazingFeature```
3. Commit your Changes ``` git commit -m 'Add some AmazingFeature'```
4. Push to the Branch ``` git push origin feature/AmazingFeature```
5. Open a Pull Request

---
## Contributors
people who already contributed to TragicSimpBot
<a href="https://github.com/JayP09/TragicSimpBot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=JayP09/TragicSimpBot" />
</a>

---
## If you liked our work considering giving it a 🌟.
![](https://media.giphy.com/media/1n3LPr8tsptiIaFUhF/giphy.gif)
