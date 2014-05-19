from functools import wraps
from flask import abort, url_for, redirect, request
from LoginUtils import encrypt_password,check_password


def secure_view(endpoint,check_function,http_response_code):
    '''
        secure a view function with a 
        function, only get the return 
        if the function returns true
        get HTTP_RESPONSE_CODE otherwise
    '''
    def decorator(view_func):
        @wraps(view_func)
        def _wrapper(self,*args,**kwargs):
            if not check_function(self,*args,**kwargs):
                return abort(http_response_code)
            return view_func(self,*args,**kwargs)
        return _wrapper
    return decorator


def redirect_to_login():
    return redirect(url_for('login',next=request.next))

def redirect_to_home():
    return redirect(url_for('index'))



