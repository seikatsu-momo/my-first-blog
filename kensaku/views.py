from django.shortcuts import render
from django.http import HttpResponse
from .models import Kensaku
from .forms import FindForm

# Create your views here.
def index(request):
    return render(request,'/index.html')

def find(request):
    if(request.method == 'POST'):
        form=FindForm(request.POST)
        find=request.POST['find']
        val=find.split()
        find_list = len(val)
        if (find_list == 1):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0])
            msg='検索結果: ' + str(data.count()) + '件'
        elif(find_list==2):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0])\
                                .filter(Shoken_Str__contains=val[1])
            msg='検索結果: ' + str(data.count()) + '件'
        elif(find_list > 2):
            data=''
            msg='検索は２つまでです。'
        else:
            data=Kensaku.objects.all()
            msg='検索結果: ' + str(data.count()) + '件'           
    else:
        msg='seach word...'
        form=FindForm()
        data=Kensaku.objects.all()
    params={
        'title':'検索エンジンWeb版',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'kensaku/find.html',params)

