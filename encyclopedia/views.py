from django.shortcuts import render, redirect
from encyclopedia import urls
from . import util
from django import forms
from django.http import HttpResponse
from django.contrib import messages
import ctypes
def index(request):
    print("went through index method")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request, name):
    print("went through title method")
    if request.method == "POST":
        title = request.POST['t']
        content = request.POST['c']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry_page.html", {
            "title": util.title_change(title),
            "content": util.get_entry(title),  
        })
    elif name not in util.list_entries():
        return error(request)
    else:
        return render(request, "encyclopedia/entry_page.html",{
            "title": util.title_change(name),
            "content": util.get_entry(name), 
        })
def search(request):
    # Check if method is POST
    if request.method == "GET":
        query = request.GET['q']
        print("passed through find method")
        store = util.search_entry(query, 0)
        substring = util.substring_check(query)
        if len(store) > 1 or substring == "true": 
            return render(request, "encyclopedia/search_page.html", {
                "queries": util.search_entry(query, 0),
                "title": "Similar pages containing " + "'" + query + "'",
            }) 
        elif len(store) == 0:
            return render(request, "encyclopedia/search_page.html", {
                "queries": util.search_entry(query, 0),
                "title": "No results to show for " + "'" + query + "'"
            })
        else:
            return render(request, "encyclopedia/entry_page.html", {
                "title": util.title_change(store[0]),
                "content": util.get_entry(store[0]), 
            }) 
def create(request):
    return render(request, "encyclopedia/new_page.html",{})
def add(request):
    if request.method == "POST":
        title = request.POST['t']
        content = request.POST['c']
        store = util.search_entry(title, 2)
        content = "<h1>" + title + "</h1>" + content
        print("passed through add method", title, content, store)
        if store == "true":
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry_page.html", {
                "title": title,
                "content": content, 
            }) 
        else:
            return render(request, "encyclopedia/new_page.html",{
                "error": "'" + title + "'" +" is taken",
            })
            # prompt()
            # return HttpResponse(request, "encyclopedia/entry_page.html", {})
        # return render(request, "encyclopedia/new_page.html",{})
def edit(request):
    if request.method == "GET":
        title = request.GET['t']
        return render(request, "encyclopedia/edit_page.html", {
            "title": util.title_change(title),
            "content": util.get_entry(title),  
        })
def random(request):
    import random
    entry = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry_page.html",{
        "title": util.title_change(entry),
        "content": util.get_entry(entry), 
    })
def error(request):
     return render(request, "encyclopedia/error_page.html",{})