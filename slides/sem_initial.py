import textwrap
from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper, get_tex_template, IconDocument

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('Initial') + 1





# ---------- Your slide ----------
class SemInitial(BaseSlide):
    TITLE = 'Motivation'

    def create_content(self):
        s = self.slide
        left = TextWrapper('Manufacturer').scale(0.9).to_edge(LEFT).shift(UP*0.5)
        right = TextWrapper('Notified Body').scale(0.9).to_edge(RIGHT).shift(UP*0.5)
        stetho = ImageMobject('img/stethoscope.png').scale(0.25).next_to(left, DOWN)

        s.wait()
        s.next_slide()
        s.play(FadeIn(stetho))
        # s.wait()
        s.next_slide()

        s.play(Write(left))
        s.next_slide()
        lr = Arrow(left.get_right(), right.get_left(), buff=0.4, color=BLACK)

        doc = IconDocument()
        # doc.scale(0.35).to_edge(UP).shift(DOWN*5) # .shift(DOWN*0.5 + LEFT*0.3)
        doc.scale(0.35).next_to(lr, UP, buff=0.5) # .shift(DOWN*0.5 + LEFT*0.3)
        s.play(DrawBorderThenFill(doc))
        s.next_slide()

        # doc = IconDocument()
        # doc.scale(0.35).to_edge(UP).shift(DOWN*5) # .shift(DOWN*0.5 + LEFT*0.3)
        # s.play(DrawBorderThenFill(doc))
        # s.next_slide()

        s.play(GrowArrow(lr), Write(right))
        s.next_slide()

        s.play(FadeOut(lr))
        rl = Arrow(right.get_left(), left.get_right(), buff=0.4, color=BLACK)
        cross = TextWrapper("✗", color=RED).scale(1.6).next_to(rl, DOWN)
        s.play(GrowArrow(rl))
        s.play(Write(cross))
        s.next_slide()
        s.play(FadeOut(rl), FadeOut(cross)) 
        s.next_slide()

        s.play(GrowArrow(lr))
        s.next_slide()

        s.play(FadeOut(lr))
        s.next_slide()
        s.play(GrowArrow(rl))
        check = TextWrapper("✓", color=GREEN).scale(1.6).next_to(rl, DOWN)
        # lr2 = Arrow(left.get_right(), right.get_left(), buff=0.4, color=BLACK)
        s.play(Write(check))
        s.next_slide()


class SemInitialScene(Slide):
    def construct(self):
        SemInitial(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
