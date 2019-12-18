from django.http import HttpResponse


def new(request):
    return HttpResponse("Hey your new News!")


def edit(request):
    return HttpResponse("Hey you can edit News!")


def lock(request):
    return HttpResponse("Hey your can lock News!")


def add(request,item_id):
    if item_id:
        return HttpResponse('Add new news with item id:' + str(item_id))


def processing(request,mode,item_id):
    if mode == 'add':
        if item_id:
            return HttpResponse('Add new articles with item id:' + str(item_id))
    elif mode == 'delete':
        if item_id:
            return HttpResponse('Delete articles with item id:' + str(item_id))
    else: return HttpResponse('Error chouse correct mode')


def return_code(request,code):
    if code:
        return HttpResponse('Article code:' + str(code))