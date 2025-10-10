from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper, TableWrapper
from slides.shared.common import boxed, labeled_node, edge_between, ind_edge

from slides.shared.colors import HIGH_COLOR, GREEN_PASTEL, D_BLUE, LAT_ORANGE


from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('ReasoningValidation') + 1

def col_lab(tex):
    return TexWrapper(tex, font_size=20)


COL_LABELS = [
    col_lab(r'Analysed\\ risk'),
    # col_lab(r'Hazard\\ '),
    col_lab(r'\ldots \\ \ldots'),
    col_lab(r'Init.\\ P1'),
    # col_lab(r'Foreseeable sequence\\ of events'),
    col_lab(r'\ldots \\ \ldots'),
    # col_lab(r'Hazardous\\ situation'),
    col_lab(r'\ldots \\ \ldots'),
    col_lab(r'Init.\\ P2'),
    col_lab(r'Harm\\ '),
    col_lab(r'Init.\\Sev.'),
    col_lab(r'Mitigation\\ '),
    col_lab(r'Res.\\ P'),
    col_lab(r'Res. \\Sev'),
    col_lab(r'\ldots \\ \ldots')
]

ORIGINAL_ROW = [
    r'Loss of consciousness due to an alarm malfunction',
    # r'Non-audio alarm malfunctions',
    r'\ldots',
    r'V',
    # r'(1) Vibration mechanism fails, (2) Vibration cannot be felt',
    r'\ldots',
    # r'No insulin delivered',
    r'\ldots',
    r'IV',
    r'Loss of consciousness',
    r'4',
    r'Implement an alternative alerting system',
    r'V',
    r'4',
    r'\ldots'
]




