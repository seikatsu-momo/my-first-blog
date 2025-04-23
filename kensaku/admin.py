from django.contrib import admin
#from models import Post
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from .models import Kensaku

# Register your models here.
class KensakuResource(resources.ModelResource):
    class Meta:
        model = Kensaku
        fields = ('id','Primary_Item','Tertiary_Item','Item_No','Check_Item','GL_importance',\
                  'M_GL_importance','Test_Item','Pic_need','Shoken_No','Shoken_Str',\
                  'Shoken_terms','Water_terms1','Handan1','Judge1','Water_terms2',\
                  'Handan2','Judge2','Tokutan','Tandoku','Gapei','Shoken_No08',\
                  'Shoken_Str08')
        import_id_fields = ['id']

resource_class = KensakuResource    


class GuestAdmin(ImportExportActionModelAdmin):
    list_display = (
                    'id','Primary_Item','Tertiary_Item','Item_No','Check_Item','GL_importance',\
                  'M_GL_importance','Test_Item','Pic_need','Shoken_No','Shoken_Str',\
                  'Shoken_terms','Water_terms1','Handan1','Judge1','Water_terms2',\
                  'Handan2','Judge2','Tokutan','Tandoku','Gapei','Shoken_No08',\
                  'Shoken_Str08')
    
    formats = [base_formats.CSV,\
               base_formats.XLS,\
               base_formats.XLSX]


admin.site.register(Kensaku,GuestAdmin)