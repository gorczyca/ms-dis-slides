from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import FONT, MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.graphs import fixed_arrow_graph, curved_arrow

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 6





class S06ABAArguments(BaseSlide):
    TITLE = r'Extension to ABA Disputes: Arguments \& Attacks'

    def create_content(self):
        s = self.slide

        FONT_SIZE = 25


        fr = TexWrapper(r'Let $\frF=\frTup$.', font_size=FONT_SIZE)
        args = TexWrapper(r'Define $\Args$:', font_size=FONT_SIZE)
        case_1 = TexWrapper(r'$\bullet$ $a \in \Args \text{ if } a \in \frA$', font_size=FONT_SIZE)
        case_1_then = TexWrapper(r'then $\conc(a)=a$, $\prem(a)=a$', font_size=FONT_SIZE)
        case_2 = TexWrapper(r'$\bullet$ $A = h \leftarrow A_1,\ldots,A_n \in \Args$', font_size=FONT_SIZE)
        case_2_if = TexWrapper(r'if $\set{A_1,\ldots,A_n}\subseteq \Args$ and $ h\leftarrow \conc(A_1),\ldots,\conc(A_n)$', font_size=FONT_SIZE)
        case_2_then = TexWrapper(r'then $\conc(A)=h$, $\prem(A)=\prem(A_1)\cup\ldots\cup\prem(A_n)$', font_size=FONT_SIZE)

        att = TexWrapper(r'Define $\Att\subseteq \Args\times\Args$:', font_size=FONT_SIZE)
        att_1 = TexWrapper(r'$\bullet$ $\tuple{A_1,A_2}\in\Att$', font_size=FONT_SIZE)
        att_if_1 = TexWrapper(r'if $A_1,A_2\in\Args$, $a\in\prem(A_2)$, $\conc(A_1)=\bar{a}$', font_size=FONT_SIZE)
        # att_if_1 = TexWrapper(r'if $A_1,A_2\in\Args$', font_size=FONT_SIZE)
        # att_if_2 = TexWrapper(r'and $a\in\prem(A_2)$', font_size=FONT_SIZE)
        # att_if_3 = TexWrapper(r'and $\conc(A_1)=\bar{a}$', font_size=FONT_SIZE)

        args_group = VGroup(
            fr,
            args,
            case_1,
            case_1_then,
            case_2,
            case_2_if,
            case_2_then,
            att,
            att_1,
            att_if_1,
            # att_if_2,
            # att_if_3,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(LEFT)

        att_group = VGroup(
            att,
            att_1,
            att_if_1
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(args_group, DOWN, aligned_edge=LEFT)

        BUFF_RATIO = 0.2
        case_1_then.shift(BUFF_RATIO*RIGHT)
        case_2_if.shift(BUFF_RATIO*RIGHT)
        case_2_then.shift(BUFF_RATIO*RIGHT)

        att_if_1.shift(BUFF_RATIO*RIGHT)
        # att_if_2.shift(BUFF_RATIO*RIGHT)
        # att_if_3.shift(BUFF_RATIO*RIGHT)

        assumptions = TexWrapper(r'$\frA=\set{a,b,c}$, $\frCtr(x)=\bar{x}$ for $x\in\frA$', font_size=FONT_SIZE).next_to(args_group, RIGHT, aligned_edge=UP, buff=0.4)
        rules = TexWrapper(r'$\frR=\set{ p \gets a,b; \;\;\; \bar{c} \gets p; \;\;\;  r\gets c }$',
        # rules = MathTexWrapper(
        #     r"\begin{aligned}"
        #     r"\frR = \{\,"
        #     r"&p\!\!\!\! &&\gets a,b;\\"
        #     r"&\bar{c} &&\gets p;\\"
        #     r"&r &&\gets c\,\}"
            # r"\end{aligned}",
            font_size=FONT_SIZE,
        ).next_to(assumptions, DOWN, aligned_edge=LEFT)




        s.add(args_group, att_group, assumptions, rules)
        
        RADIUS = 0.2
        STROKE_WIDTH=1





        a = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH).add(MathTexWrapper("a")).next_to(rules, DOWN, aligned_edge=LEFT)
        b = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH).add(MathTexWrapper("b")).next_to(a, RIGHT, buff=0.8)
        c = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH).add(MathTexWrapper("c")).next_to(b, RIGHT, buff=0.8)

        s.wait()
        s.next_slide()

        s.play(Create(VGroup(a,b,c)))

        a_cp, b_cp, c_cp = a.copy(), b.copy(), c.copy()

        a_cp.next_to(a, DOWN, aligned_edge=LEFT)
        b_cp.next_to(a_cp, DOWN, aligned_edge=LEFT)

        s.next_slide()
        s.play(TransformFromCopy(a, a_cp), TransformFromCopy(b, b_cp))

        p = Circle(radius=RADIUS, color=WHITE).add(MathTexWrapper("p")).next_to(a_cp, RIGHT, buff=1).shift(DOWN*0.4)


        p_arg = VGroup(
            p,
            fixed_arrow_graph(a_cp.get_right(), p.get_left()+ UP * 0.1, color=BLACK),
            fixed_arrow_graph(b_cp.get_right(), p.get_left() + DOWN * 0.1, color=BLACK),
        )

        p_box = SurroundingRectangle(p_arg, a_cp, b_cp, color=BLACK, buff=0.1, corner_radius=0.0, stroke_width=1)
        p_arg_box = VGroup(p_arg, p_box, a_cp, b_cp)
        s.next_slide()
        s.play(Create(p_arg), Create(p_box))

        s.next_slide()

        c_cp.next_to(c, DOWN, aligned_edge=LEFT)
        s.play(TransformFromCopy(c, c_cp))

        s.next_slide()
        r = Circle(radius=RADIUS, color=WHITE).add(MathTexWrapper("r")).next_to(c_cp, RIGHT, buff=1)
        r_arg = VGroup(r, fixed_arrow_graph(c_cp.get_right(), r.get_left(), color=BLACK))
        r_box = SurroundingRectangle(r_arg, c_cp, color=BLACK, buff=0.1, corner_radius=0.0, stroke_width=1)
        s.play(Create(r_arg), Create(r_box))

        s.next_slide()

        p_arg_box_cp = p_arg_box.copy()

        p_arg_box_cp.next_to(p_box, DOWN)

        xc = Circle(radius=RADIUS, color=WHITE).add(MathTexWrapper(r"\bar{c}")).next_to(p_arg_box_cp[0][0], RIGHT, buff=1)
        s.next_slide()
        s.play(TransformFromCopy(p_arg_box, p_arg_box_cp))

        xc_arg = VGroup(
            xc,
            fixed_arrow_graph(p_arg_box_cp[0][0], xc.get_left(), color=BLACK),

        )
        xc_box = SurroundingRectangle(p_arg_box_cp, xc, color=BLACK, buff=0.1, corner_radius=0.0, stroke_width=1)

        s.next_slide()
        s.play(Create(xc_arg), Create(xc_box))

        s.next_slide()
        s.play(Create(fixed_arrow_graph(xc.get_top(), c_cp.get_bottom(), color=RED)))
        s.next_slide()
        s.play(Create(curved_arrow(xc.get_top(), c.get_right()+RIGHT*0.1+DOWN*0.1, bend=-.4, color=RED)))

class S06AbaArgumentsScene(Slide):
    def construct(self):
        S06ABAArguments(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
