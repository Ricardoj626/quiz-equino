from datetime import timezone

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Questionario
from .forms import *
# from .models





def nome_view(request):
    if request.method == 'POST':
        form = nomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print(post.nome)
            print(post.numero)
            saida = int(post.numero)
            return redirect('pergunta1', pk=saida)
    else:
        form = nomeForm()
    context = {
        'form': form,
    }
    return render(request, 'quiz/nome.html', context)


def pergunta1_view(request, pk):
    perguntas = Questionario.objects.all().order_by("-pontuacao")
    instance = get_object_or_404(Questionario, pk=pk)
    p1 = instance.pergunta_1
    print(instance.pergunta_1)
    print(request.method)
    if request.method == "POST":
        form = p1Form(request.POST, instance=instance)
        if form.is_valid():
            instance2 = form.save(commit=False)
            print('pergunta 1:',instance.pergunta_1)
            print('pergunta 1-2:',instance2.pergunta_1)
            if not p1:
                if int(instance2.pergunta_1) > 9:
                    instance.pontuacao+=int(instance2.pergunta_1)
            instance.save()

            return redirect('pergunta2', pk=instance.pk)
        return redirect('pergunta2', pk=instance.pk)
    else:
        # instance.pontuacao -= int(instance.pergunta_1)
        # instance.save()
        print(instance.pontuacao)
        print(instance.pergunta_1)
        form = p1Form(instance=instance)
        context = {
            "form": form,
            "perguntas": perguntas,
        }
    return render(request, 'quiz/pergunta1.html', context)

def pergunta2_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p2 = instance.pergunta_2

    if request.method == "POST":
        form = p2Form(request.POST, instance=instance)
        if form.is_valid():
            instance2 = form.save(commit=False)
            if not p2:
                if int(instance2.pergunta_2) > 9:
                    instance.pontuacao += int(instance2.pergunta_2)
            instance.save()
            return redirect('pergunta3', pk=instance.pk)          #######
        return redirect('pergunta2', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_2)
        instance.save()
        form = p2Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})

def pergunta3_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p3 = instance.pergunta_3
    if request.method == "POST":
        form = p3Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            print(instance.pergunta_3)

            if not p3:
                if int(instance2.pergunta_3) > 9:
                    instance.pontuacao += int(instance2.pergunta_3)
            instance.save()

            return redirect('pergunta4', pk=instance.pk)          #######
        return redirect('pergunta3', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_3)
        instance.save()
        form = p3Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})

def pergunta4_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p4 = instance.pergunta_4
    if request.method == "POST":
        form = p4Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            if not p4:
                if int(instance2.pergunta_4) > 9:
                    instance.pontuacao += int(instance2.pergunta_4) #######
            instance.save()

            return redirect('pergunta5', pk=instance.pk)          #######
        return redirect('pergunta4', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_4)
        instance.save()
        form = p4Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})


def pergunta5_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p5 = instance.pergunta_5
    if request.method == "POST":
        form = p5Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            if not p5:
                if int(instance2.pergunta_5) > 9:
                    instance.pontuacao += int(instance2.pergunta_5)
            instance.save()

            return redirect('pergunta6', pk=instance.pk)          #######
        return redirect('pergunta5', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_5)
        instance.save()
        form = p5Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})

def pergunta6_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p6 = instance.pergunta_6
    if request.method == "POST":
        form = p6Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            print(instance.pergunta_6)
            if not p6:#######
                if int(instance2.pergunta_6) > 9:
                    instance.pontuacao += int(instance2.pergunta_6)
            instance.save()


            return redirect('pergunta7', pk=instance.pk)          #######
        return redirect('pergunta6', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_6)
        instance.save()
        form = p6Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})


def pergunta7_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p7 = instance.pergunta_7
    if request.method == "POST":
        form = p7Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            print(instance.pergunta_7)
            if not p7:
                if int(instance2.pergunta_7) > 9:
                    instance.pontuacao += int(instance2.pergunta_7)
            instance.save()

            return redirect('pergunta8', pk=instance.pk)          #######
        return redirect('pergunta7', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_7)
        instance.save()
        form = p7Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})


def pergunta8_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p8 = instance.pergunta_8
    if request.method == "POST":
        form = p8Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            print(instance.pergunta_8)
            if not p8:
                if int(instance2.pergunta_9) > 9:
                    instance.pontuacao += int(instance2.pergunta_8)
            instance.save()
            #######

            return redirect('pergunta9', pk=instance.pk)          #######
        return redirect('pergunta8', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_8)
        instance.save()
        form = p8Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})


def pergunta9_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p9 = instance.pergunta_9
    if request.method == "POST":
        form = p9Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            if not p9:
                if int(instance2.pergunta_9) > 9:
                    instance.pontuacao += int(instance2.pergunta_9)
            instance.save()

            return redirect('pergunta10', pk=instance.pk)          #######
        return redirect('pergunta9', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_9)
        instance.save()
        form = p9Form(instance=instance)                          #######
    return render(request, 'quiz/pergunta1.html', {'form': form})


def pergunta10_view(request, pk):
    instance = get_object_or_404(Questionario, pk=pk)
    p10 = instance.pergunta_10
    if request.method == "POST":
        form = p10Form(request.POST, instance=instance)             #######
        if form.is_valid():
            instance2 = form.save(commit=False)
            if not p10:
                if int(instance2.pergunta_10) > 9:
                    instance.pontuacao += int(instance2.pergunta_10)
            instance.save()

            return redirect('pontuacao', pk=instance.pk)          #######
        return redirect('pergunta10', pk=instance.pk)              #######
    else:
        # instance.pontuacao -= int(instance.pergunta_10)
        instance.save()
        form = p10Form(instance=instance)
    return render(request, 'quiz/pergunta1.html', {'form': form})
