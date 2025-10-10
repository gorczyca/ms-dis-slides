from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.common import boxed, labeled_node, edge_between, ind_edge
from slides.shared.qrcode_gen import qr_code


from slides.shared.colors import HIGH_COLOR, GREEN_PASTEL

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('RiskmanStats') + 1


class SemRiskmanStats(BaseSlide):
    TITLE = r'The \textsc{Riskman} Ontology \& Shapes: Overview'

    def create_content(self):

        # p = qr_code('https://w3id.org/riskman')

        s = self.slide
        qr = ImageMobject("img/qr.png") \
            .scale(0.8) \
            .to_corner(DR).shift(UP)

        # logo = ImageMobject("img/riskman-doc.png") \
        logo = ImageMobject("img/riskman-doc.png") \
            .scale(.35) \
            .to_corner(UR)

        border = Rectangle(
            width=qr.width + 0.3,
            height=qr.height + 0.3,
            stroke_color=HIGH_COLOR,
            stroke_width=3
        ).move_to(qr)
        s.add(qr, qr, border, logo)  # for some reason something caches

        points = BulletedList(
            r'$\bullet$ formulated in the lightweight OWL EL',
            r'$\bullet$ 24 classes',
            r'$\bullet$ 27 object properties (each with domain and range)',
            r'$\bullet$ 15 concept and role inclusion axioms',
            r'$\bullet$ 10 SHACL shapes',
            r'$\bullet$ registered under stable URI \texttt{https://w3id.org/riskman}',
            font_size=30,
            color=BLACK,
            buff=0.2
        ).to_edge(LEFT)

        for item in points:
            s.play(FadeIn(item, shift=RIGHT))
            s.next_slide()


# to be run as standalone
# i.e. by only `manim slide2.py Slide2Scene`
class SemRiskmanStatsScene(Slide):
    def construct(self):
        SemRiskmanStats(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
