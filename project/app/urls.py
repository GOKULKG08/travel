from . import views


from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    # path('add/',views.addittion,name='addition'),
    # path('sub/',views.contact,name='contact'),
    # path('divi/',views.detail,name='detail'),
    # path('mul/',views.thanks,name='thanks'),
]
