from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('Conclusion') + 1


class SemConclusion(BaseSlide):
    TITLE = r'Wrap-up'

    def create_content(self):
        s = self.slide

        logo = ImageMobject("img/riskman-doc.png") \
            .scale(.35) \
            .to_corner(UR)
        
        s.add(logo)  # for some reason something caches

        conc_title = TextWrapper("Conclusions", font_size=32, 
                                #  color=D_BLUE
                                 )\
            .to_corner(UL).shift(DOWN*0.8 + RIGHT*0.5)
        fw_title = TextWrapper("Future Work", font_size=32, 
                            #    color=LAT_ORANGE
                               )\
            .next_to(conc_title, DOWN, buff=2.75)

        # --- Tighter, slide-friendly bullets (sans-serif + bold labels)
        conclusions = BulletedList(
            r'\sffamily  \textbf{\textsc{Riskman}:} OWL~EL ontology + SHACL constraints',
            r'\sffamily  \textbf{Digitization:} RMFs encoded as a RDFa files',
            r'\sffamily  \textbf{Readability:} human- and machine-readable RMFs are ensured',
            r'\sffamily  \textbf{Two pillars:} reasoning derives implicit knowledge; SHACL validates compliance',
            font_size=30, color=BLACK, buff=0.2
        ).next_to(conc_title, DOWN, buff=0.4).align_to(conc_title, LEFT)

        future_work = BulletedList(
            r'\sffamily  \textbf{Integration:} AIRO (AI Act), NCIt, SNOMED',
            r'\sffamily  \textbf{Beyond completeness:} assess assurance quality',
            r'\sffamily  \textbf{Usability:} explain SHACL violations and suggest fixes',
            # r'\sffamily  \textbf{Unification:} combine OWL inference and SHACL validation',
            font_size=30, color=BLACK, buff=0.2
        ).next_to(fw_title, DOWN, buff=0.4).align_to(fw_title, LEFT)

        s.add(conc_title)
        s.wait()
        s.next_slide()

        for item in conclusions:
            s.play(FadeIn(item, shift=RIGHT))
            s.next_slide()

        s.play(FadeIn(fw_title))
        s.next_slide()

        for item in future_work:
            s.play(FadeIn(item, shift=RIGHT))
            s.next_slide()


class SemConclusionScene(Slide):
    def construct(self):
        SemConclusion(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
