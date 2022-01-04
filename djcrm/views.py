from django.views import generic
from django.http import HttpResponse

class HomepageView(generic.TemplateView):
    template_name = 'pages/landing-page.html'