from django.shortcuts import render
from .forms import JuicyForm
# Create your views here.
from .models import JuicyBoard
from django.views import generic

class Juicy_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'juicy_board/juicy_list.html'
        juicy_list = JuicyBoard.objects.all()
        return render(request, template_name, {"juicy_list":juicy_list})

def check_post(request):
    template_name = 'juicy_board/juicy_board_success.html'
    
    if request.method == 'POST':
        form = JuicyForm(request.POST)
        if form.is_valid():
            juicy = form.save(commit=False)
            juicy.juicy_save()
            message = "Juicy한 일정이 추가되었습니다."
            
            return render(request, template_name, {"message":message})
    else:
        
        template_name = 'juicy_board/juicy_board_insert.html'
        form = JuicyForm
        return render(request, template_name, {"form":form})
    