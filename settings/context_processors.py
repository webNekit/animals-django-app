from .models import SiteSettings

def site_settings(request):
    settings = SiteSettings.get_instance()
    return {'site_settings': settings}