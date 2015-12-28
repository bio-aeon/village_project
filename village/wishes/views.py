import json

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .factories import draw_text_service_factory, social_service_factory
from .forms import TodoForm


def todo(request):
    if request.method == 'POST':
        return post_todo(request)
    else:
        return get_todo(request)


def get_todo(request):
    form = TodoForm()
    return render(request, "wishes/todo.html", {'form': form})


def post_todo(request):
    social_type = request.GET.get('type', 'fb')
    if social_type not in ('fb', 'vk'):
        return HttpResponse(json.dumps({'detail': 'Invalid social type'}),
                            content_type='application/json', status=400)

    form = TodoForm(request.POST)
    if form.is_valid():
        text_lines = [form.cleaned_data['aim{}'.format(i)] for i in range(1, 6)]
        image_name = draw_text_service_factory(social_type).generate_image(text_lines)
        proto = 'https://' if request.is_secure() else 'http://'
        image_url = '{proto}{host}{media_url}{image_name}'.format(proto=proto,
                                                                  host=request.get_host(),
                                                                  media_url=settings.MEDIA_URL,
                                                                  image_name=image_name)

        redirect_url = social_service_factory(social_type).get_redirect_url(image_url)
        return HttpResponse(json.dumps({'redirect_url': redirect_url}),
                            content_type='application/json', status=201)
    else:
        errors = {key: form.errors[key][0] for key in form.errors}
        return HttpResponse(json.dumps({'errors': errors}),
                            content_type='application/json', status=400)
