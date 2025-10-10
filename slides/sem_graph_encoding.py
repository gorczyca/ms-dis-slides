from copy import deepcopy
import textwrap

from manim import *
from manim_slides import Slide
from manim.mobject.geometry.arc import ArcBetweenPoints


from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TableWrapper
from slides.shared.colors import HIGHLIGHT_COLORS

from slides.shared.common import labeled_node, edge_between


from manim.mobject.geometry.line import Line

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('GraphEncoding') + 1

CODE_PATH = 'code-assets/rdf-initial.ttl'
PGREEN = HIGHLIGHT_COLORS['green']


def col_lab(tex):
    return TexWrapper(tex, font_size=20)


COL_LABELS = [
    col_lab(r'Analysed\\ risk'),
    col_lab(r'Hazard\\ '),
    col_lab(r'Init.\\ P1'),
    # col_lab(r'Foreseeable sequence\\ of events'),
    # col_lab(r'Hazardous\\ situation'),
    # col_lab(r'Init.\\ P2'),
    # col_lab(r'Harm\\ '),
    # col_lab(r'Init.\\Sev.'),
    # col_lab(r'Mitigation\\ '),
    # col_lab(r'Res.\\ P'),
    # col_lab(r'Res. \\Sev'),
    col_lab(r'\ldots')
]

ORIGINAL_ROW = [
    r'Loss of consciousness due to an alarm malfunction',
    r'Non-audio alarm malfunctions',
    r'V',
    # r'(1) Vibration mechanism fails, (2) Vibration cannot be felt',
    # r'No insulin delivered',
    # r'IV',
    # r'Loss of consciousness',
    # r'4',
    # r'Implement an alternative alerting system',
    # r'V',
    # r'4',
    r'...'
]



class SemGraphEncoding(BaseSlide):
    TITLE = 'Risk Management File -- RDF Graph encoding'

    def create_content(self):

        # full table
        table = TableWrapper(
            [ORIGINAL_ROW],
            col_labels=COL_LABELS,
            row_labels=[col_lab("1.")],
            font_size=18,
            top_left_entry=col_lab(r'Ctr.\\ risk'),
            max_width=2.5
        )

        table.scale(1.0).to_edge(UP).shift(DOWN)
        self.slide.add(table)

        self.slide.wait()
        self.slide.next_slide()

        # highlight rows
        row = 2  # 1 = header
        n_cols = len(table.get_columns())
        cells = [table.get_cell((row, j)) for j in range(1, n_cols + 1)]

        hl = SurroundingRectangle(
            cells[0], color=PGREEN, stroke_width=6, buff=0).set_z_index(10)
        self.slide.add(hl)
        self.slide.play(GrowFromEdge(hl,LEFT), run_time=0.3)
        self.slide.next_slide()

        centr_x, centr_y = 0, -1.5
        y_delta = 1
        x_delta = 3

        positions = [
            # [centr_x, centr_y, ORIGIN, ''],
            [centr_x-x_delta, centr_y+y_delta, RIGHT, 'hasAnalysedRisk'],
            [centr_x-x_delta, centr_y, RIGHT, 'hasHazard'],
            [centr_x-x_delta, centr_y-y_delta, RIGHT, 'hasInitialP1'],
            # [centr_x+x_delta, centr_y+y_delta,  LEFT, 'hasSequenceOfEvents'],
            # [centr_x+x_delta, centr_y,  LEFT, 'hasHazardousSituation'],
            # [centr_x+x_delta, centr_y+y_delta,  LEFT, '...'],
            [centr_x+x_delta, centr_y,  LEFT, '...'],
            # [centr_x+x_delta, centr_y-y_delta,  LEFT, '...'],
            # [centr_x+x_delta, centr_y-y_delta,  LEFT, '...'],
        ]

        central_node = labeled_node('1', [centr_x, centr_y, 0])
        self.slide.play(Create(central_node[0]), FadeIn(central_node[1]))
        self.slide.next_slide()
        graph_elems = [central_node]

            
        for i,(x,y,al_edge,edge_label) in enumerate(positions): # range(1, len(positions)+1):
            
            # if i < len(positions):
            text = ORIGINAL_ROW[i]
            c = cells[i+1]
            tgt = SurroundingRectangle(c, color=PGREEN, stroke_width=6, buff=0)
            self.slide.play(Transform(hl, tgt), run_time=0.5)
                # pass
            # else:
                # self.slide.play(FadeOut(hl))
                # text = r'...'


            # x, y, edge, edge_label = positions[i]
            
            if  np.allclose(al_edge, LEFT):
                out_dir = RIGHT 
                in_dir = LEFT
            else:
                out_dir = LEFT
                in_dir = RIGHT
            
            n = labeled_node(text, [x, y, 0], aligned_edge=al_edge)
            self.slide.play(Create(n[0]), FadeIn(n[1]))
            
            # edge = elbow_edge(central_node, n, up=0.9, bend=0.2)
            edge = edge_between(central_node, n, out_dir=out_dir, in_dir=in_dir, label_text=edge_label)
            self.slide.play(Create(edge[0]), Create(edge[1]))
            # self.slide.play(Create(edge))
            
            graph_elems += [n,edge]

            self.slide.next_slide()


        self.slide.play(FadeOut(hl))

        # self.slide.play(FadeOut(hl), run_time=0.2)
        self.slide.play(VGroup(*graph_elems).animate.scale(0.8).shift(LEFT*2))
        
        self.slide.next_slide()
        
        code = Code(
            code_file=CODE_PATH,
            language="turtle",      # or "python" if no Turtle lexer
            background="rectangle",
            tab_width=2,
        ).scale(0.4).move_to([6.5, centr_y, 0], aligned_edge=RIGHT)

        self.slide.play(GrowFromCenter(code)) #.add(code)
        


class SemGraphEncodingScene(Slide):
    def construct(self):
        SemGraphEncoding(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
