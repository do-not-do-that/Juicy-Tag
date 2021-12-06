from django.shortcuts import render

# Create your views here.
from django.views import generic

class Juicy_main(generic.TemplateView):
    def get(self, request, *args, **kwars):
        template_name = 'juicy_main/index.html'
        return render(request, template_name)