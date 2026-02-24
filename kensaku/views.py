from django.shortcuts import render
from django.http import HttpResponse
from .models import Kensaku,Kensaku_Katasiki
from .forms import FindForm,Katasiki_FindForm

# Create your views here.
def index(request):
    return render(request,'kensaku/index.html')

def find(request):
    if(request.method == 'POST'):
        form=FindForm(request.POST)
        find=request.POST['find']
        val=find.split()
        find_list = len(val)
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
            data=''
            msg='検索は２つまでです。'
        else:
            data=Kensaku.objects.all()
            msg='検索結果: ' + str(data.count()) + '件'           
    else:
        msg='検索件数'
        form=FindForm()
        data=Kensaku.objects.all()
    if request.GET.get("tokutan") == "1":
        data = Kensaku.objects.filter(Tokutan=1)
        msg = f'検索結果: {data.count()}件'
    params={
        'title':'検索エンジンWeb版',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'kensaku/find.html',params)
   

def katasiki_find(request):
    if(request.method == 'POST'):
        form=Katasiki_FindForm(request.POST)
        k_find=request.POST['K_find']
        val=k_find.split()
        k_find_list = len(val)
        k_find2=request.POST['K_find2']
        val2=k_find2.split()
        k_find_list2=len(val2)
        if (k_find_list == 1 and k_find_list2==0):
            data=Kensaku_Katasiki.objects.filter(MAKER_NM__contains=val[0]).order_by('MAKER_NM_INDEX','JLK_MEISYO')
            msg='検索結果: ' + str(data.count()) + '件'
        elif (k_find_list==0 and k_find_list2==1):
            data=Kensaku_Katasiki.objects.filter(JLK_MEISYO__contains=val2[0]).order_by('MAKER_NM_INDEX','JLK_MEISYO')
            msg='検索結果: ' + str(data.count()) + '件'
        elif (k_find_list==1 and k_find_list2==1):
            data=Kensaku_Katasiki.objects.filter(MAKER_NM__contains=val[0]).filter(JLK_MEISYO__contains=val2[0]).order_by('MAKER_NM_INDEX','JLK_MEISYO')
            msg='検索結果: ' + str(data.count()) + '件'
        else:
            data=Kensaku_Katasiki.objects.all().order_by('MAKER_NM_INDEX','JLK_MEISYO')
            msg='検索結果: ' + str(data.count()) + '件'           
    else:
        msg='検索件数'
        form=Katasiki_FindForm()
        data=Kensaku_Katasiki.objects.all().order_by('MAKER_NM_INDEX','JLK_MEISYO')
    params={
        'title':'検索エンジンWeb版',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'kensaku/k_find.html',params)