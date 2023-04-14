from django.http.response import HttpResponse
from django.shortcuts import render
from .models import MenuItem
from .debugger import query_debugger
from django.http import Http404


def ping(request):
    return HttpResponse('pong')


@query_debugger
def list_menu_render(request, name=None):
    if name is not None:
        try:
            menu = MenuItem.objects.get(name__exact=name)
        except MenuItem.DoesNotExist:
            raise Http404('menu does not exist')
        menu_items = MenuItem.objects.filter(parent=menu.parent).prefetch_related('children')
    else:
        menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')
    items_json = {
        'menu_items': [i.to_json() for i in menu_items]
    }
    return render(request, 'list_menu.html', items_json)
