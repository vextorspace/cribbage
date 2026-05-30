from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist


# Authoritative news catalogue. Each entry corresponds to a template file
# at templates/cribbage/news/<slug>.html. Ordered newest-first; the index
# foregrounds the scandal arc per canon, with the rise-era stories sitting
# below in chronological retreat.
NEWS_STORIES = [
    {
        'slug': 'thornenberg-suspensions',
        'date_display': '20 May MMXXVI',
        'category': 'Statement from the Director',
        'title': 'Executive Director Thornenberg Issues Provisional Suspensions; “Stop, Cease, Desist”',
        'excerpt': (
            'Director Thornenberg, in a statement read at the close of Wednesday’s '
            'Council session, suspended Mr. Cullen and Ms. Lake from all sanctioned '
            'play pending the final determination of the Tribunal in Case '
            'ICA-T-2026-014.'
        ),
    },
    {
        'slug': 'lake-revival-staged',
        'date_display': '8 April MMXXVI',
        'category': 'Tribunal',
        'title': 'Lake’s Dead-Horse Revival Now Believed Staged; Cullen Allegedly Administered Kicks',
        'excerpt': (
            'Sworn statements filed with the Tribunal allege that the celebrated 2019 '
            'revival was preceded by the administration of multiple kicks by Mr. '
            'Cullen. The IWCCA has commenced a review of the Double Lotus Shuffle’s '
            'historical designation.'
        ),
    },
    {
        'slug': 'veterinary-linguist-thirty-one',
        'date_display': '22 March MMXXVI',
        'category': 'Tribunal Testimony',
        'title': 'Veterinary Linguist Confirms Horses Cannot Pronounce “Thirty-One”',
        'excerpt': (
            'Professor Helga Eikenboom, of the Royal Veterinary College, established a '
            'confirmed numerical ceiling of three in equine subjects and presented the '
            'phonetic findings now annexed to the Tribunal’s working file.'
        ),
    },
    {
        'slug': 'tribunal-opens-equine-inquiry',
        'date_display': '15 February MMXXVI',
        'category': 'Tribunal',
        'title': 'Tribunal Opens Inquiry into Equine Participation in Sanctioned Play',
        'excerpt': (
            'The International Cribbage Association announced Friday that its '
            'Tribunal has formally opened proceedings under the case number '
            'ICA-T-2026-014. The principal parties have been notified.'
        ),
    },
]


def home(request):
    # The home page features the three most recent bulletins.
    return render(request, 'cribbage/home.html', {
        'featured_stories': NEWS_STORIES[:3],
    })


def about(request):
    return render(request, 'cribbage/about.html')


def rules(request):
    return render(request, 'cribbage/rules.html')


def news_index(request):
    return render(request, 'cribbage/news_index.html', {
        'stories': NEWS_STORIES,
    })


def news_detail(request, slug):
    story = next((s for s in NEWS_STORIES if s['slug'] == slug), None)
    if story is None:
        raise Http404("No such bulletin.")
    template = f'cribbage/news/{slug}.html'
    try:
        return render(request, template, {'story': story})
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
