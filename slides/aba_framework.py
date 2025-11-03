from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE
from slides.shared.asp_lexer import set_asp_lexer, get_asp_code

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 5
CODE_W = 5.5


set_asp_lexer()

def example_box(mobj):
    box = SurroundingRectangle(mobj, color=GREEN, buff=0.1).set_fill(color=[GREEN,WHITE], opacity=0.15)
    return VGroup(box, mobj)


class ABAFramework(BaseSlide):
    TITLE = r'ABA Framework (TODO)'

    def create_content(self):
        s = self.slide

        FONT_SIZE = 30
        BUFF=0.1
        FONT_SIZE_CODE = 18
        X = 0

        framework_text = MathTexWrapper(r'\frF=\frTup', font_size=50).to_edge(LEFT).shift(2.5*UP)
        language_l = TexWrapper(r'Language $\frL$', font_size=FONT_SIZE).next_to(framework_text, DOWN, aligned_edge=LEFT).shift(.5*RIGHT)
        example_language_l = example_box(MathTexWrapper(r'\set{ a,b,c,d,e,\ldots }', font_size=FONT_SIZE)).next_to(language_l, DOWN, aligned_edge=LEFT, buff=BUFF)
        language_code = get_asp_code('./code/aba-framework/language.lp', font_size=FONT_SIZE_CODE).move_to([X, language_l.get_top()[1], 0], aligned_edge=UL)

        assumptions_a = TexWrapper(r'Assumptions $\frA\subseteq\frL$', font_size=FONT_SIZE).next_to(example_language_l, DOWN, aligned_edge=LEFT)
        example_assumptions_a = example_box(MathTexWrapper(r'\set{ b,d,\ldots }', font_size=FONT_SIZE)).next_to(assumptions_a, DOWN, aligned_edge=LEFT,  buff=BUFF)
        assumptions_code = get_asp_code('./code/aba-framework/assumptions.lp', font_size=FONT_SIZE_CODE).move_to([X, assumptions_a.get_top()[1], 0], aligned_edge=UL)
        
        contraries = TexWrapper(r'Contrary function $\frCtr:\frA\mapsto\frL$', font_size=FONT_SIZE).next_to(example_assumptions_a, DOWN, aligned_edge=LEFT)
        example_contraries = example_box(MathTexWrapper(r'\bar{b}=c,\bar{d}=a,\ldots', font_size=FONT_SIZE)).next_to(contraries, DOWN, aligned_edge=LEFT,  buff=BUFF)
        contraries_code = get_asp_code('./code/aba-framework/contraries.lp', font_size=FONT_SIZE_CODE).move_to([X, contraries.get_top()[1], 0], aligned_edge=UL)
        
        rules = TexWrapper(r'Rules $h\leftarrow B$ with $h\in\frL\setminus\frA$, $B\subseteq \frL$', font_size=FONT_SIZE).next_to(example_contraries, DOWN, aligned_edge=LEFT)
        example_rules = example_box(MathTexWrapper(r'\set{d \leftarrow c,e,\ldots }', font_size=FONT_SIZE)).next_to(rules, DOWN, aligned_edge=LEFT,  buff=BUFF)
        rules_code = get_asp_code('./code/aba-framework/rules.lp', font_size=FONT_SIZE_CODE).move_to([X, rules.get_top()[1], 0], aligned_edge=UL)

        s.add(framework_text)
        
        s.wait()
        s.next_slide()

        s.play(FadeIn(language_l), FadeIn(example_language_l))
        s.next_slide()
        s.play(FadeIn(language_code))
        s.next_slide()

        s.play(FadeIn(assumptions_a), FadeIn(example_assumptions_a))
        s.next_slide()
        s.play(FadeIn(assumptions_code))
        s.next_slide()

        s.play(FadeIn(contraries), FadeIn(example_contraries))
        s.next_slide()
        s.play(FadeIn(contraries_code))
        s.next_slide()

        s.play(FadeIn(rules), FadeIn(example_rules))
        s.next_slide()
        s.play(FadeIn(rules_code))
        s.next_slide()


class AbaFrameworkScene(Slide):
    def construct(self):
        ABAFramework(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
