from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper
import slides.shared.colors as custom_colors

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 0

class Title(BaseSlide):
    TITLE = ''
    def create_content(self):


        s = self.slide

        bg = SVGMobject('img/logo/tud-logo.svg')
        bg.set_color(custom_colors.PRIMARY_COLOR)
        bg.move_to(ORIGIN, aligned_edge=ORIGIN).scale(15).shift(RIGHT*1.25+UP*7)
        # bg.to_edge(UP)

        # dispute = SVGMobject("img/aba.svg").scale_to_fit_height(3).move_to(ORIGIN)
        # dispute = SVGMobject("img/aba_plain.svg")\
            # .set_fill(opacity=1).set_stroke(width=1, opacity=1)\
            # .scale_to_fit_width(1.5).next_to(bg, RIGHT, buff=1.5).shift(UP*0.25)



        s.add(bg)



        # title = TexWrapper(
        #     # r'\raggedright Supporting Risk Management for Medical Devices via\\'
        #     # r'the \textsc{Riskman} Ontology \& Shapes',
        #     r'\raggedright ABA Disputes in ASP:\\' ,
        #     # r'Advancing Argument Games through Multi-Shot Solving',
        #     font_size=50, 
        #     color=custom_colors.PRIMARY_COLOR,
        #     # tex_template=TexWrapper.TEX_TEMPLATE
        # ).to_edge(LEFT).shift(DOWN * 2)   

        title = TexWrapper(
            # r'\raggedright Supporting Risk Management for Medical Devices via\\'
            # r'the \textsc{Riskman} Ontology \& Shapes',
            r'\raggedright  \setstretch{0.5}\textbf{ABA Disputes in ASP}:\\' ,
            r'Advancing Argument Games \\ ' \
            r'through Multi-Shot Solving',
            # r'Advancing Argument Games through Multi-Shot Solving',
            font_size=50, 
            color=WHITE,
            # tex_template=TexWrapper.TEX_TEMPLATE
        # ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.0)  
        ).to_edge(LEFT).shift(DOWN * 2)      



        # bar = Line(LEFT, RIGHT).scale(6).set_stroke(BLACK, 2).next_to(title, DOWN, aligned_edge=LEFT)

        authors = TexWrapper(r'\raggedright \textbf{Martin Diller}, Piotr Gorczyca', color=WHITE, font_size=32).next_to(title, DOWN, aligned_edge=LEFT, buff=0.3)
        venue_and_date = TexWrapper(r'\raggedright NMR @ KR2025 -- 11th November 2025', color=WHITE, font_size=32).next_to(authors, DOWN, aligned_edge=LEFT, buff=0)

        # images
        tud = ImageMobject("./img/logo/TUD_Logos_final_RGB_TUD_Logo_horizontal_weiß_de.png").scale_to_fit_width(3.5).to_corner(UL).shift(UP*0.5+LEFT*0.5)
        iccl = ImageMobject("img/logo/iccl_logo.png").scale_to_fit_width(3.5).to_corner(DR).shift(RIGHT*0.5) 


        # kimeds = ImageMobject("img/logo/KIMEDS_Logo.png").scale_to_fit_width(1.5).next_to(tud, RIGHT, buff=1.5).shift(UP*0.25)
        # bmftr = ImageMobject("img/logo/bmftr.png").scale_to_fit_width(2.5).to_corner(DR).shift(DOWN*.5+RIGHT*0.25)
            

        self.slide.add(tud, title, authors, venue_and_date, iccl)
        
        
# to be run as standalone
# i.e. by only `manim slide2.py Slide2Scene`
class TitleScene(Slide):  
    def construct(self):
        Title(self, show_footer=False, slide_no=SLIDE_NO, slide_total=SLIDES_NO, show_logo=False)
        self.wait()