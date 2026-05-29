from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist


def home(request):
    return render(request, 'cribbage/home.html')


def about(request):
    return render(request, 'cribbage/about.html')


def rules(request):
    return render(request, 'cribbage/rules.html')


def news_index(request):
    return render(request, 'cribbage/news_index.html')


def news_detail(request, slug):
    template = f'cribbage/news/{slug}.html'
    try:
        return render(request, template)
    except TemplateDoesNotExist:
        raise Http404("No such bulletin.")


def events(request):
    return render(request, 'cribbage/events.html')


def membership_apply(request):
    return render(request, 'cribbage/membership_apply.html')


def scoring_calculator(request):
    return render(request, 'cribbage/scoring_calculator.html')


def contact(request):
    return render(request, 'cribbage/contact.html')
