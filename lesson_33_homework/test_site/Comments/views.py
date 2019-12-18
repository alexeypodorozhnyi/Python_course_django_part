from django.http import HttpResponse


def new(request):
    return HttpResponse("Hey your new News!")


def edit(request):
    return HttpResponse("Hey you can edit News!")


def lock(request):
    return HttpResponse("Hey your can lock News!")


def processing(request,mode,item_id):
    if mode == 'add':
        if item_id:
            return HttpResponse('Add new comments with item id:' + str(item_id))
    elif mode == 'delete':
        if item_id:
            return HttpResponse('Delete comments with item id:' + str(item_id))
    else: return HttpResponse('Error news correct mode')

def phone_check(request,phone):
    if phone:
        return HttpResponse('Phone:' + phone)