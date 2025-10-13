from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 3


class ExampleAF(BaseSlide):
    TITLE = r'Example AF Dispute (TODO)'

    def create_content(self):
        s = self.slide

        bullets = BulletedList(
            r'\sffamily -- show interactive, step by step AF dispute',
            # r'\sffamily -- lightweight, modular, declarative, extensible implementation',
            # r'\sffamily -- advance ABA disputes',
            # r'\sffamily -- propose our approach as general methodology for argument games',
            font_size=40, color=BLACK, buff=0.2)

        s.add(bullets)
        s.wait()


class ExampleAfScene(Slide):
    def construct(self):
        ExampleAF(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
