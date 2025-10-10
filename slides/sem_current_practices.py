from copy import deepcopy

from manim import *
from manim_slides import Slide



from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TableWrapper
from slides.shared.colors import HIGHLIGHT_COLORS


from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('CurrentPractices') + 1


def col_lab(tex):
    return TexWrapper(tex, font_size=20)


COL_LABELS = [
    col_lab(r'Analysed\\ risk'),
    col_lab(r'Hazard\\ '),
    col_lab(r'Init.\\ P1'),
    col_lab(r'Foreseeable sequence\\ of events'),
    col_lab(r'Hazardous\\ situation'),
    col_lab(r'Init.\\ P2'),
    col_lab(r'Harm\\ '),
    col_lab(r'Init.\\Sev.'),
    col_lab(r'Mitigation\\ '),
    col_lab(r'Res.\\ P'),
    col_lab(r'Res. \\Sev'),
    col_lab(r'\ldots')
]

ORIGINAL_ROW = [
    r'Loss of consciousness due to an alarm malfunction',
    r'Non-audio alarm malfunctions',
    r'V',
    r'(1) Vibration mechanism fails, (2) Vibration cannot be felt',
    # r'Underdose',
    r'No insulin delivered',
    r'IV',
    r'Loss of consciousness',
    r'4',
    r'Implement an alternative alerting system',
    r'V',
    r'4',
    r'\ldots'
]

CHATGPT_ROWS = [
    [
        r'Overdelivery of insulin due to stuck motor',
        r'Motor control failure',
        r'II',
        r'(1) Motor does not stop, (2) Continuous insulin infusion',
        r'Overdose',
        r'IV',
        r'Hypoglycemia leading to seizure',
        r'V',
        r'Dual motor monitoring, automatic shutoff',
        r'II',
        r'III',
        r'\ldots',
    ],
    [
        r'Underdelivery of insulin due to occlusion',
        r'Catheter blockage',
        r'III',
        r'(1) Kinked tubing, (2) Insulin flow obstructed',
        r'Underdose',
        r'III',
        r'Hyperglycemia, risk of ketoacidosis',
        r'IV',
        r'Pressure sensor with alarm and backup injection option',
        r'II',
        r'III',
        r'\ldots',
    ],
    [
        r'Loss of therapy due to empty reservoir not detected',
        r'Reservoir sensor failure',
        r'II',
        r'(1) User forgets to refill, (2) Sensor fails to alarm',
        r'Underdose',
        r'III',
        r'Severe hyperglycemia',
        r'IV',
        r'Dual sensing, mandatory periodic checks',
        r'II',
        r'III',
        r'\ldots',
    ],
    [
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots',
        r'\ldots'
    ]
]


class SemCurrentPractices(BaseSlide):
    TITLE = 'Current Practices'

    def create_content(self):
        # full table
        table = TableWrapper(
            [ORIGINAL_ROW, *CHATGPT_ROWS],
            col_labels=COL_LABELS,
            row_labels=[*[
                col_lab(rf'{i}.') for i in range(1, len(CHATGPT_ROWS) + 2)
            ]],
            font_size=18,
            top_left_entry=col_lab(r'Ctr.\\ risk'),
            max_width=2.5
        )

        self.slide.add(table)

        self.slide.wait()
        self.slide.next_slide()
        
              
        # highlight rows
        # row = 2  # 1 = header
        # n_cols = len(table.get_columns())
        # cells = [table.get_cell((row, j)) for j in range(1, n_cols + 1)]
        first_cell = table.get_cell((2, 1))

        # persistent outline (no color changes to the table itself)
        PGREEN = HIGHLIGHT_COLORS['green']
        hl = SurroundingRectangle(first_cell[0], color=PGREEN, stroke_width=6, buff=0).set_z_index(10)
        self.slide.add(hl)
        self.slide.play(FadeIn(hl), run_time=0.3)
        self.slide.next_slide()

        for index in [3,6,8,4,7,10,11]:
            c = table.get_cell((2, index))
            tgt = SurroundingRectangle(c, color=PGREEN, stroke_width=6, buff=0)
            self.slide.play(Transform(hl, tgt), run_time=0.5)
            self.slide.next_slide()

        self.slide.play(FadeOut(hl), run_time=0.2)

class SemCurrentPracticesScene(Slide):
    def construct(self):
        SemCurrentPractices(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
