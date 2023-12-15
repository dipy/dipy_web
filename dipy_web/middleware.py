virtual_hosts = {
    "workshop.dipy.org": "workshop.urls",
    "deprecated.docs.dipy.org": "website.urls",
}

class VirtualHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # let's configure the root urlconf
        host = request.get_host()
        request.urlconf = virtual_hosts.get(host, 'website.urls')
        # order matters!
        response = self.get_response(request)
        return response
