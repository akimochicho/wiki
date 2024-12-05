from django.shortcuts import render
from encyclopedia import urls
from . import util
from django import forms

def index(request):
    print("went through index method")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request, name):
    print("went through title method")
    return render(request, "encyclopedia/entry_page.html",{
        "title": util.title_change(name),
        "name": util.get_entry(name), 
    })
def search(request):
    # Check if method is POST
    if request.method == "GET":
        query = request.GET['q']
        print("passed through find method")
        return render(request, "encyclopedia/search_page.html", {
            "queries": util.search_entry(query)
        }) 
