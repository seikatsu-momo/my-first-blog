from django import forms

'''
class KensakuForm(forms.Form):
    Primary_Item = forms.CharField(label='大項目')
    Tertiary_Item = forms.CharField(label='中項目')
    Item_No = forms.IntegerField(label='ガイドラインNO')
    Check_Item=forms.CharField(label='チェック項目')
    GL_importance=forms.CharField(label='重要度')
    M_GL_importance=forms.CharField(label='宮城県重要度')
    Test_Item=forms.CharField(label='検査項目')
    Pic_need=forms.CharField(label='写真')
    Shoken_No=forms.CharField(label='所見NO')
    Shoken_Str=forms.CharField(label='所見文章')
    Shoken_terms=forms.CharField(label='条件')
    Water_terms1=forms.CharField(label='水質条件')
    Handan1=forms.CharField(label='判断表示1')
    Judge1=forms.CharField(label='判定1')
    Water_terms2=forms.CharField(label='水質条件2')
    Handan2=forms.CharField(label='判断表示2')
    Judge2=forms.CharField(label='判定2')
    Tokutan=forms.IntegerField(label='特単')
    Tandoku=forms.IntegerField(label='単独')
    Gapei=forms.IntegerField(label='合併')
    Shoken_No08=forms.CharField(label='旧所見NO')
    Shoken_Str08=forms.CharField(label='旧所見文章')
'''
    
class FindForm(forms.Form):
        find=forms.CharField(label='所見文章検索（スペースを入れると２つまで検索可能）',required=False,\
                             widget=forms.TextInput(attrs={'class':'form-control'}))
        
        find2=forms.CharField(label='条件文章検索（スペースを入れると２つまで検索可能）',required=False,\
                             widget=forms.TextInput(attrs={'class':'form-control'}))
        
class Katasiki_FindForm(forms.Form):
        K_find=forms.CharField(label='メーカー検索',required=False,\
                             widget=forms.TextInput(attrs={'class':'form-control'}))