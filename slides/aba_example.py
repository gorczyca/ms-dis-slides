from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 8


class ABAExample(BaseSlide):
    TITLE = r'ABA Example (TODO)'

    def create_content(self):
        s = self.slide

        # framework        
        FONT_SIZE = 30
        BUFF=0.05
        assumptions = TexWrapper(r'$\frA=\set{a,b,c,d,e,\bar{e},f}$, $\frCtr(x)=\bar{x}$ for $x\in\frA$', font_size=FONT_SIZE).to_corner(UR).shift(DOWN)
        rules = TexWrapper(r'$\frR=\{ s \gets d,p,a; \;\; p\gets\bar{c}; \;\; \bar{c} \gets f; $', font_size=FONT_SIZE).next_to(assumptions, DOWN, aligned_edge=LEFT, buff=BUFF*2)
        rules_2 = TexWrapper(r'$\bar{a} \gets b,t; \;\;\;\;\;\; \bar{d} \gets e;   \;\; t\gets c \;\;\; \}$', font_size=FONT_SIZE).next_to(rules, DOWN, aligned_edge=LEFT, buff=BUFF).shift(RIGHT*.85)


        FONT_SIZE_OUTPUT = 30
        output_str = TexWrapper(r'Output:', font_size=FONT_SIZE_OUTPUT)
        m_1 = TexWrapper(r'\texttt{m(1,p,pb1,}$s\gets d,p,a$\texttt{).}}', font_size=FONT_SIZE_OUTPUT)
        m_2 = TexWrapper(r'\texttt{m(2,o,ob2,}$\bar{a}\gets b,t$\texttt{).}}', font_size=FONT_SIZE_OUTPUT)
        m_2_1 = TexWrapper(r'\texttt{m(2,o,ob2,}$\bar{d}\gets e$\texttt{).}}', font_size=FONT_SIZE_OUTPUT)
        m_3 = TexWrapper(r'\texttt{m(3,p,ob1,}$t\gets c$\texttt{).}}', font_size=FONT_SIZE_OUTPUT)
        m_4 = TexWrapper(r'\texttt{m(4,p,pf2,$\bar{e}$).}', font_size=FONT_SIZE_OUTPUT)
        m_5 = TexWrapper(r'\texttt{m(5,p,pb1,}$p\gets \bar{c}$\texttt{).}}', font_size=FONT_SIZE_OUTPUT)
        m_6 = TexWrapper(r'\texttt{m(6,p,pb1,}$\bar{c}\gets f$\texttt{).}}', font_size=FONT_SIZE_OUTPUT)

        output_group = VGroup(output_str, m_1, m_2, m_2_1, m_3, m_4, m_5, m_6).arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(assumptions, DOWN, aligned_edge=LEFT, buff=1.5)
        
        s.add(assumptions, rules, rules_2, output_group)

        s.wait()


class AbaExampleScene(Slide):
    def construct(self):
        ABAExample(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
