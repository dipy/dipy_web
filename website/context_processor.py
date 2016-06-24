from .models import WebsiteSection, DocumentationLink


def nav_pages_processor(request):
    pages = WebsiteSection.objects.filter(section_type="page",
                                          show_in_nav=True)
    all_doc_displayed = DocumentationLink.objects.filter(displayed=True)
    return {'pages_in_nav': pages, 'all_doc_displayed': all_doc_displayed}
