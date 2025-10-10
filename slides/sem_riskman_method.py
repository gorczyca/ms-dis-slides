from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper, IconDocumentStack, SmallGraph

from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('RiskmanMethod') + 1

class SemRiskmanMethod(BaseSlide):
    TITLE = r'Our Proposal'
    def create_content(self):

        s = self.slide

        up_points = BulletedList(
            r'\sffamily  \textbf{Assumption:} RMFs should be digitized',
            r'\sffamily  \textbf{Requirement:} RMFs must be human- and machine-readable',
            r'\sffamily  \textbf{Approach:} encode them in a logic-based language: RDFa=HTML+RDF',
            r'\sffamily  \textbf{Benefit:} supports inference (implicit knowledge completion)',
            r'\sffamily $\qquad$ and validation (constraints checking)',
            font_size=30,
            color=BLACK,
            buff=0.2
        ).to_corner(UL).shift(DOWN*2+RIGHT*0.5)

        up_points[3][16:25].set_color(D_BLUE)    
        up_points[4][4:14].set_color(LAT_ORANGE)


        icon = IconDocumentStack().scale(0.5).to_edge(RIGHT).shift(UP*2+0.25*LEFT)
        gr = SmallGraph(5, -1)   
        s.add(icon)

        for i, item in enumerate(up_points):
            s.play(FadeIn(item, shift=RIGHT))

            if i == 2:
                s.next_slide()
                s.play(Create(gr))

            if i == 3:
                s.next_slide()
                s.play(Create(gr.to_add))

            s.next_slide()

        # s.next_slide()
        s.play(
            gr.to_highlight[0][0].animate.set_color(LAT_ORANGE),
            # prob5[0].animate.set_color(LAT_ORANGE),
            gr.to_highlight[1][0].animate.set_color(LAT_ORANGE)
        )
        

class SemRiskmanMethodScene(Slide):  
    def construct(self):
        SemRiskmanMethod(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()