from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 7


class ABAExample(BaseSlide):
    TITLE = r'ABA Example (TODO)'

    def create_content(self):
        s = self.slide

        bullets = BulletedList(
            r'\sffamily -- show visually a few step of the dispute',
            # r'\sffamily (1) initialization (the entire base)',
            # r'\sffamily (2) update state (explain and maybe show visually culprits, defences, blocked pieces)',
            # r'\sffamily (3) possible moves',
            # r'\sffamily (4) new pieces from the performed moves',
            # r'\sffamily (5) termination criteria',
            # r'\sffamily (6) choice of next move',

            # r'\sffamily -- show AF (from previous slide)',
            # r'\sffamily -- go line by line and show what is encoded and how this corresponds to AF components',
            # r'\sffamily -- also show the various parts (base, updateState, step)',
            # r'\sffamily -- explain what dispute state is in AF',
            # r'\sffamily -- lightweight, modular, declarative, extensible implementation',
            # r'\sffamily -- advance ABA disputes',
            # r'\sffamily -- propose our approach as general methodology for argument games',
            font_size=30, color=BLACK, buff=0.2)

        s.add(bullets)
        s.wait()


class AbaExampleScene(Slide):
    def construct(self):
        ABAExample(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
