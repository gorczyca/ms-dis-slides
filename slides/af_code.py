from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 4


class AFCode(BaseSlide):
    TITLE = r'AF Code (TODO)'

    def create_content(self):
        s = self.slide

        bullets = BulletedList(
            r'\sffamily -- show both Python and ASP code',
            r'\sffamily -- replace ASP code with block diagram',
            r'\sffamily -- show AF (from previous slide)',
            r'\sffamily -- go line by line and show what is encoded and how this corresponds to AF components',
            r'\sffamily -- also show the various parts (base, updateState, step)',
            # r'\sffamily -- lightweight, modular, declarative, extensible implementation',
            # r'\sffamily -- advance ABA disputes',
            # r'\sffamily -- propose our approach as general methodology for argument games',
            font_size=30, color=BLACK, buff=0.2)

        s.add(bullets)
        s.wait()


class AfCodeScene(Slide):
    def construct(self):
        AFCode(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
