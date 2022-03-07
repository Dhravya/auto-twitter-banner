<div align="center">
<h1 align="center">Auto twitter banner</h1>

<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg" /><br>
<br>
Automatically updates the twitter banner every few seconds with follower profile pics on it
<img src="https://us-east-1.tixte.net/uploads/img.dhravya.dev/t-generated.png" alt="Auto twitter banner">
</div>

***

### Installation
```
git clone https://github.com/Dhravya/auto-twitter-banner.git
cd auto-twitter-banner
pip install -r requirements.txt
```

### Usage

First, you need your developer tokens from twitter:
- Go to https://developer.twitter.com/en/portal/
- Create an app, and get your keys and tokens 
- Make a `.env` file and fill it up according to `.env.example`
- Go to your app settings -> User authentication settings -> Toggle on OAuth 1.0a, and in the OAuth 1.0a Settings section, select Read and write

Make sure it says read and write access here, something like this
![Here's how it should look](https://us-east-1.tixte.net/uploads/img.dhravya.dev/l0gwfrg8s0a.png)

You might need to make your own banner and figure out the position where you need to paste the images and just change the `FIRST_IMAGE_COORDS` and `IMAGE_DIA` constants

```
python main.py
```

### Contributing
All contributors are welcome!
- Open an issue
- Assign yourself
- fork and send a PR

### License
This project is licensed under the mit license
### Show your support
Leave a ⭐ if you like this project

***
Readme made with 💖 using [README Generator by Dhravya Shah](https://github.com/Dhravya/readme-generator)