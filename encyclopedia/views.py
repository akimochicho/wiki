from django.shortcuts import render

from . import util

from flask import Flask, render_template 
 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request, name):
    return render(request, "encyclopedia/entry_page.html",{
        "title": util.title_change(name),
        "name": util.get_entry(name), 
    })
def search(request, name):
    return render(request, "encyclopedia/search_page.html", {
        "queries": util.search_entries(name),
    })
