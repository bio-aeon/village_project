from django.conf import settings
from .services import DrawTextService, FacebookService, VkontakteService


def draw_text_service_factory(type):
    params = settings.TEXT_DRAWING
    source_image = '{}/{}'.format(settings.RESOURCES_ROOT, params[type]['source_image'])
    font = '{}/fonts/{}'.format(settings.RESOURCES_ROOT, params['font'])
    return DrawTextService(params[type]['left_bias'], params[type]['top_bias'],
                           params[type]['line_space'], source_image, font,
                           params['font_size'], params['font_color'], settings.MEDIA_ROOT)


def social_service_factory(type):
    if type == 'fb':
        return FacebookService(settings.FACEBOOK_APP_ID, settings.SHARE_TITLE,
                               settings.SHARE_TEXT, settings.SHARE_URL)
    else:
        return VkontakteService(settings.SHARE_TITLE, settings.SHARE_TEXT, settings.SHARE_URL)
