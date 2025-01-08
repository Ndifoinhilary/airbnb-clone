from math import ceil

from django.core.paginator import Paginator
from django.shortcuts import render

from rooms.models import Room


# Create your views here.



def all_rooms(request):
    page_num = request.GET.get('page', 1)
    page = int(page_num)
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.page(page)
    context = {'page': rooms, }
    return render(request, 'rooms/home.html', context)