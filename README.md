<img src="assets\logo.png" />
<br/>


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![LinkedIn][linkedin-shield]][linkedin-url-two]
<br>

![alt='discord bot'](https://img.icons8.com/dusk/64/000000/discord-logo.png)

[contributors-shield]: https://img.shields.io/github/forks/JayP09/discfactbot?color=%23555&label=Fork&style=for-the-badge
[contributors-url]: https://github.com/JayP09/discfactbot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JayP09/discfactbot?label=CONTRIBUTORS&style=for-the-badge
[forks-url]: https://github.com/JayP09/discfactbot/network/members
[stars-shield]: https://img.shields.io/github/stars/JayP09/discfactbot?color=Blue&style=for-the-badge
[stars-url]: https://github.com/JayP09/discfactbot/stargazers
[issues-shield]: https://img.shields.io/github/issues/JayP09/discfactbot?color=Yellow&style=for-the-badge
[issues-url]: https://github.com/JayP09/discfactbot/issues
[license-shield]: https://img.shields.io/github/license/JayP09/discfactbot?color=green&style=for-the-badge
[license-url]: https://github.com/JayP09/discfactbot/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dhruv-khara-9190ab1aa/
[linkedin-url-two]: https://www.linkedin.com/in/jay-panchal-12565719a
[product-screenshot]: images/screenshot.png


## Add to your server!

[![Uptime Robot status](https://img.shields.io/uptimerobot/status/m779430970-e7fbeac99e0f5b24c277880c.svg)](https://stats.uptimerobot.com/WPBJjHp26) &nbsp;
[![Uptime Robot ratio](https://img.shields.io/uptimerobot/ratio/m779430970-e7fbeac99e0f5b24c277880c.svg)](https://stats.uptimerobot.com/WPBJjHp26)

<a href="https://discord.com/api/oauth2/authorize?client_id=808695542501736479&permissions=8&scope=bot"><img src="assets/add_to_discord.png" width="300"/></a>

## Description

TragicSimp is a discord bot that can send memes, facts, jokes, quotes and track user stats. This bot has levelling system which rank user based on their commands in a channel created by Bot.

## Features

```
Here are just listed some of the various commands of the bot.
```
---
- **Setup Commands :**
  - `pls setup` - Use this command when you add a bot to your server for first time. This command create text_channel where you can send commands for a meme, fact, quote, joke. This command also create certain roles for levelling system.
  - `pls prefix prefix` - This command change prefix for commands . default prefix is `pls `.
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
 ---
- **Quotes Commands :**
  - `pls quote` - sends a random Quote from [Favqs](https://favqs.com/).
  - `pls quote category` - sends a random Quote from category list.`categary`=`MOTIVATION`,`inspiration`,`inspire`, `motivational`,`productive`
  - `pls quote qotd` - sends a quote of the Day form Favqs API.
---
- **Meme Commands :**
  - `pls meme` - sends a random Meme from a database. In this Database we have collected a top meme of week from [reddit](https://www.reddit.com/dev/api) API
  - `pls meme pagename` - sends a Meme from Page list.`Pages`= `funny`, `dankmemes`, `memes`, `teenagers`, `Chodi`, `DsyncTV`, `cursedcomments`, `holdup`,
                     `SaimanSays/`, `wholesomememes`, `IndianMeyMeys`, `indiameme`, `desimemes`, `Tinder`,
                     `2meirl4meirl`,
                     `ComedyCemetery`, `terriblefacebookmemes`
  - `meme pagename` - sends a Meme from user specified page name.
---
- **Levelling System Commands :**
  - `pls rank` - sends your rank based on command you have sent in a channel created by Bot.
  - `pls learderboard` - sends a leaderboard of top 10 user in a server with the highest level.
---

see full list of documented commands by using the `pls help` command

## How does it work ?

  
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
  
## Libraries Used 

- **pymongo :**
  >PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. This documentation attempts to explain everything you need to know to use PyMongo.

- **Praw :**
  >PRAW, an acronym for “Python Reddit API Wrapper”, is a Python package that allows for simple access to Reddit’s API. PRAW aims to be easy to use and internally follows all of Reddit’s API rules. With PRAW there’s no need to introduce sleep calls in your code. Give your client an appropriate user agent and you’re set.

- **Re :**
  >This module provides regular expression matching operations similar to those found in Perl.

- **Random :**
  >This module implements pseudo-random number generators for various distributions.

- **Discord.py :**
  >A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.

- **Requests :**
  >The requests library is the de facto standard for making HTTP requests in Python

  
## Contributing 

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

##Contributors


## If you liked our work considering giving it a 🌟.

   

  
  
