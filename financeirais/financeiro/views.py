from django.shortcuts import render

from .models import Movimentacao


def images_view(request):
    post = Movimentacao.objects.exclude(status=0)
    return render(request, "comprovante.html", {'post': post})