from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import TextWrapper, TableWrapper, TexWrapper

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('HumanReadability') + 1

def col_lab(tex): return TexWrapper(tex, font_size=20)

class SemHumanReadability(BaseSlide):
    TITLE = r'The \textsc{Riskman} Ontology: Human Readability'

    def create_content(self):
        s = self.slide

        old_lines = [
            '<tr>',
            '  <td> ',
            '     1.',
            '  </td> ',
            '<tr>',
            '  <td> ',
            '     Loss of consciousness...',
            '  </td> ',
            '...',
            '</tr>',
        ]
        new_lines = [
            '<tr prefix="">',
            '  <td resource="cr1">',
            '     1.',
            '     <link property="riskman:hasAnalysedRisk" href="ar1"/>',
            '  </td> ',
            '  <td resource="ar1"> ',
            '     <span property="rdfs:comment">',
            '        Loss of consiousness...</span> ',
            '     </span>',
            '  </td> ',
            ' ... ',
            '</tr>',
        ]

        code_left = Code(
            code_string="\n".join(old_lines),
            language="html", formatter_style="monokai",
            tab_width=2, add_line_numbers=True, background="rectangle",
        ).scale(0.55).to_edge(LEFT)

        code_left_new = Code(
            code_string="\n".join(new_lines),
            language="html", formatter_style="monokai",
            tab_width=2, add_line_numbers=True, background="rectangle",
        ).scale(0.55).move_to(code_left, aligned_edge=LEFT)

        s.play(FadeIn(code_left))

        # smaller browser on the right
        win_w, win_h, bar_h = 4.6, 2.8, 0.35
        frame = RoundedRectangle(width=win_w, height=win_h, corner_radius=0.05).to_edge(RIGHT).set_stroke(GRAY, 2)
        titlebar = Rectangle(width=win_w, height=bar_h).move_to(frame.get_top() + DOWN*bar_h/2).set_fill(GRAY, 0.15).set_stroke(width=0)
        body = Rectangle(width=win_w, height=win_h - bar_h).next_to(titlebar, DOWN, buff=0).align_to(frame, LEFT).set_fill(WHITE, 1).set_stroke(width=0)
        dots = VGroup(
            Circle(0.08).set_fill(RED, 1).set_stroke(width=0).move_to(titlebar.get_left() + RIGHT*0.3),
            Circle(0.08).set_fill(YELLOW, 1).set_stroke(width=0).move_to(titlebar.get_left() + RIGHT*0.6),
            Circle(0.08).set_fill(GREEN, 1).set_stroke(width=0).move_to(titlebar.get_left() + RIGHT*0.9),
        )
        title = TexWrapper("Web Browser", font_size=18).move_to(titlebar.get_center() + UP*0.02)
        browser_group = VGroup(frame, body, titlebar, dots, title).shift(UP*1.5)

        pad = 0.18
        table = TableWrapper(
            [[r'\text{Loss of consciousness\ldots}', r'\ldots']],
            col_labels=[
                col_lab(r'Analysed\\ risk'),
                col_lab(r'\ldots'),
            ],
            row_labels=[col_lab("1.")],
            top_left_entry=col_lab(r'Ctr.\\ risk'),
            font_size=18,
            max_width=2.5
        )

        target_w = body.width - 2*pad
        target_h = body.height - 2*pad
        table.set(width=target_w)
        if table.height > target_h:
            table.scale(target_h / table.height)
        table.move_to(body.get_center())
        s.wait()
        s.next_slide()
        
        s.play(GrowFromCenter(browser_group))
        
        s.next_slide()
        browser_group.add(table)
        s.play(DrawBorderThenFill(table))

        s.next_slide()
        s.play(ReplacementTransform(code_left, code_left_new))

        s.next_slide()
        code = Code(
            code_string='''
@prefix : <https://w3id.org/riskman/ontology> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:cr1 :hasAnalysedRisk [
        rdfs:comment "Loss of consciousness..."
    ] ;
    ...
.
''',
            language="turtle",      # or "python" if no Turtle lexer
            background="rectangle",
            tab_width=2,
        ).scale(0.5).next_to(browser_group, DOWN).shift(LEFT*.5)

        s.play(Create(code))

class SemHumanReadabilityScene(Slide):
    def construct(self):
        SemHumanReadability(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
