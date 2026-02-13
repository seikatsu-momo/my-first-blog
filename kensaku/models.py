from django.conf import settings
from django.db import models
from django.utils import timezone


class Kensaku(models.Model):
    Primary_Item = models.CharField(max_length=200)
    Tertiary_Item = models.CharField(max_length=200)
    Item_No = models.IntegerField(blank=True,null=True)
    Check_Item=models.CharField(max_length=200)
    GL_importance=models.CharField(max_length=10)
    M_GL_importance=models.CharField(max_length=10)
    Test_Item=models.CharField(max_length=10)
    Pic_need=models.CharField(max_length=10)
    Shoken_No=models.CharField(max_length=10)
    Shoken_Str=models.CharField(max_length=50)
    Shoken_terms=models.CharField(max_length=200)
    Water_terms1=models.CharField(max_length=15)
    Handan1=models.CharField(max_length=10)
    Judge1=models.CharField(max_length=10)
    Water_terms2=models.CharField(max_length=15)
    Handan2=models.CharField(max_length=10)
    Judge2=models.CharField(max_length=10)
    Tokutan=models.IntegerField()
    Tandoku=models.IntegerField()
    Gapei=models.IntegerField()
    Shoken_No08=models.CharField(max_length=10)
    Shoken_Str08=models.CharField(max_length=50)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

'''
    def __str__(self):
        return self.id
'''
class Kensaku_Katasiki(models.Model):
    JLK_MEISYO = models.CharField(max_length=20)
    JLK_OEM_CD = models.CharField(max_length=20,null=True)
    JLK_SYORIMEI = models.CharField(max_length=50,null=True)
    JLK_SEINO = models.CharField(max_length=50)
    MAKER_NM = models.CharField(max_length=30)
    JLK_KATASIKI_LINK = models.URLField(blank=True,null=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

