from django.shortcuts import render
from .forms import JuicyForm
# Create your views here.
from .models import JuicyBoard
from django.views import generic
from datetime import datetime, timedelta 

class Juicy_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'juicy_board/juicy_list.html'
        juicy_list = JuicyBoard.objects.all()
        
        juicy_list_no_end_Date = JuicyBoard.objects.all().filter(end_date__isnull=True, is_complete=0).order_by('priority')
        juicy_list_end_Date_non_complete = JuicyBoard.objects.all().filter(end_date__isnull=False, is_complete=0).order_by('priority')
        juicy_list_end_Date_complete = JuicyBoard.objects.all().filter(is_complete=1).order_by('end_date')
        
        today = datetime.now()
        close_end_day = []
        over_end_day = []
        
        for i in juicy_list_end_Date_non_complete:
            e_day = str(i.end_date).split("-")
            end_day = datetime(int(e_day[0]), int(e_day[1]), int(e_day[2]))
            if (end_day - today).days < -1: over_end_day.append(i.title)
            if (end_day - today).days >= -1 and (end_day - today).days < 3: close_end_day.append(i.title)
        return render(request, template_name, 
                      {"juicy_list_end_Date_non_complete": juicy_list_end_Date_non_complete, 
                       "juicy_list_end_Date_complete": juicy_list_end_Date_complete, 
                       "juicy_list_no_end_Date": juicy_list_no_end_Date, 
                       'close_end_day': close_end_day, 'over_end_day':over_end_day})
        
def check_post(request):
    template_name = 'juicy_board/juicy_board_success.html'
    
    if request.method == 'POST':
        if str(request.path).split('/board/')[1].split('/')[0] == "insert":
            form = JuicyForm(request.POST)

            if form.is_valid():
                message = "Juicy한 일정이 추가되었습니다."
                if len(request.POST.get('title')) < 1:
                    message = '제목이 너무 짧습니다. 1글자 이상 작성해주세요.'
                else:
                    juicy = form.save(commit=False)
                    juicy.juicy_save()

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
    form_class = JuicyForm
    template_name = "juicy_board/juicy_board_update.html"
    success_url = '/board/'
    
    def form_valid(self, form):
        form.save()
        return render(self.request, 'juicy_board/juicy_board_success.html',{"message":'Juicy한 일정을 업데이트 했습니다.'})
    
    
class Juicy_board_delete(generic.DeleteView):
    model = JuicyBoard
    success_url = '/board/'
    context_object_name = 'juicy_list'