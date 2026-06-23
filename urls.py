from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('usertable/', views.usertable, name='usertable'),
    path('signup_submit/',views.signup_submit,name='signup_submit'),
    path('update_view/',views.update_view,name='update_view'),
    path('update_submit/<int:id>',views.update_submit,name='update_submit'),
    path('update_submit_data/<int:id>',views.update_submit_data,name='update_submit_data'),
    path('delete_data/<int:id>',views.delete_data,name='delete_data'),
    path('search_bar/',views.search_bar,name='search_bar'),
    path('search_data/',views.search_data,name='search_data'),

]