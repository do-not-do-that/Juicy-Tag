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

class Juicy_board_detail(generic.DetailView):
    model = JuicyBoard
    template_name = 'juicy_board/juicy_board_detail.html'
    context_object_name = 'juicy_list'
    
class Juicy_board_update(generic.UpdateView):
    model = JuicyBoard
    fields= {'title','content'}
    template_name = "juicy_board/juicy_board_update.html"
    success_url = '/board/'
    
    def form_valid(self, form):
        form.save()
        return render(self.request, 'juicy_board/juicy_board_success.html',{"message":'Juicy한 일정을 업데이트 했습니다.'})
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)