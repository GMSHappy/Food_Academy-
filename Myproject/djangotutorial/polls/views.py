from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Module


def index(request):
    latest_module_list = Module.objects.order_by("-start_date")[:5]  # Fix: use start_date
    context = {"latest_module_list": latest_module_list}
    return render(request, "polls/index.html", context)


def detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    return render(request, "polls/detail.html", {"module": module})


def results(request, module_id):
    response = "You're looking at the results of module %s."
    return HttpResponse(response % module_id)


def vote(request, module_id):
    return HttpResponse("You're voting on module %s." % module_id)
