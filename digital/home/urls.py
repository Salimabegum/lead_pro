from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('Register/',views.register,name="Register"),
	path('walkins/',views.walkins,name="walkins"),
    path('Calling/',views.Calling,name="Calling"),
    path('Counselling/',views.Counselling,name="Counselling"),
    path('joining/',views.join,name="joining"),
    path('Students/',views.Students,name="Students"),
    # path('data_page/',views.data_page,name="data_page"),
    path('single_data/',views.single_data,name="single_data"),
    path('Calling1/',views.Calling1,name='Calling1'),
    path('Calling/',views.Calling,name='Calling'),
    path('Counselling1/',views.Counselling1,name='Counselling1'),
    path('update/<id>',views.update,name="update"),
    path('edit/<id>',views.edit,name="edit"),
    path('delete/<id>',views.destroy,name='delete'),
    path('current/',views.current,name='current'),
    # path('register_modelform/',views.register_modelform),   
    # path('COMPLETE/',views.status,name='COMPLETE'),
    # path('DELAY/',views.delay,name='DELAY'),
    # path('discontinue/',views.discontinue,name='discontinue'),
    # path('status/<id>',views.status,name='status'),
    # path('update1/<id>',views.update1,name='update1'),
    path('edit1/<id>',views.edit1,name='edit1'),   
    path('complete/<id>',views.complete,name='complete'),
    path('delay/<id>',views.delay,name='delay'),
    path('rejoin/<id>',views.rejoin,name='rejoin'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),

]