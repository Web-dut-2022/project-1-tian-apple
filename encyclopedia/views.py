import random
import markdown
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    title = request.GET.get("q")
    Entry =util.get_entry(title)
    if Entry == None:
        return HttpResponseNotFound("Not Found")
    else: return render(request, "encyclopedia/display.html", {
        "searchname":title,
        "Entry":markdown.markdown(Entry)
    })

def random_entry(request):
    list=util.list_entries();
    r = random.randint(0,len(list)-1)
    Entry=util.get_entry(list[r])
    return render(request, "encyclopedia/display.html", {
        "searchname":"random",
        "Entry":markdown.markdown(Entry)
    })
