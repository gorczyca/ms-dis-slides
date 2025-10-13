from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 1


class BigPicture(BaseSlide):
    TITLE = r'Big Picture (TODO)'

    def create_content(self):
        s = self.slide

        big_pic_bullets = BulletedList(
            r'\sffamily -- explain there is AFs and ABA',
            r'\sffamily -- high-level description of the problem',
            r'\sffamily -- visual intuition',
            font_size=40, color=BLACK, buff=0.2)

        s.add(big_pic_bullets)
        s.wait()


class BigPictureScene(Slide):
    def construct(self):
        BigPicture(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
