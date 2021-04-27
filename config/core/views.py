from django.shortcuts import render


def testme(request):
    return render(request, 'base.html')
