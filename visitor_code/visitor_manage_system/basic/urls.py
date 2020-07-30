from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),

    # path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),




    path('host/',views.host,name='host'),
    # path('host/<str:pk>',views.hostdynamic,name='hostdynamic'),
    path('create_host/',views.createhost,name='createhost'),
    path('update_host/<str:id>',views.updateHost,name='updatehost'),
    path('delete_host/<str:pk>',views.deleteHost,name='deletehost'),


    path('visitor/',views.visitor,name='visitor'),
    path('create_visitor/',views.createvisitor,name='createvisitor'),
    path('update_visitor/<str:pk>',views.updatevisitor,name='updatevisitor'),
    path('delete_visitor/<str:pk>',views.deletevisitor,name='deletevisitor'),


    path('visitentry/',views.visitdetails,name='visitdetails'),

    path('eventvisitor/',views.eventvisitor,name='eventvisitor'),

    path('events/',views.events,name= 'events'),
    path('create_events/',views.createevent,name='createevent'),
    path('update_events/<str:pk>',views.updateevent,name='updateevent'),
    path('delete_event/<str:pk>',views.deleteevent,name='deleteevent'),


    path('user/',views.userpage,name='userpage'),

    path('account',views.accountsettings,name='account'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="basic/reset_password.html"),name="password_reset"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="basic/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="basic/password_reset_form.html"),name="password_reset_confirm"),
    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="basic/password_reset_done.html"),name="password_reset_complete")
   

]