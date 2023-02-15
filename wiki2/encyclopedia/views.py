from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_md_to_html(md):
    s = Markdown(md)
    return s


def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    else:
            