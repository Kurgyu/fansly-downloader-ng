![Title Banner](https://i.imgur.com/mrbhd6y.png) ![Downloads](https://img.shields.io/github/downloads/Avnsx/fansly/total?color=0078d7&label=🔽%20Executable%20Downloads&style=flat-square) ![Stars](https://img.shields.io/github/stars/Avnsx/fansly?style=flat-square&label=⭐%20Stars&color=ffc83d)
## 
![UI Banner](https://i.imgur.com/jvpJQaJ.png)
## Description
On click code, to scrape your favorite fansly creators media content. After you've ran the code, it'll create a folder named ``CreatorName_fansly`` in the same directory you launched the code from. That folder will have two sub-folders called Pictures & Videos, which will contain the downloaded content sorted into them.
This is pretty useful for example; if you dislike the website theming and would like to view the media on your local machine instead. This code does not bypass any paywalls & no end user information is collected during usage.

## How To
1. If you have Python installed download the GitHub repository, else use the [Executable version](https://github.com/Avnsx/fansly/releases)
2. Make sure you have registered an account on fansly and are logged in with it in your browser or you'll not be able to get a authorization token from Developer Console.
3. Go to whatever creators account page and open your browsers developer console (Most often Key: F12)
4. Reload the website by using the rotating arrow symbol to the left of your browsers search bar(Key: F5), while the developer console is open. Now do the steps on the following picture:
5. ![GitHub Banner](https://i.imgur.com/X2L9XFo.png)
6. Now paste both of the strings - that were on the right side of ``authorization:`` & ``User-Agent:`` - which you just copied, as shown in the picture above. Into the configuration file (config.ini) and replace the two strings with their corresponding values. (1. ``[MyAccount]`` > ``Authorization_Token=`` paste the value for ``authorization:``; 2. ``[MyAccount]`` > ``User_Agent=`` paste the value for ``User-Agent:``.
7. Replace the value for ``[TargetedCreator]`` > ``Username=`` with whatever content creator you wish.
8. Save the ``config.ini`` file with the changes you've done to it, close it & then start up fansly scraper.

From now on, you'll only need to re-do step 7 for every future use case.

**Not enough content downloaded? Enable media previews.** (``Download_Media_Previews`` to ``True`` in the configuration file)

You can turn ``Open_Folder_When_Finished`` to ``False``; if you no longer wish the download folder to automatically open after code completion.

## Installation
You can just install the [Executable version](https://github.com/Avnsx/fansly/releases).
Else you'll need to install python (ticking pip in installer) and paste below in ``cmd.exe``.

	pip install requests loguru imagehash pillow

## Support
Dependant on how many people show me that they're liking the code by giving ⭐'s on this repo, I'll expand functionality & push more quality of life updates.
Would you like to help out more? Any crypto donations are welcome!

BTC: bc1q82n68gmdxwp8vld524q5s7wzk2ns54yr27flst

ETH: 0x645a734Db104B3EDc1FBBA3604F2A2D77AD3BDc5

## Disclaimer
"Fansly" or fansly.com is operated by Select Media LLC as stated on their "Contact" page. This code (Avnsx/fansly) isn't in any way affiliated with, sponsored by, or endorsed by Select Media LLC or "Fansly". The developer of this code is not responsible for the end users actions. Of course I've never even used this code myself ever before and haven't experienced its intended functionality on my local machine. This was written purely for educational purposes, in a entirely theoretical environment.

Written with python 3.9.7 for Windows 10, Version 21H1 Build 19043.1237
