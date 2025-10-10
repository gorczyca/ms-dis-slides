from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.common import boxed, labeled_node, edge_between, ind_edge
from slides.shared.qrcode_gen import qr_code


from slides.shared.colors import HIGH_COLOR, GREEN_PASTEL, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('MoreShacl') + 1


class SemMoreShacl(BaseSlide):
    TITLE = r'\textsc{Riskman}: SHACL Shapes'

    def create_content(self):
        s = self.slide

        shape1 = MathTexWrapper(r'\text{ControlledRisk} \Rightarrow {\color{shaclCol} =_{1} \text{isMitigatedBy}.\top', font_size=25) #.next_to(entity_title, DOWN, buff=10, aligned_edge=LEFT)#.shift(DOWN*2)
        shape1_expl = TexWrapper(r'\textit{"Every controlled risk must be mitigated."}', font_size=25).next_to(shape1, aligned_edge=LEFT)
        def_box = boxed(shape1, shape1_expl,  color=BLACK, buff=0.15).move_to([-6,2,0], aligned_edge=LEFT)

        s.wait()
        s.next_slide()
        s.play(DrawBorderThenFill(def_box))


        shape2 = MathTexWrapper(r'\text{SDA} \Rightarrow {\color{shaclCol} \exists \text{hasSubSDA}\cdot\text{hasImplementationManifest}.\top', font_size=25) #.next_to(entity_title, DOWN, buff=10, aligned_edge=LEFT)#.shift(DOWN*2)
        shape2_expl = TexWrapper(r'\textit{"Every SDA needs a final mitigation (which has the implementation manifest)."}', font_size=25).next_to(shape2, aligned_edge=LEFT)
        def2_box = boxed(shape2, shape2_expl,  color=BLACK, buff=0.15).next_to(def_box, DOWN, aligned_edge=LEFT, buff=1)
        
        s.next_slide()
        s.play(DrawBorderThenFill(def2_box))

        s.next_slide()
        shape3 = TexWrapper(r'\ldots', font_size=50)
        def3_box = boxed(shape3,  color=BLACK, buff=0.15, pad=0.5).next_to(def2_box, DOWN, aligned_edge=LEFT, buff=1)
        s.play(DrawBorderThenFill(def3_box))



class SemMoreShaclScene(Slide):
    def construct(self):
        SemMoreShacl(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
