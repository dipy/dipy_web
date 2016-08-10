from django.conf import settings

from .models import WebsiteSection, DocumentationLink


def nav_pages_processor(request):
    pages = WebsiteSection.objects.filter(section_type="page",
                                          show_in_nav=True)
    all_doc_displayed = DocumentationLink.objects.filter(displayed=True)
    return {'pages_in_nav': pages, 'all_doc_displayed': all_doc_displayed}


def google_analytics_processor(request):
    tracking_id = settings.GOOGLE_ANALYTICS_TRACKING_ID
    tracking_code = """<script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', '%s', 'auto');
      ga('send', 'pageview');

    </script>""" % (tracking_id,)
    return {'google_analytics': tracking_code}
