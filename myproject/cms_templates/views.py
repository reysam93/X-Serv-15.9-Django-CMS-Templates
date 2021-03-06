from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Page
from django.template.loader import get_template
from django.template import Context


def isLogged(request):
    if request.user.is_authenticated():
        logged = "<br><br>Logged in as " + request.user.username +\
                ". <a href='/admin/logout/'>Logout</a><br>"
    else:
        logged = "<br><br>Not logged. <a href='/admin/login/'>Login</a><br>"
    return logged


def getContent(resource):
    try:
        page = Page.objects.get(name=resource)
        return page.page
    except Page.DoesNotExist:
        return ""


def withTemplates(request, resource):
    template = get_template('index.html')
    logged = isLogged(request)
    text = getContent(resource)
    if text == "":
        return HttpResponseNotFound("Page not found" + logged)
    c = Context({'logged': logged, 'text': text})
    render = template.render(c)
    return HttpResponse(render)


def processCmsRequest(request, resource):
    logged = isLogged(request)
    if request.method == 'GET':
        content = getContent(resource)
        if content == "":
            return HttpResponseNotFound("Page not found" + logged)
        else:
            return HttpResponse(content + logged)
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            try:
                newPage = Page.objects.get(name=resource)
                newPage.page = request.body
            except Page.DoesNotExist:
                newPage = Page(name = resource, page = request.body)
            newPage.save()
            return HttpResponse("Added to the list")
        else:
            return HttpResponse("Couldn't add to the list" + logged)
    else:
        return HttpResponse(status=403)
