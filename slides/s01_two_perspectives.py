from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
from slides.shared.common import FONT_SIZE_TEXT

SLIDE_NO = 1

WIDTH = 13
BUFF=1.5


def bullet_line(text, width=WIDTH, font_size=FONT_SIZE_TEXT):
    bullet = TexWrapper(r"$\bullet$", font_size=font_size)
    body = TexWrapper(
        r"\parbox[t]{%scm}{\sffamily %s}" % (width, text),
        font_size=font_size,
        color=BLACK,
    )
    body.next_to(bullet, RIGHT, aligned_edge=UP, buff=0.25).shift(UP*0.1)
    return VGroup(bullet, body).align_to(bullet, LEFT)

def tex_paragraph(text, width=WIDTH, font_size=FONT_SIZE_TEXT, color=BLACK):
    return TexWrapper(
        r"\parbox[t]{%scm}{\sffamily %s}" % (width, text),
        font_size=font_size,
        color=color,
    )


class S01TwoPerspectives(BaseSlide):
    TITLE = r'Formal Argumentation: Two Perspectives'

    def create_content(self):
        s = self.slide

        m_types_text = TexWrapper(r'Model types:', font_size=FONT_SIZE_TEXT).to_edge(LEFT).shift(UP*2+RIGHT*.25)

        items = [
            r'\textbf{Abstract} (e.g. \textbf{Dung AFs}) -- focus on relations between arguments',
            r'\textbf{Structured} (e.g. \textbf{ABA}) -- include premises, rules and inference steps',
        ]

        bullets = VGroup(*[bullet_line(t) for t in items]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(m_types_text, DOWN, aligned_edge=LEFT)

        s.add(m_types_text)
        for b in bullets:
            s.play(FadeIn(b, shift=0.2*RIGHT))
            s.next_slide()

        reasoning_views_text = TexWrapper(r'Reasoning views:', font_size=FONT_SIZE_TEXT).next_to(m_types_text, DOWN, buff=BUFF, aligned_edge=LEFT)
        reasoning_views_text_items = [
            r'\textbf{Argumentation as inference} -- decide acceptable arguments or claims',
            r'\textbf{Argumentation as process} -- argumentation as the reasoning mechanism itself'
        ]


        r_bullets = VGroup(*[bullet_line(t) for t in reasoning_views_text_items]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(reasoning_views_text, DOWN, aligned_edge=LEFT)

        s.play(FadeIn(reasoning_views_text))
        s.next_slide()

        for b in r_bullets:
            s.play(FadeIn(b, shift=0.2*RIGHT))
            s.next_slide()

        arg_text = tex_paragraph(r'\textbf{Argument games:} discussion between proponent and opponent; provide dialectical justifications, support interaction, connected to dialogical models $\rightarrow$ useful for XAI').next_to(reasoning_views_text, DOWN, buff=BUFF*1.15, aligned_edge=LEFT)

        s.play(FadeIn(arg_text))

        



class S01TwoPerspectivesScene(Slide):
    def construct(self):
        S01TwoPerspectives(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
