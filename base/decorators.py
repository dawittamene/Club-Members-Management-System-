from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('newsuserview')
        else: 
            return view_func(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request,*args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page!')
        return wrapper_function
    return decorator

def admin_only(view_functon):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'user':
                return  redirect('newsuserview')

            if group == 'admin':
                return view_functon(request, *args, **kwargs)
        else:
            return  redirect('newsuserview')
    return wrapper_function
        