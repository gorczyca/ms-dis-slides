from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.common import boxed, labeled_node, edge_between, ind_edge

from slides.shared.colors import HIGH_COLOR, GREEN_PASTEL, D_BLUE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('EncRules3') + 1

class SemEncRules3(BaseSlide):
    TITLE = r'The \textsc{Riskman} Ontology: Encoding Rules (3)' 
    def create_content(self):
        
        s = self.slide
        
        according = TexWrapper('According to ISO 14971:').move_to([-6,2.5,0], aligned_edge=LEFT)
        
        p1_def = TexWrapper(r'$P_1$ -- probability of a hazardous situation occurring', font_size=30)
        p2_def = TexWrapper(r'$P_2$ -- probability that the hazardous situation leads to harm', font_size=30).next_to(p1_def, DOWN, buff=6, aligned_edge=LEFT)
        p_def = TexWrapper(r'$P=P_1\times P_2$ -- overall probability of harm', font_size=30).next_to(p2_def, DOWN, buff=6, aligned_edge=LEFT)
        def_box = boxed(p1_def, p2_def, p_def, color=BLACK, buff=0.15).move_to([0,1.25,0], aligned_edge=ORIGIN)

        
        bar = Line(LEFT, RIGHT).scale(6).set_stroke(BLACK, 2).next_to(def_box, DOWN, buff=1)
        ontology_text = TextWrapper('Ontology (TBox)', font_size=20).next_to(bar, UP, aligned_edge=LEFT).shift(RIGHT)
        data_text = TextWrapper('Data (ABox)', font_size=20).next_to(bar, UP, aligned_edge=RIGHT).shift(LEFT)
        s.add(according, def_box)

        s.wait()
        s.next_slide()
        s.play(DrawBorderThenFill(bar), Write(ontology_text), Write(data_text))

        
        axiom = MathTexWrapper(
            r'\begin{array}{c}'
            r'\exists \text{hasProbability1}.\{\text{V}\} \sqcap \\'
            r'\exists \text{hasProbability2}.\{\text{IV}\} \sqsubseteq \\'
            r'{\color{blue}\exists \textit{hasProbability}.\{\textit{III}\}}\quad'
            r'\end{array}'
        ).next_to(ontology_text, DOWN, aligned_edge=LEFT, buff=1)

        s.wait()
        s.next_slide()
        s.play(Write(axiom))

        # graph 
        rl = labeled_node('...', [3,-1,0], color=BLACK)
        p1 = labeled_node('V', [6, -1, 0], color=BLACK)
        rlp1_edge = edge_between(rl, p1, out_dir=RIGHT, in_dir=LEFT, label_text='hasProbability1', font_size=20)
        p2 = labeled_node('IV', [3, -3, 0], color=BLACK)
        rlp2_edge = edge_between(rl, p2, out_dir=DOWN, in_dir=UP, label_text='hasProbability2', font_size=20)
        
        graph = VGroup(rl, p1, rlp1_edge, p2, rlp2_edge)

        s.next_slide()
        s.play(DrawBorderThenFill(graph))

        s.next_slide()
        s.play(
            Indicate(axiom[0][0:20], color=HIGH_COLOR, scale_factor=1.05),   # first part
            Indicate(axiom[0][21:42], color=HIGH_COLOR, scale_factor=1.05)    # last part
        )

        s.next_slide()
        s.play(*ind_edge(rlp1_edge), *ind_edge(rlp2_edge), Indicate(rl, color=GREEN_PASTEL, scale_factor=1.05), Indicate(p1, color=GREEN_PASTEL, scale_factor=1.05), Indicate(p2, color=GREEN_PASTEL, scale_factor=1.05))

        p = labeled_node('III', [0,-1,0], color=D_BLUE)
        rlp_edge = edge_between(rl, p, out_dir=LEFT, in_dir=RIGHT, label_text='hasProbability', font_size=20, color=D_BLUE)
        s.next_slide()
        s.play(Create(p), Create(rlp_edge))       
        
        
        
        
class SemEncRules3Scene(Slide):  
    def construct(self):
        SemEncRules3(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()