from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# @login_required
# def index(request):
#     item_list = Item.objects.all()
#     context = {"item_list": item_list}
#     return render(request, 'index/index.html', context)

# @method_decorator(login_required, name="dispatch")
# class IndexView(View):
#     template_name = "index/index.html"

#     def get(self, request):
#         item_list = Item.objects.all()
#         context = {"item_list": item_list}
#         return render(request, self.template_name, context)

class IndexView(ListView):
    model = Item
    template_name = "index/index.html"
    context_object_name = "item_list"


# def about(request, id):
#     item = Item.objects.get(id=id)
#     context = {"item": item}
#     return render(request, "index/detail.html", context)


class ItemDetail(DetailView):
    model = Item
    context_object_name = "item"
    template_name = "index/detail.html"


def edit(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST':
        form.save()
        return redirect('index:index')
    context = {"form": form}
    return render(request, 'index/edit.html', context)


def delete(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index:index')
    context = {"item": item}
    return render(request, 'index/delete.html', context)


# def create(request):
#     form = ItemForm(request.POST or None)
#     if request.method == 'POST':
#         form.save()
#         return redirect("index:index")
#     context = {"form": form}
#     return render(request, 'index/create.html', context)

class CreateItem(CreateView):
    model = Item
    template_name = 'index/create.html'
    fields = ['item_name', 'item_desc', 'item_price', 'item_photo']
    success_url = reverse_lazy('index:index')