class SemReasoningValidation(BaseSlide):
    TITLE = r'\textsc{Riskman}: Reasoning \& Validation' 
    def create_content(self):
        
        # self.show_grid()

        s = self.slide

        # 
        table = TableWrapper(
            [ORIGINAL_ROW],
            col_labels=COL_LABELS,
            row_labels=[col_lab("1.")],
            font_size=18,
            top_left_entry=col_lab(r'Ctr.\\ risk'),
            max_width=2.5
        )

        table.scale(1.0).to_edge(UP).shift(DOWN)
        s.add(table)
        
        
        # ontology axiom
        axiom_1 = MathTexWrapper(
            r'\begin{array}{c}'
            r'\exists \text{hasProbability}.\top'
            r'\sqcap \\'
            r'\exists \text{hasSeverity}.\top'
            r'\sqsubseteq {\color{blue}\textit{RiskLevel}}'
            r'\end{array}'
        ).to_edge(UP).shift(DOWN)

        axiom_2 = MathTexWrapper(
            r'\begin{array}{c}'
            r'\exists \text{hasRiskLevel}.\top \sqcap \\'
            r'\exists \text{hasHarm}.\top \sqsubseteq {\color{blue}\textit{Risk}}'
            r'\end{array}'
        ).to_edge(UP).shift(DOWN)
        
        axiom_3 = MathTexWrapper(
            r'\begin{array}{c}'
            r'\exists \text{hasProbability1}.\{\text{V}\} \sqcap \\'
            r'\exists \text{hasProbability2}.\{\text{IV}\} \sqsubseteq \\'
            r'{\color{blue}\exists \textit{hasProbability}.\{\textit{III}\}}'
            r'\end{array}'
        ).to_edge(UP).shift(DOWN)


        Y_DELTA = 1.15
        X_DELTA = 2.5
        CR_POS_X = -5
        CR_POS_Y = -1.8

        cr = labeled_node('"1."', [CR_POS_X,CR_POS_Y,0], color=BLACK, aligned_edge=ORIGIN)
        rrl = labeled_node(' ', [CR_POS_X,CR_POS_Y+Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        # rrlp = labeled_node('V', [CR_POS_X,CR_POS_Y+2*Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        # rrls = labeled_node('4', [CR_POS_X-1.5*X_DELTA,CR_POS_Y+Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)

        sda = labeled_node('"Implement ...', [CR_POS_X,CR_POS_Y-Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        ar = labeled_node('"Loss of ... due to...', [CR_POS_X+2*X_DELTA,CR_POS_Y,0], color=BLACK, aligned_edge=ORIGIN)
        # hazard = labeled_node('"Non-audio alarm', [CR_POS_X+2*X_DELTA,CR_POS_Y,0], color=BLACK, aligned_edge=ORIGIN)
        irl = labeled_node(' ', [CR_POS_X+2*X_DELTA,CR_POS_Y+Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        prob4 = labeled_node('IV', [CR_POS_X+3*X_DELTA,CR_POS_Y+2*Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        prob5 = labeled_node('V', [CR_POS_X+1*X_DELTA,CR_POS_Y+2*Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        sev = labeled_node('4', [CR_POS_X+1*X_DELTA,CR_POS_Y+1*Y_DELTA,0], color=BLACK, aligned_edge=ORIGIN)
        h = labeled_node('"Loss of consciousness"', [CR_POS_X+3.5*X_DELTA,CR_POS_Y,0], color=BLACK, aligned_edge=ORIGIN)
        
        
        # irlp2 = labeled_node('1.', [CR_POS_X+2*X_DELTA,CR_POS_Y+Y_DELTA,0], color=BLACK)
        cr_rrl = edge_between(cr, rrl, out_dir=UP, in_dir=DOWN, label_text='hasResidualRiskLevel', font_size=20)
        cr_sda = edge_between(cr, sda, out_dir=DOWN, in_dir=UP, label_text='isMitigatedBy', font_size=20)
        rrl_rrlp = edge_between(rrl, prob5, out_dir=UP, in_dir=DOWN, label_text='hasProbability', font_size=20)
        rrl_rrls = edge_between(rrl, sev, out_dir=RIGHT, in_dir=LEFT, label_text='hasSeverity', font_size=20)
        cr_ar = edge_between(cr, ar, out_dir=RIGHT, in_dir=LEFT, label_text='hasAnalysedRisk', font_size=20)
        ar_h = edge_between(ar, h, out_dir=RIGHT, in_dir=LEFT, label_text='hasHarm', font_size=20)
        ar_irl = edge_between(ar, irl, out_dir=UP, in_dir=DOWN, label_text='hasInitialRiskLevel', font_size=20)
        irl_irlp1 = edge_between(irl, prob5, out_dir=UP, in_dir=DOWN, label_text='hasProbability1', font_size=20)
        irl_irlp2 = edge_between(irl, prob4, out_dir=UP, in_dir=DOWN, label_text='hasProbability2', font_size=20)
        irl_irls = edge_between(irl, sev, out_dir=LEFT, in_dir=RIGHT, label_text='hasSeverity', font_size=20)
        
        init_graph = VGroup(cr, rrl, 
              sev, 
              sda, ar, irl, prob4, h, prob5, cr_rrl, cr_sda, rrl_rrlp, 
              rrl_rrls, 
              cr_ar, ar_h, ar_irl, irl_irlp1, irl_irlp2, 
              irl_irls, 
              )
        
        s.wait()
        s.next_slide()
        s.play(DrawBorderThenFill(init_graph))
        # s.play(ShowIncreasingSubsets(init_graph))


        s.next_slide()
        s.play(FadeOut(table))

        # s.play()
        s.next_slide()
        s.play(Write(axiom_3))

        s.next_slide()
        s.play(
            Indicate(axiom_3[0][0:20], color=HIGH_COLOR, scale_factor=1.05),   
            Indicate(axiom_3[0][21:42], color=HIGH_COLOR, scale_factor=1.05),
            *ind_edge(irl_irlp1), *ind_edge(irl_irlp2), 
            Indicate(irl, color=GREEN_PASTEL, scale_factor=1.05), Indicate(prob4[0], color=GREEN_PASTEL, scale_factor=1.05), Indicate(prob5[0], color=GREEN_PASTEL, scale_factor=1.05)
        )

        s.next_slide()
        prob3 = labeled_node('III', [CR_POS_X+3.5*X_DELTA,CR_POS_Y+Y_DELTA,0], color=D_BLUE, aligned_edge=ORIGIN)
        irl_irlp = edge_between(irl, prob3, out_dir=RIGHT, in_dir=LEFT, color=D_BLUE, label_text='hasProbability', font_size=20)
        s.play(Create(prob3), Create(irl_irlp))
        # s.play(Create(prob3), Create(irl_irlp))

        s.next_slide()
        s.play(FadeTransform(axiom_3, axiom_1))
        
        s.next_slide()
        s.play(
            Indicate(axiom_1[0][0:17], color=HIGH_COLOR, scale_factor=1.05),   
            Indicate(axiom_1[0][18:32], color=HIGH_COLOR, scale_factor=1.05),
            *ind_edge(irl_irls), *ind_edge(irl_irlp), Indicate(irl, color=GREEN_PASTEL)
            # *ind_edge(rrl_rrls), *ind_edge(rrl_rrlp), Indicate(rrl, color=GREEN_PASTEL)    
        )
        s.play(
            *ind_edge(rrl_rrlp), *ind_edge(rrl_rrls), Indicate(rrl, color=GREEN_PASTEL)
        )

        rrl_label = TexWrapper(r'{\color{blue}\textit{RiskLevel}}', font_size=20).next_to(rrl,UP,buff=0.25).shift(LEFT*.35+DOWN*.15)
        irl_label = TexWrapper(r'{\color{blue}\textit{RiskLevel}}', font_size=20).next_to(irl,RIGHT,buff=0.1).shift(DOWN*.3)
        
        s.next_slide()
        s.play(Write(rrl_label), Write(irl_label))

        s.next_slide()
        s.play(FadeTransform(axiom_1, axiom_2))

        s.next_slide()
        s.play(
            Indicate(axiom_2[0][0:15], color=HIGH_COLOR, scale_factor=1.05),   # first part
            Indicate(axiom_2[0][16:26], color=HIGH_COLOR, scale_factor=1.05),    # last part
            *ind_edge(ar_irl), *ind_edge(ar_h), Indicate(ar[0], color=GREEN_PASTEL)
        )


        s.next_slide()
        r_label = TexWrapper(r'{\color{blue}\textit{Risk}}', font_size=20).next_to(ar,DOWN,buff=0.1)
        s.play(Write(r_label))

        s.next_slide()
        s.play(FadeOut((axiom_2)))

        s.next_slide()

        entity_title = TexWrapper('SHACL',  font_size=20, color=LAT_ORANGE)
        definition = MathTexWrapper(r'\text{Risk} \Rightarrow {\color{shaclCol} \exists\text{hasInitialRiskLevel}\cdot\text{hasProbability}\cdot\text{gt}^{-}\cdot\text{hasProbability}^{-}\neq\cdot\text{hasAnalysedRisk}^{-}\cdot\text{hasResidualRiskLevel}}', font_size=25).next_to(entity_title, DOWN, buff=10, aligned_edge=LEFT)#.shift(DOWN*2)
        expl = TexWrapper(r'\textit{"Residual probability should not be higher than initial probability."}', font_size=25).next_to(definition, aligned_edge=LEFT)

        def_box = boxed(entity_title, definition, expl, width=config.frame_width-1.8,  color=BLACK, buff=0.15).move_to([0,2,0], aligned_edge=ORIGIN)

        s.play(DrawBorderThenFill(def_box))
        s.next_slide()

        s.play(
            prob3[0].animate.set_color(LAT_ORANGE),
            prob3[1].animate.set_color(WHITE),
            # prob5[0].animate.set_color(LAT_ORANGE),
            prob5[0].animate.set_color(LAT_ORANGE),
            prob5[1].animate.set_color(WHITE)
        )


        
        
# to be run as standalone
# i.e. by only `manim slide2.py Slide2Scene`
class SemReasoningValidationScene(Slide):  
    def construct(self):
        SemReasoningValidation(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()