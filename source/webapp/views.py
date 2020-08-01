from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import GuestBook

from django.http import HttpResponseNotAllowed
from .forms import GuestForm

def index_view(request):
    data = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={'guest_book': data})


def create_guest_view(request):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'guest_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest = GuestBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'])
            return redirect('index')
        else:
            return render(request, 'guest_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(
            permitted_methods=['GET', 'POST'])

def update_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestForm(initial={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
            'status': guest.status
        })
        return render(request, 'guest_edit.html', context={
            'form': form,
            'guest': guest
        })
    elif request.method == "POST":
       form = GuestForm(data=request.POST)
       if form.is_valid():
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('index')
       else:
            return render(request, 'guest_edit.html', context={
                'guest': guest,
                'form': form
            })

    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def delete_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')