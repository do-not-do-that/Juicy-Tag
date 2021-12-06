from django.shortcuts import render

# Create your views here.
from .models import JuicyBoard
from django.views import generic

class Juicy_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'juicy_board/juicy_list.html'
        juicy_list = JuicyBoard.objects.all()
        return render(request, template_name, {"juicy_list":juicy_list})
    