from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, 'index/index.html', context)


def about(request, id):
    item = Item.objects.get(id=id)
    context = {"item": item}
    return render(request, "index/detail.html", context)


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


def create(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect("index:index")
    context = {"form": form}
    return render(request, 'index/create.html', context)
