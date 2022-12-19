from django.contrib import admin

from testApp.models import TestObj, OtherTest
# Register your models here.

admin.site.register(TestObj)
admin.site.register(OtherTest)
