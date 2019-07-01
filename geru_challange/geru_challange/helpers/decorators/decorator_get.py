from pyramid.response import Response

def get_check(function):
    def wrapper(fuction, request):
        if request.method=='GET':
            return function(request)
        else:
            return Response(status_code=403, text='Only GET method')

    return wrapper