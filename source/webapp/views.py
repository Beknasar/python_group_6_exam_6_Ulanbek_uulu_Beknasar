from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import GuestBook, STATUS_CHOICES

from django.http import HttpResponseNotAllowed
#from .forms import

def index_view(request):
    data = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={'guest_book': data})


def create_guest_view(request):
    if request.method == 'GET':
        form = guestForm()
        return render(request, 'guest_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        #print(request.POST)
        form = guestForm(data=request.POST)
        # date = request.POST.get('date')
        # if date == '':
        #     date = None
        if form.is_valid():
            guest = guest.objects.create(
                title=form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                status = form.cleaned_data['status'],
                guest_deadline = form.cleaned_data['guest_deadline'])

        return redirect('guest_view', pk=guest.pk)
    else:
        return HttpResponseNotAllowed(
            permitted_methods=['GET', 'POST'])

def update_view(request, pk):
    guest = get_object_or_404(guest, pk=pk)
    if request.method == "GET":
        form = guestForm(initial={
            'title': guest.title,
            'description': guest.description,
            'guest_deadline': guest.guest_deadline,
            'status': guest.status
        })
        return render(request, 'guest_update.html', context={
            'form': form,
            'guest': guest
        })
    elif request.method == "POST":
       form = GuestForm(data=request.POST)
       if form.is_valid():
            guest.title = form.cleaned_data['title']
            guest.description = form.cleaned_data['description']
            guest.status = form.cleaned_data['status']
            guest.guest_deadline = form.cleaned_data['guest_deadline']
            guest.save()
            return redirect('guest_view', pk=guest.pk)
       else:
            return render(request, 'guest_update.html', context={
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