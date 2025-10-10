from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.common import boxed, labeled_node, edge_between, ind_edge

from slides.shared.colors import HIGH_COLOR, GREEN_PASTEL


from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('EncRules2') + 1

class SemEncRules2(BaseSlide):
    TITLE = r'The \textsc{Riskman} Ontology: Encoding Rules (2)' 
    def create_content(self):
        
       
        according = TexWrapper('According to ISO 14971 [3.18]:').move_to([-6,2.5,0], aligned_edge=LEFT)
        
        entity_title = TextWrapper('risk', weight=BOLD, font_size=20)
        definition = TexWrapper('Combination of probability of occurrence of harm and severity.', font_size=30).next_to(entity_title, DOWN, buff=10, aligned_edge=LEFT)#.shift(DOWN*2)
        def_box = boxed(entity_title, definition, color=BLACK, buff=0.35).move_to([0,1.5,0], aligned_edge=ORIGIN)

        bar = Line(LEFT, RIGHT).scale(6).set_stroke(BLACK, 2).next_to(def_box, DOWN, buff=1)
        ontology_text = TextWrapper('Ontology (TBox)', font_size=20).next_to(bar, UP, aligned_edge=LEFT).shift(RIGHT)
        data_text = TextWrapper('Data (ABox)', font_size=20).next_to(bar, UP, aligned_edge=RIGHT).shift(LEFT)
        
        s = self.slide
        s.add(according, def_box)
        s.wait()
        s.next_slide()

        s.play(DrawBorderThenFill(bar), Write(ontology_text), Write(data_text))


        # ontology axiom
        axiom = MathTexWrapper(
            r'\begin{array}{c}'
            r'\exists \text{hasRiskLevel}.\top \sqcap \\'
            r'\exists \text{hasHarm}.\top \sqsubseteq {\color{blue}\textit{Risk}}'
            r'\end{array}'
        ).next_to(ontology_text, DOWN, aligned_edge=LEFT, buff=1)


        s.wait()
        s.next_slide()
        s.play(Write(axiom))
        s.next_slide()

        # graph 
        rl = labeled_node('...', [3,-1,0], color=BLACK)
        sev = labeled_node('...', [6, -1, 0], color=BLACK)
        rls_edge = edge_between(rl, sev, out_dir=RIGHT, in_dir=LEFT, label_text='hasSeverity', font_size=20)
        prob = labeled_node('...', [3, -3, 0], color=BLACK)
        rlp_edge = edge_between(rl, prob, out_dir=DOWN, in_dir=UP, label_text='hasProbability', font_size=20)
        
        r = labeled_node('...', [0,-1,0], color=BLACK)
        rrl_edge = edge_between(r, rl, out_dir=RIGHT, in_dir=LEFT, label_text='hasRiskLevel', font_size=20)
        h = labeled_node('...', [0,-3,0], color=BLACK)
        rh_edge = edge_between(r, h, out_dir=DOWN, in_dir=UP, label_text='hasHarm', font_size=20)

        graph = VGroup(rl, sev, rls_edge, prob, rlp_edge, r, rrl_edge, h, rh_edge)
        s.play(DrawBorderThenFill(graph))
        s.next_slide()

        risk_level_label = TexWrapper(r'{\color{blue}\textit{RiskLevel}}').next_to(rl,UP,buff=0.25)
        s.play(Write(risk_level_label))
        s.wait()
        s.next_slide()

        self.slide.play(
            Indicate(axiom[0][0:15], color=HIGH_COLOR, scale_factor=1.05),   # first part
            Indicate(axiom[0][16:26], color=HIGH_COLOR, scale_factor=1.05)    # last part
        )

        # self.slide.wait()
        s.next_slide()
        s.play(*ind_edge(rh_edge), *ind_edge(rrl_edge), Indicate(r, color=GREEN_PASTEL))
        
        s.next_slide()

        risk_label = TexWrapper(r'{\color{blue}\textit{Risk}}').next_to(r,UP,buff=0.25)
        s.play(Write(risk_label))
        

class SemEncRules2Scene(Slide):  
    def construct(self):
        SemEncRules2(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()