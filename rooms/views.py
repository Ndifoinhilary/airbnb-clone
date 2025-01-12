from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from rooms import models as rooms_models
from rooms.models import Room


# Create your views here.



# def all_rooms(request):
#     page_num = request.GET.get('page', 1)
#     page = int(page_num)
#     room_list = Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     rooms = paginator.page(page)
#     context = {'page': rooms, }
#     return render(request, 'rooms/room_list.html', context)


class HomeView(ListView):
    """
    HomeView
    """
    model = rooms_models.Room
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = 'rooms'



def room_details(request, pk):
    room = get_object_or_404(rooms_models.Room, pk=pk)
    amenities = room.amenities.all()
    context = {
        'room': room,
        'amenities': amenities,
    }
    return  render(request, 'rooms/room_details.html', context)