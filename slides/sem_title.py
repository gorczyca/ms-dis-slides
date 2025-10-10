from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper
from slides.shared.colors import HIGHLIGHT_COLORS

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 0

class SemTitle(BaseSlide):
    TITLE = ''
    def create_content(self):
        title = TexWrapper(
            r'\raggedright Supporting Risk Management for Medical Devices via\\'
            r'the \textsc{Riskman} Ontology \& Shapes',
            font_size=55, 
            color=HIGHLIGHT_COLORS['green']
            # tex_template=TexWrapper.TEX_TEMPLATE
        ).to_edge(UP).shift(DOWN)        

        bar = Line(LEFT, RIGHT).scale(6).set_stroke(BLACK, 2).next_to(title, DOWN, aligned_edge=LEFT)


        authors = TexWrapper(r'\raggedright \textbf{Piotr Gorczyca}, Dörthe Arndt, Martin Diller, Jochen Hampe, Georg Heidenreich, Pascal Kettmann, Markus Krötzsch, Stephan Mennicke, Sebastian Rudolph, Hannes Straß').next_to(bar, DOWN, aligned_edge=LEFT, buff=0.5)
        
        venue_and_date = TexWrapper(r'\raggedright LogAI Seminar -- 25th September 2025', font_size=32).next_to(authors, DOWN, aligned_edge=LEFT, buff=0.8)
        

        # images
        tud = ImageMobject("./img/logo/TU_Logo_blau.png").scale_to_fit_width(2).to_corner(DL)
        kimeds = ImageMobject("img/logo/KIMEDS_Logo.png").scale_to_fit_width(1.5).next_to(tud, RIGHT, buff=1.5).shift(UP*0.25)
        # kimeds = ImageMobject("./img/logo/KIMEDS_Logo.png").scale_to_fit_width(2).to_corner(DL) 
        bmftr = ImageMobject("img/logo/bmftr.png").scale_to_fit_width(2.5).to_corner(DR).shift(DOWN*.5+RIGHT*0.25)
        iccl = ImageMobject("img/logo/iccl_logo.png").scale_to_fit_width(3.5).next_to(bmftr, LEFT, buff=0.6) 
            

        self.slide.add(tud, title, authors, venue_and_date, kimeds, bmftr, iccl, bar)
        
        
# to be run as standalone
# i.e. by only `manim slide2.py Slide2Scene`
class SemTitleScene(Slide):  
    def construct(self):
        SemTitle(self, show_footer=False, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()