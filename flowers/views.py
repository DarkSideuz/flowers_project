from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Type, Flower

# Barcha gullarni chiqarish
def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flower_list.html', {'flowers': flowers})

# Gullarni turlari bo'yicha chiqarish
def flowers_by_type(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    flowers = type_obj.flowers.all()
    return render(request, 'flowers_by_type.html', {'type': type_obj, 'flowers': flowers})

# Bitta gulni chiqarish
def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flower_detail.html', {'flower': flower})