from django.contrib.auth.handlers.modwsgi import groups_for_user
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groups = None

            if request.user.groups.exists():
                groups = request.user.groups.all()[0].name

            if groups in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page.")

        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        groups = None
        if request.user.groups.exists():
            groups = request.user.groups.all()[0].name

        if groups == 'customer':
            return redirect('user-page')

        if groups == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func