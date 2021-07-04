from math import ceil
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)    # 마지막 페이지 element를 이전 페이지에 표시
    rooms = paginator.page(int(page))
    return render(request, "rooms/home.html", {"page": rooms})