from django.shortcuts import render,redirect,get_object_or_404
from .models import SummerClothes
from .forms import UpdateClothForm
# Create your views here.

def cloth_view(request):
    clothes = SummerClothes.objects.order_by('name')
    context = {
        'clothes':clothes
    }
    return render(request,'summer_cloth/summercloth.html',context=context)

def update_cloth(request, pk):
    cloth_instance = get_object_or_404(SummerClothes, pk=pk)

    if request.method == 'POST':
        form = UpdateClothForm(request.POST, request.FILES, instance=cloth_instance)
        if form.is_valid():
            form.save()
            return redirect('clothes')
    else:
        form = UpdateClothForm(instance=cloth_instance)

        return render(request, 'summer_cloth/update_summer_cloth.html', {'form': form,'cloth':cloth_instance})

def delete_cloth(request, pk):
    cloth_instance = get_object_or_404(SummerClothes, pk=pk)

    if request.method == 'POST':
        cloth_instance.delete()
        return redirect('clothes')

    return render(request, 'summer_cloth/delete.html', {'cloth':cloth_instance})

def about_cloth(request,pk):
    cloth = SummerClothes.objects.get(pk=pk)
    context = {
        'cloth':cloth,
    }
    return render(request,'summer_cloth/aboutsummercloth.html',context=context)