from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Kensaku,Kensaku_Katasiki
from .forms import FindForm,Katasiki_FindForm

# Create your views here.
def index(request):
    return render(request,'kensaku/index.html')
=======
from .models import Kensaku
from .forms import FindForm

# Create your views here.
def index(request):
    return render(request,'/index.html')
>>>>>>> a337fb2a7f9fdba6e83f32597198a25237f90b9c

def find(request):
    if(request.method == 'POST'):
        form=FindForm(request.POST)
        find=request.POST['find']
        val=find.split()
        find_list = len(val)
<<<<<<< HEAD
        find2=request.POST['find2']
        val2=find2.split()
        find2_list=len(val2)
        if (find_list == 1 and find2_list ==0):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list == 2 and find2_list ==0):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0]).filter(Shoken_Str__contains=val[1])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list ==0 and find2_list == 1):
            data=Kensaku.objects.filter(Shoken_terms__contains=val2[0])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list ==0 and find2_list == 2 ):
            data=Kensaku.objects.filter(Shoken_terms__contains=val2[0]).filter(Shoken_terms__contains=val2[1])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list == 1 and find2_list == 1 ):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0]).filter(Shoken_terms__contains=val2[0])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list == 2 and find2_list == 1 ):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0]).filter(Shoken_Str__contains=val[1]).filter(Shoken_terms__contains=val2[0])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list == 1 and find2_list == 2 ):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0]).filter(Shoken_terms__contains=val2[0]).filter(Shoken_terms__contains=val2[1])
            msg='検索結果: ' + str(data.count()) + '件'
        elif (find_list == 2 and find2_list == 2 ):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0]).filter(Shoken_Str__contains=val[1]).filter(Shoken_terms__contains=val2[0]).filter(Shoken_terms__contains=val2[1])
            msg='検索結果: ' + str(data.count()) + '件'
        elif(find_list > 2 or find2_list>2):
=======
        if (find_list == 1):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0])
            msg='検索結果: ' + str(data.count()) + '件'
        elif(find_list==2):
            data=Kensaku.objects.filter(Shoken_Str__contains=val[0])\
                                .filter(Shoken_Str__contains=val[1])
            msg='検索結果: ' + str(data.count()) + '件'
        elif(find_list > 2):
>>>>>>> a337fb2a7f9fdba6e83f32597198a25237f90b9c
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

<<<<<<< HEAD
def katasiki_find(request):
    if(request.method == 'POST'):
        form=Katasiki_FindForm(request.POST)
        k_find=request.POST['K_find']
        val=k_find.split()
        k_find_list = len(val)
        if (k_find_list == 1):
            data=Kensaku_Katasiki.objects.filter(MAKER_NM__contains=val[0])
            msg='検索結果: ' + str(data.count()) + '件'
        else:
            data=Kensaku_Katasiki.objects.all()
            msg='検索結果: ' + str(data.count()) + '件'           
    else:
        msg='seach word...'
        form=Katasiki_FindForm()
        data=Kensaku_Katasiki.objects.all()
    params={
        'title':'検索エンジンWeb版',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'kensaku/k_find.html',params)
=======
>>>>>>> a337fb2a7f9fdba6e83f32597198a25237f90b9c
