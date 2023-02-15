from django.shortcuts import render
from markdown2 import Markdown
from . import util


def convert_md_to_html(md):
    res = util.get_entry(md)
    s = Markdown()   
    return s.convert(res)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    else:
        all_md = util.list_entries()
        for md in all_md:
            if title.lower() in md.lower():
                title = md
        res = convert_md_to_html(title)
        return render(request, "encyclopedia/converting.html", {
            "title": title,
            "res": res
        })

            