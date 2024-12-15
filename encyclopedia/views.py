from django.shortcuts import render, redirect
from encyclopedia import urls
from . import util

def index(request): #index page
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    if request.method == "POST": #editing page
        title = request.POST['t']
        content = request.POST['c']
        util.save_entry(title, content)
        if content.isspace() or content == "":
            return render(request, "encyclopedia/edit_page.html",{
            "title": util.title_change(title),
            "error": "Content is empty",
            })
        else:
            return render(request, "encyclopedia/entry_page.html", {
                "title": util.title_change(title),
                "content": util.get_entry(title),  
            })
    else: #for url search
        if util.title_change(name) == "None":  #url error
            return error(request)
        else: #redirect to existing entry
            return render(request, "encyclopedia/entry_page.html",{
                "title": util.title_change(name),
                "content": util.get_entry(name), 
            })

def search(request):
    # Check if method is POST
    if request.method == "GET":
        query = request.GET['q']
        store = util.search_entry(query, 0)
        substring = util.substring_check(query)
        if len(store) > 1 or substring == "true":  #contains substring 
            return render(request, "encyclopedia/search_page.html", {
                "queries": util.search_entry(query, 0),
                "title": "Pages containing " + "'" + query + "'",
            }) 
        elif len(store) == 0: #no results
            return render(request, "encyclopedia/search_page.html", {
                "queries": util.search_entry(query, 0),
                "title": "No results to show for " + "'" + query + "'"
            })
        else: #show entry page
            return render(request, "encyclopedia/entry_page.html", {
                "title": util.title_change(store[0]),
                "content": util.get_entry(store[0]), 
            }) 

def create(request):
    if request.method == "POST": #creates new page
        title = request.POST['t']
        content = request.POST['c']
        store = util.search_entry(title, 2)
        if store == "true":
            if title.isspace() or title == "":
                return render(request, "encyclopedia/new_page.html",{
                "t_error": "Title is empty",
                })
            elif content.isspace() or content == "":
                return render(request, "encyclopedia/new_page.html",{
                "c_error": "Content is empty",
                })
            else: #save entry, redirects to entry page
                content = "<h1>" + title + "</h1>" + content #uniform with sample entries
                util.save_entry(title, content)
                return render(request, "encyclopedia/entry_page.html", {
                    "title": title,
                    "content": content, 
                }) 
        else:
            return render(request, "encyclopedia/new_page.html",{
                "t_error": "'" + title + "'" +" is taken",
            })
    else:
      return render(request, "encyclopedia/new_page.html",{})
         
def edit(request): #after clicking edit button
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