from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.common import boxed, labeled_node, edge_between, ind_edge

from slides.shared.colors import HIGH_COLOR, GREEN_PASTEL

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('EncRules1') + 1


class SemEncRules1(BaseSlide):
    TITLE = r'The \textsc{Riskman} Ontology: Encoding Rules (1)' 
    def create_content(self):
               
        entity_title = TextWrapper('risk level', weight=BOLD, font_size=20)
        definition = TexWrapper('Combination of probability and severity.', font_size=30).next_to(entity_title, DOWN, buff=10, aligned_edge=LEFT)#.shift(DOWN*2)
        def_box = boxed(entity_title, definition, color=BLACK, buff=0.35).move_to([0,2,0], aligned_edge=ORIGIN)
        
        bar = Line(LEFT, RIGHT).scale(6).set_stroke(BLACK, 2).next_to(def_box, DOWN, buff=1)
        ontology_text = TextWrapper('Ontology (TBox)', font_size=20).next_to(bar, UP, aligned_edge=LEFT).shift(RIGHT)
        data_text = TextWrapper('Data (ABox)', font_size=20).next_to(bar, UP, aligned_edge=RIGHT).shift(LEFT)
        
        # ontology axiom
        axiom = MathTexWrapper(
            r'\begin{array}{c}'
            r'\exists \text{hasProbability}.\top'
            r'\sqcap \\'
            r'\exists \text{hasSeverity}.\top'
            r'\sqsubseteq {\color{blue}\textit{RiskLevel}}'
            r'\end{array}'
        ).next_to(ontology_text, DOWN, aligned_edge=LEFT, buff=1)
        

        # graph 
        rl = labeled_node('...', [3,-1,0], color=BLACK)
        sev = labeled_node('...', [6, -1, 0], color=BLACK)
        rls_edge = edge_between(rl, sev, out_dir=RIGHT, in_dir=LEFT, label_text='hasSeverity', font_size=20)
        prob = labeled_node('...', [3, -3, 0], color=BLACK)
        rlp_edge = edge_between(rl, prob, out_dir=DOWN, in_dir=UP, label_text='hasProbability', font_size=20)
        risk_level_label = TexWrapper(r'{\color{blue}\textit{RiskLevel}}').next_to(rl,UP,buff=0.25)
        
        s = self.slide

        s.wait()
        s.next_slide()
        s.play(DrawBorderThenFill(def_box))

        s.next_slide()
        s.play(DrawBorderThenFill(bar), Write(ontology_text), Write(data_text))
        # s.play(DrawBorderThenFill(data_text))
        s.next_slide()

        s.play(Write(axiom))

        s.next_slide()
        # s.next_slide()
        graph = VGroup(rl, prob, sev, rlp_edge, rls_edge)
        s.play(DrawBorderThenFill(graph))
                
        self.slide.next_slide()

        self.slide.play(
            Indicate(axiom[0][0:17], color=HIGH_COLOR, scale_factor=1.05),   
            Indicate(axiom[0][18:32], color=HIGH_COLOR, scale_factor=1.05)    
        )
        self.slide.wait()
        self.slide.next_slide()
        self.slide.play(*ind_edge(rls_edge), *ind_edge(rlp_edge), Indicate(rl, color=GREEN_PASTEL))
        
        self.slide.next_slide()

        self.slide.play(Write(risk_level_label))
        
        

class SemEncRules1Scene(Slide):  
    def construct(self):
        SemEncRules1(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()