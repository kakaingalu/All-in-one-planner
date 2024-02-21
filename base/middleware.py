# base/middleware.py

from django.urls import reverse
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.utils.deprecation import MiddlewareMixin

class RestrictNormalToAdmin(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated:
                if not request.user.is_staff:
                    return self.render_custom_404(request)
            else:
                return self.render_custom_404(request)

    def render_custom_404(self, request):
        context = {}
        return HttpResponse(render_to_string('base/404.html', context), status=404)