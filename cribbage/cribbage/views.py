import random

from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.views.decorators.http import require_http_methods


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


# ── The sanctioned events calendar ──────────────────────────────────────
EVENTS = [
    {
        'date_display': '12–14 June MMXXVI',
        'location': 'Bordeaux, France',
        'sanction': 'Continental Championship',
        'title': 'European Confederation Championships',
        'description': (
            'The senior recurring competition of the European Confederation, '
            'contested at the H&ocirc;tel de Ville. The defending Champion, '
            'Mme Ren&eacute;e Charpentier of the F&eacute;d&eacute;ration '
            'Fran&ccedil;aise, returns to defend the title for the third '
            'consecutive year.'
        ),
        'registration': 'By national federation invitation; the list of qualifying federations is presently closed.',
    },
    {
        'date_display': '24–26 July MMXXVI',
        'location': 'Halifax, Nova Scotia',
        'sanction': 'Ratified Variant · Four-Hand Partners',
        'title': 'The Four-Hand Partners Festival',
        'description': (
            'The largest annual gathering of the partnered variant, hosted by '
            'the Maritime Federation since 1979. Partnerships of long standing '
            'and partnerships newly formed compete on the same draw.'
        ),
        'registration': 'Registration open through national federation thirty days prior; partnerships must be filed in writing.',
    },
    {
        'date_display': '7–9 August MMXXVI',
        'location': 'Casablanca, Kingdom of Morocco',
        'sanction': 'Continental Championship',
        'title': 'African Confederation Cup',
        'description': (
            'The senior competition of the African Confederation, contested '
            'biennially at venues rotating among the member federations. The '
            'Casablanca venue has hosted the Cup on four prior occasions.'
        ),
        'registration': 'By federation invitation; the African Confederation Secretariat administers the draw.',
    },
    {
        'date_display': '23 August MMXXVI',
        'location': 'Portland, Oregon',
        'sanction': 'Sector Qualifier',
        'title': 'Pacific Northwest Federation — Sanctioned Qualifier',
        'description': (
            'One of the regional qualifiers for the North American Sector '
            'Championship in October. The Pacific Northwest qualifier is '
            'noted for its severe field strength relative to its draw size.'
        ),
        'registration': 'Registration open through the Pacific Northwest Federation, closing the first of August.',
    },
    {
        'date_display': '11–13 September MMXXVI',
        'location': 'Toronto, Ontario',
        'sanction': 'Sector Championship',
        'title': 'NCCWL North American Open',
        'description': (
            'The senior competition of the National Crib Champ World League, '
            'contested annually since 1947 with intermissions only in years '
            'of the World Championship cycle. The Toronto venue has hosted '
            'the Open on eleven prior occasions.'
        ),
        'registration': 'By Sector invitation; the list of invited players will be published in the Annual Bulletin.',
    },
    {
        'date_display': '14–18 September MMXXVI',
        'location': 'Reykjav&iacute;k, Iceland',
        'sanction': 'World Championship · Quadrennial',
        'title': 'XXIII Quadrennial World Championships',
        'description': (
            'The Association&rsquo;s senior recurring competition, contested '
            'every fourth year at venues nominated by the Council of '
            'Federations. The Reykjav&iacute;k venue&rsquo;s bid was approved '
            'at the 2023 Sector Meeting in Dubai. The defence by the '
            'present Champion is anticipated to be the central narrative '
            'thread of the Championships.'
        ),
        'registration': 'By national federation nomination, ratified by the Sanctioning Committee.',
    },
    {
        'date_display': '16 September MMXXVI',
        'location': 'Veracruz, M&eacute;xico',
        'sanction': 'Commemorative · Veracruz Convention',
        'title': 'The Veracruz Convention Commemorative Tournament',
        'description': (
            'Marking the sixty-fourth anniversary of the Veracruz Convention '
            'of 1962, at which the Association formally designated tequila '
            'as the official spirit of sanctioned cribbage. The ceremonial '
            'toast is conducted by the Executive Director.'
        ),
        'registration': 'Open to all sanctioned holders of any rank; registration on the day.',
    },
    {
        'date_display': '18 October MMXXVI',
        'location': 'Yarmouth, Nova Scotia',
        'sanction': 'Sanctioned Charity Match',
        'title': 'The Anglers&rsquo; Hospice Foundation Match',
        'description': (
            'An invitational eight-player charity engagement in aid of the '
            'Yarmouth Anglers&rsquo; Hospice, in continuous operation since '
            '1971. The Match is conducted under simplified scoring conventions '
            'to accommodate the spectator gallery.'
        ),
        'registration': 'Tickets via the host institution; players by invitation only.',
    },
    {
        'date_display': '18–21 October MMXXVI',
        'location': 'Singapore',
        'sanction': 'Continental Championship',
        'title': 'Asian Confederation Championships',
        'description': (
            'The senior competition of the Asian Confederation, contested at '
            'the Raffles Convention Centre. The Singaporean Federation, '
            'admitted to the Confederation in 1998, hosts for the first time.'
        ),
        'registration': 'By federation invitation; the Asian Confederation Secretariat administers the draw.',
    },
    {
        'date_display': '22–24 November MMXXVI',
        'location': 'Mexico City, M&eacute;xico',
        'sanction': 'Sector Open',
        'title': 'Pan-American Open',
        'description': (
            'The senior open of the Pan-American Confederation, contested in '
            'alternate years between Mexico City and S&atilde;o Paulo. The '
            'Mexico City venue last hosted in 2024.'
        ),
        'registration': 'Open registration through the Mexican Federation, closing the first of November.',
    },
    {
        'date_display': '12 January MMXXVII',
        'location': 'Norwich, England',
        'sanction': 'Sanctioned Invitational',
        'title': 'The Suckling Memorial Invitational',
        'description': (
            'Held annually in the cathedral close at Norwich in commemoration '
            'of Sir John Suckling, the seventeenth-century English poet to '
            'whom the invention of the game is traditionally attributed. The '
            'Invitational is contested in five-card cribbage, the historical '
            'form of the game.'
        ),
        'registration': 'By the Memorial Trust&rsquo;s annual invitation, generally extended to twelve players.',
    },
    {
        'date_display': '19–22 February MMXXVII',
        'location': 'Ushuaia, Argentina',
        'sanction': 'Continental Championship · Inaugural',
        'title': 'Free Federation of Polar Cribbage Bodies — Inaugural Antarctic Open',
        'description': (
            'The first sanctioned competition of the Free Federation of Polar '
            'Cribbage Bodies, contested in Ushuaia owing to the climatic '
            'unsuitability of the Antarctic mainland in February. The '
            'Federation&rsquo;s charter contemplates eventual relocation to '
            'McMurdo Station upon the completion of the heated pavilion now '
            'under construction.'
        ),
        'registration': 'By Federation nomination; the inaugural draw is presently confidential.',
    },
    {
        'date_display': '5–7 March MMXXVII',
        'location': 'Auckland, New Zealand',
        'sanction': 'Continental Championship',
        'title': 'Oceanic Confederation Open',
        'description': (
            'The senior competition of the Oceanic Confederation, hosted in '
            'alternating years between Auckland and Brisbane. The Auckland '
            'venue&rsquo;s Tasman Room has hosted the Open since 1992.'
        ),
        'registration': 'By federation invitation; observers welcomed on registration in advance.',
    },
    {
        'date_display': '3–5 April MMXXVII',
        'location': 'Vienna, Austria',
        'sanction': 'Ratified Variant · Three-Hand World Championship',
        'title': 'The Three-Hand World Championship',
        'description': (
            'The senior recurring competition of the three-hand variant, '
            'contested triennially at the Hofburg Congress Centre. The '
            'Championship is the only sanctioned event at which the deal '
            'rotates by the full Viennese protocol.'
        ),
        'registration': 'By national federation nomination, ratified by the Variant Sub-Committee.',
    },
    {
        'date_display': '4–7 May MMXXVII',
        'location': 'The Hague, the Netherlands',
        'sanction': 'Convocation · Triennial Congress',
        'title': 'The Council of Federations Triennial Congress',
        'description': (
            'The senior deliberative assembly of the Association, convened '
            'every third year at Suckling House for the consideration of '
            'amendments to the standing bylaws, the receipt of the '
            'Director&rsquo;s reports, and such other business as the Council '
            'shall by motion entertain.'
        ),
        'registration': 'Delegations by national federation. Observers admitted by application to the Office of the Director.',
    },
]


def events(request):
    return render(request, 'cribbage/events.html', {'events': EVENTS})


def membership_apply(request):
    return render(request, 'cribbage/membership_apply.html')


def scoring_calculator(request):
    return render(request, 'cribbage/scoring_calculator.html')


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        # The Director's correspondence is in fact never delivered; the
        # reference number is generated at random and the message is silently
        # discarded. This is in keeping with the standing policy.
        name = request.POST.get('name', '').strip()
        message = request.POST.get('message', '').strip()
        if name and message:
            reference = f"ICA-{random.randint(100000, 999999)}-COR"
            return render(request, 'cribbage/contact_received.html', {
                'reference': reference,
            })
    return render(request, 'cribbage/contact.html')
