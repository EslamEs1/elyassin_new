
from datetime import date
from main.models import Settings


def global_view(request):
    links = Settings.objects.last()
    return {'links': links}
