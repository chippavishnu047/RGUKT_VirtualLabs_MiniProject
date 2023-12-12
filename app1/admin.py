from django.contrib import admin

# Register your models here.
from .models import Student,QuesModel,res,Question,DBMS,Pyy,Py_res,DB_res
admin.site.register(Student)
admin.site.register(QuesModel)
admin.site.register(res)
admin.site.register(Question)
admin.site.register(DBMS)
admin.site.register(Pyy)
admin.site.register(Py_res)
admin.site.register(DB_res)