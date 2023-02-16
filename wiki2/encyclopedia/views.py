from django.shortcuts import render
from markdown2 import Markdown
from . import util


def convert_md_to_html(md):
    if util.get_entry(md) == None:
        return None
    else:
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
                md = title
        res = convert_md_to_html(title)
        return render(request, "encyclopedia/converting.html", {
            "title": md,
            "res": res
        })


def search(request):
    if request.method == "POST":
        look_for = request.POST["q"]
        res = convert_md_to_html(look_for)
        if res:            
            return render(request, "encyclopedia/converting.html", {
                "title": res,
                "res": res
            })
        else:
            all_possible = []
            all_md = util.list_entries()
            for md in all_md:
                if look_for.lower() in md.lower():
                    all_possible.append(md)
            if all_possible:
                return render(request, "encyclopedia/search.html", {
                "entries": all_possible
            })
            else:
                return render(request, "encyclopedia/error.html")



                


