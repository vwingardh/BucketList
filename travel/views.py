from django.shortcuts import render
from .forms import DestinationForm, NextDestination
from .models import Destination, Checkoff, Next
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings


def add_destination(request):
    submitted = False
    if request.user.is_authenticated:
        if request.method == "POST":
            form = DestinationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_destination?submitted=True')
        else:
            form = DestinationForm
            if 'submitted' in request.GET:
                submitted = True
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    return render(request, 'travel/add_destination.html', {'form':form, 'submitted':submitted})


def next_destination(request):
    submitted = False
    if request.method == "POST":
        next_form = NextDestination(request.POST)
        if next_form.is_valid():
            next = next_form.save(commit=False)
            next.save()
            return HttpResponseRedirect('/next_destination?submitted=True')
    else:
        next_form = NextDestination()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'travel/next_destination.html', {'next_form': next_form, 'submitted':submitted})

def next_filter(next):
    # Beach
    if next.adventure == 'beach' and next.climate == 'tropical' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='beach', climate='tropical', flight='short')
        return beach_list
    
    elif next.adventure == 'beach' and next.climate == 'tropical' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='beach', climate='tropical', flight='long')
        return beach_list

    elif next.adventure == 'beach' and next.climate == 'temperate' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='beach', climate='temperate', flight='long')
        return beach_list

    elif next.adventure == 'beach' and next.climate == 'temperate' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='beach', climate='temperate', flight='short')
        return beach_list

    elif next.adventure == 'beach' and next.climate == 'cold' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='beach', climate='cold', flight='short')
        return beach_list

    elif next.adventure == 'beach' and next.climate == 'cold' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='beach', climate='cold', flight='long')
        return beach_list
    # Diving
    elif next.adventure == 'diving' and next.climate == 'tropical' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='diving', climate='tropical', flight='short')
        return beach_list

    elif next.adventure == 'diving' and next.climate == 'tropical' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='diving', climate='tropical', flight='long')
        return beach_list
    
    elif next.adventure == 'diving' and next.climate == 'temperate' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='diving', climate='temperate', flight='long')
        return beach_list

    elif next.adventure == 'diving' and next.climate == 'temperate' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='diving', climate='temperate', flight='short')
        return beach_list

    elif next.adventure == 'diving' and next.climate == 'cold' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='diving', climate='cold', flight='short')
        return beach_list
    
    elif next.adventure == 'diving' and next.climate == 'cold' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='diving', climate='cold', flight='long')
        return beach_list
    # City
    elif next.adventure == 'city' and next.climate == 'tropical' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='city', climate='tropical', flight='short')
        return beach_list

    elif next.adventure == 'city' and next.climate == 'tropical' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='city', climate='tropical', flight='long')
        return beach_list

    elif next.adventure == 'city' and next.climate == 'temperate' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='city', climate='temperate', flight='long')
        return beach_list

    elif next.adventure == 'city' and next.climate == 'temperate' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='city', climate='temperate', flight='short')
        return beach_list

    elif next.adventure == 'city' and next.climate == 'cold' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='city', climate='cold', flight='short')
        return beach_list

    elif next.adventure == 'city' and next.climate == 'cold' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='city', climate='cold', flight='long')
        return beach_list
    # Hiking
    elif next.adventure == 'hiking' and next.climate == 'tropical' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='hiking', climate='tropical', flight='short')
        return beach_list

    elif next.adventure == 'hiking' and next.climate == 'tropical' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='hiking', climate='tropical', flight='long')
        return beach_list

    elif next.adventure == 'hiking' and next.climate == 'temperate' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='hiking', climate='temperate', flight='long')
        return beach_list

    elif next.adventure == 'hiking' and next.climate == 'temperate' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='hiking', climate='temperate', flight='short')
        return beach_list

    elif next.adventure == 'hiking' and next.climate == 'cold' and next.flight == 'short':
        beach_list = Destination.objects.filter(adventure='hiking', climate='cold', flight='short')
        return beach_list

    elif next.adventure == 'hiking' and next.climate == 'cold' and next.flight == 'long':
        beach_list = Destination.objects.filter(adventure='hiking', climate='cold', flight='long')
        return beach_list


def travel_home(request):
    destination_list = Destination.objects.all().order_by('city')
    checkoff_list = Checkoff.objects.all().order_by('city')
    form = NextDestination()
    if request.method == "POST":
        next_form = NextDestination(request.POST)
        if next_form.is_valid():
            next = next_form.save(commit=False)
            next.save()
            list = next_filter(next)
            return render(request, 'travel/next_destination.html', {'list':list})

    return render(request, 'travel/travel-home.html', {'destination_list': destination_list, 'checkoff_list': checkoff_list, 'form':form})


