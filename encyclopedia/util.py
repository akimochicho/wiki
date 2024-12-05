import re
from . import views

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        for entry in list_entries():
            if entry.lower() == title.lower():
                f = default_storage.open(f"entries/{entry}.md")
                return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def title_change(title):
    for entry in list_entries():
        if entry.lower() == title.lower():
            return entry

def search_entry(query):
    output=[]
    broke= "false"
    # for i in range(len(query)):
    #     for j in range(i+1, len(query)+1):
    #         output.append(query[i:j])
    list_search=[]
    for k in range(len(query)):
        for l in range(k+1, len(query)+1):
            broke = "false"
            for entry in list_entries():
                if query == entry:
                    output.append(entry)
                    broke = "true"
                    break
                else:
                    for i in range(len(entry)):
                        broke = "false"
                        for j in range(i+1, len(entry)+1):
                            if entry[i:j] == query [k:l]:
                                output.append(entry)
                                broke = "true"
            if broke == "true":
                break
               
                    

            
    # for entry in list_entries():
    #     for i in range(len(entry)):
    #         for j in range(i+1, len(entry)+1):
    #             list_search.append(entry[i:j])
    #             for k in range(len(query)):
    #                 for l in range(k+1, len(query)+1):
    #                     if query[k:l] == entry[i:j]:
    #                         output.append(entry)
    #                         break
    # for k in output:
    #     for filename in list_entries():
    #         if k in filename:
    #           list_search.append()
    return output