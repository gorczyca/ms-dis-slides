from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper, get_tex_template, IconDocumentStack

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('Motivation') + 1





# ---------- Your slide ----------
class SemMotivation(BaseSlide):
    TITLE = 'Big Picture: RMFs'

    def create_content(self):
        s = self.slide

        # Bullets (unchanged, but shifted left to make space for the icon)
        up_points = BulletedList(
            r'\sffamily \textbf{Risk management files:} hundreds of rows, dozens of pages',
            r'\textbf{Manual review:} slow, error-prone, inconsistent, tedious...',
            r'\textbf{Objective:} automate checks $\rightarrow$ ensure consistency, speed the process up',
            r'\textbf{Notified bodies need:} quick, objective validation',
            r'\textbf{Manufacturers need:} instant feedback before submission',
            font_size=40,
            color=BLACK,
            buff=0.2
        ).to_corner(UL).shift(DOWN*2 + RIGHT*0.2)

        # Document stack icon on the right
        stack = IconDocumentStack()
        stack.scale(0.35).to_edge(RIGHT).shift(UP*2) # .shift(DOWN*0.5 + LEFT*0.3)

        # Bring in the icon first
        s.play(FadeIn(stack, shift=UP*0.2), run_time=0.6)

        # Reveal bullets one by one; wiggle the stack on the first bullet
        for i, item in enumerate(up_points):
            s.play(FadeIn(item, shift=RIGHT), run_time=0.35)
            # if i == 0:
                # s.play(stack.attention_anim(), run_time=0.6)
            s.next_slide()

        # Brief hold after all items
        # s.wait(0.2)


class SemMotivationScene(Slide):
    def construct(self):
        SemMotivation(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
