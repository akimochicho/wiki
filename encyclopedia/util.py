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

    
def search_entry(query, check):
    output=[]
    available = "true"
    substring ="false"
    for entry in list_entries():
        if query.lower() == entry.lower() :
            if entry in output:
                pass
            else:
                output.append(entry)
            if check == 2:
                available = "false"
                return available
            break
        else:
            for i in range(len(entry)):
                for j in range(i+1, len(entry)+1):
                    if entry[i:j].lower() == query:
                        substring = "true"
                        if entry in output:
                            pass
                        else:
                            output.append(entry)
                        break
    if substring == "true" and check == 1:
        return substring
    elif check == 2:
        return available
    else: 
        return output
def substring_check(query):
    return search_entry(query, 1)
