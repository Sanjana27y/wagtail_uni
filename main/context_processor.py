from .models import Menu

def menus(request):
    return {
        'menus': Menu.objects.all(),
    }
