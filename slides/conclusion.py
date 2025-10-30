from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 12


class Conclusion(BaseSlide):
    TITLE = r'Conclusion (TODO)'

    def create_content(self):
        s = self.slide

        bullets = BulletedList(
            r'\sffamily -- summarize the work',
            r'\sffamily -- say we have also variant for different semantics',
            r'\sffamily -- we also have graphical interface, interactive',
            r'\sffamily -- future work',
            font_size=30, color=BLACK, buff=0.2)

        s.add(bullets)
        s.wait()


class ConclusionScene(Slide):
    def construct(self):
        Conclusion(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
