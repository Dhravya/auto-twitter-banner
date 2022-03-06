import requests
from os import environ as env
import io

import dotenv
import tweepy
from PIL import Image, ImageDraw

dotenv.load_dotenv()


class ProfileBanner:
    def __init__(self):
        self.client = self.__login()
        self.FIRST_IMAGE_COORDS = (600, 400)
        self.IMAGE_DIA = 75

    def __login(self):
        auth = tweepy.OAuthHandler(env["CONSUMER_KEY"], env["CONSUMER_SECRET"])
        auth.set_access_token(env["ACCESS_TOKEN"], env["ACCESS_TOKEN_SECRET"])
        api = tweepy.API(auth)
        api.verify_credentials()
        return api

    def __get_latest_followers_images(self) -> list[io.BytesIO]:
        latest_followers = self.client.get_followers(
            user_id=env.get("USER_ID"), count=5
        )
        images = []

        for follower in latest_followers:
            response = requests.get(follower.profile_image_url)
            images.append(io.BytesIO(response.content))
        return images

    def image_factory(self, savepath: str = None) -> Image:
        """
        Pastes the image onto the template
        """
        template = Image.open("template.png")
        images = self.__get_latest_followers_images()
        for i, image in enumerate(images):
            image = Image.open(image)
            image = image.resize((self.IMAGE_DIA, self.IMAGE_DIA))

            # Make image circle
            mask = Image.new("L", (self.IMAGE_DIA, self.IMAGE_DIA), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, self.IMAGE_DIA, self.IMAGE_DIA), fill=255)
            image.putalpha(mask)

            # Paste the image onto the template
            template.paste(
                image,
                (
                    self.FIRST_IMAGE_COORDS[0] + (i * self.IMAGE_DIA),
                    self.FIRST_IMAGE_COORDS[1],
                ),
                image,
            )

        if savepath:
            template.save(savepath)
        return template


if __name__ == "__main__":
    banner = ProfileBanner()
    banner.image_factory(savepath="profile_banner.png")
