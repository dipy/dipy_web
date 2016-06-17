from .models import WebsiteSection


def nav_pages_processor(request):
    pages = WebsiteSection.objects.filter(section_type="page",
                                          show_in_nav=True)
    return {'pages_in_nav': pages}
