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
    # ── The Rise: Tony Cullen and Alicia Lake (archive) ───────────────────
    {
        'slug': 'lake-perfect-29-washington',
        'date_display': '19 January MMXXVI',
        'category': 'From the Archive · Sector Championship',
        'title': 'Lake Wins Washington State Finals with Perfect Twenty-Nine; Bicycle Brand Cards Confirms Sponsorship Renewal',
        'excerpt': (
            'The closing hand — three Fives and the Jack of clubs with the '
            'fourth Five of clubs as Starter — was the eighth sanctioned '
            'twenty-nine of Ms. Lake’s career. The opposing player finished '
            'below the skunk line.'
        ),
    },
    {
        'slug': 'tarbish-tournament-lake',
        'date_display': '18 December MMXXV',
        'category': 'From the Archive · Tournament Despatch',
        'title': 'International Tarbish Tournament to Honour Lake as Guest in January Seattle Convocation',
        'excerpt': (
            'Ms. Lake becomes the first cribbage Masters holder named Guest '
            'of Honour at the Tarbish Convocation since 1987. Mr. Cullen '
            'compares the cross-game distinction to the Nobel Peace Prize '
            'winner attending the Nobel Physics presentation.'
        ),
    },
    {
        'slug': 'cullen-lake-masters-dubai',
        'date_display': '14 November MMXXIV',
        'category': 'From the Archive · Sector Resolution',
        'title': 'Cullen and Lake Elevated to Masters Level Following Sector Vote in Dubai',
        'excerpt': (
            'The Association’s highest distinction was conferred jointly upon '
            'Mr. Cullen and his sanctioned mentee Ms. Lake at the Madinat '
            'Jumeirah Conference Centre. Mr. Douglas Ronne was concurrently '
            'inducted at the Pi Level on the motion of Mr. Cullen.'
        ),
    },
    {
        'slug': 'cullen-spanish-wells-pigs',
        'date_display': '31 January MMXXIII',
        'category': 'From the Archive · Special Programs',
        'title': 'Cullen Wild Pig Welfare Initiative Established at Spanish Wells',
        'excerpt': (
            'Ms. Michelle Cullen, Director of Special Programs, has formally '
            'extended the Special Programs portfolio to encompass the welfare '
            'of the wild pig population resident on the eastern beaches of '
            'Spanish Wells, in the Eleuthera District of the Bahamas.'
        ),
    },
    {
        'slug': 'lake-trudeau-rcmp-ruling',
        'date_display': '8 June MMXXI',
        'category': 'From the Archive · Tribunal',
        'title': 'Tribunal Examines Allegations of RCMP Misconduct Following Lake–Trudeau Championship Final',
        'excerpt': (
            'Ms. Lake decisively defeated Mr. Trudeau at the Château '
            'Frontenac before the attempted RCMP detention that followed. '
            'The Canadian Federation’s standing has been referred to the '
            'Office of the Director pending the Tribunal’s determination.'
        ),
    },
    {
        'slug': 'cullen-uganda-tiny-homes',
        'date_display': '15 March MMXX',
        'category': 'From the Archive · Philanthropic Initiative',
        'title': 'Cullen Initiative Repurposes Retired Cribbage Boards as Tiny Homes in Uganda',
        'excerpt': (
            'Mr. Cullen has donated the first two hundred boards to the '
            'Kampala district programme. Mr. Cullen acknowledges the '
            'dwellings to be “too small to house anyone” and describes their '
            'primary use as adjunctive structures sited alongside existing '
            'dwellings.'
        ),
    },
    {
        'slug': 'lake-mentee-induction',
        'date_display': '22 September MMXVIII',
        'category': 'From the Archive · Sector Designation',
        'title': 'Lake Inducted as Cullen’s First Sanctioned Mentee; Sector Hails “A Singular Partnership”',
        'excerpt': (
            'The North American Sector formally designated Ms. Lake as the '
            'sanctioned mentee of Level 3 holder Mr. Cullen — the first female '
            'mentee designated by a Level 3 holder in the Sector’s history.'
        ),
    },
    {
        'slug': 'cullen-level-3-helsinki',
        'date_display': '18 March MMXV',
        'category': 'From the Archive · Congress Despatch',
        'title': 'Cullen Elevated to Level 3 at the Helsinki Congress; Federation Cites “Singular Mastery of the Crib”',
        'excerpt': (
            'The Council of Federations, in unanimous voice vote at Finlandia '
            'Hall, elevated Mr. Cullen to the Association’s second-highest '
            'certification. The Sanctioning Committee took particular note of '
            'the player’s 78 per cent skunk rate across all sanctioned play.'
        ),
    },
    {
        'slug': 'cullen-level-1-toronto',
        'date_display': '12 October MMIX',
        'category': 'From the Archive · Sector News',
        'title': 'Cullen Confirmed at Level 1 Certification; Sector Notes “A Quietly Generational Player”',
        'excerpt': (
            'Mr. Cullen crossed the thirty-thousand sanctioned-win threshold '
            'at the Toronto Regional, becoming the seventh holder of the Level '
            '1 distinction inducted by the North American Sector in the decade.'
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
