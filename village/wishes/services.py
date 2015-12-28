import uuid
from urllib.parse import quote_plus

from PIL import Image, ImageFont, ImageDraw


class DrawTextService:
    def __init__(self, left_bias, top_bias, line_space,
                 source_image, font, font_size, font_color, media_root):
        self.left_bias = left_bias
        self.top_bias = top_bias
        self.line_space = line_space
        self.source_image = source_image
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.media_root = media_root

    def generate_image(self, text_lines):
        im = Image.open(self.source_image)
        draw = ImageDraw.Draw(im)
        true_font = ImageFont.truetype(self.font, self.font_size)
        top = self.top_bias
        for text_line in text_lines:
            draw.text((self.left_bias, top), text_line, font=true_font, fill=self.font_color)
            top += self.line_space

        new_image_name = '{}.jpg'.format(uuid.uuid4())
        im.save('{}/{}'.format(self.media_root, new_image_name), 'JPEG', quality=100)
        return new_image_name


class FacebookService:
    def __init__(self, app_id, title, text, url):
        self.app_id = app_id
        self.title = title
        self.text = text
        self.url = url

    def get_redirect_url(self, image_url):
        return ('https://www.facebook.com/dialog/feed?app_id={app_id}&display=popup'
                '&caption={title}&description={text}&link={url}&redirect_uri={url}'
                '&picture={image_url}').format(app_id=self.app_id, title=quote_plus(self.title),
                                               text=quote_plus(self.text), url=quote_plus(self.url),
                                               image_url=quote_plus(image_url))


class VkontakteService:
    def __init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def get_redirect_url(self, image_url):
        return ('http://vk.com/share.php?url={url}'
                '&title={title}&description={text}'
                '&image={image_url}').format(url=quote_plus(self.url), title=quote_plus(self.title),
                                             text=quote_plus(self.text),
                                             image_url=quote_plus(image_url))
