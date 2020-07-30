from django.http import HttpResponse
from django.shortcuts import redirect,render


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                # context={'form':'Your are not authorized','k':False}
                # return render(request,'basic/user.html',context)
                return HttpResponse('Your are not autorized')
            return view_func(request,*args, **kwargs)
        return wrapper_func
    return decorator



def admin_only(view_func):
    def wrapper_func(request,*args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'entryperson':
            return redirect('/')
        if group == 'host':
            return redirect('/')
        if group== 'admin':
            return view_func(request,*args, **kwargs)
    return wrapper_func
