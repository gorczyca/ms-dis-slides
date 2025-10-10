from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.common import boxed, labeled_node, edge_between
from slides.shared.colors import HIGHLIGHT_COLORS

from slides.shared.videoMObject import VideoMobject

VID_PATH = 'videos/demo.mp4'
HIGH_COLOR = HIGHLIGHT_COLORS['green']

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('Video') + 1

class SemVideo(BaseSlide):
    TITLE = r'The \textsc{Riskman} Workflow: Demo'

    def create_content(self):


        # self.slide.wait()
        # self.slide.next_slide()

        video1 = VideoMobject(
            filename=VID_PATH,
            speed=1.
        )

        video1.stretch_to_fit_width(10.75)
        video1.stretch_to_fit_height(5.5)

        code_bg = Code(
            code_string="\n".join([f"  \td                         d                        d\t  " for i in range(1, 15)]),
            language="text",
            background="window",
            add_line_numbers=False,
        )

        # self.slide.toggle_reverse(False)

        code_bg.move_to([0,0,0], aligned_edge=ORIGIN)
        video1.move_to([0,0,0], aligned_edge=ORIGIN).shift(DOWN*.2)

        # self.slide.play(DrawBorderThenFill(code_bg), DrawBorderThenFill(video1))

        self.slide.add(Group(code_bg, video1))
        self.slide.wait(0.07)
        self.slide.next_slide() # stop ASAP


        self.slide.wait(4) 
        self.slide.next_slide()
        self.slide.wait(4) 
        self.slide.next_slide() # live preview shown


        self.slide.wait(4) 
        self.slide.next_slide()
        self.slide.wait(4) 
        self.slide.next_slide()
        self.slide.wait(4) 
        self.slide.next_slide()  # finish writing


        self.slide.wait(4) # hide preview 
        self.slide.next_slide()
        self.slide.wait(4) 
        self.slide.next_slide() # show graph
        self.slide.wait(2) # 
        self.slide.next_slide()

        
        self.slide.wait(4) # start reasoning
        self.slide.next_slide()
        self.slide.wait(4) 
        self.slide.next_slide()


        self.slide.wait(4) # start reasoning
        self.slide.next_slide()
        self.slide.wait(4) 
        self.slide.next_slide()

        #  we want to circumscribe around the error message to draw attention to it
        rect = Rectangle(width=3.5, height=1).move_to([1.75, -2, 0], aligned_edge=UL)
        rect.set_stroke(opacity=0).set_fill(opacity=0)  # invisible
        self.slide.add(rect)
        self.slide.play(Circumscribe(rect, color=HIGH_COLOR))



# to be run as standalone
class SemVideoScene(Slide):
    def construct(self):
        SemVideo(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
