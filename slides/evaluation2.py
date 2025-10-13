import textwrap
from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper, get_tex_template, IconDocument
import pandas as pd

import slides.evaluation1 as ev1 

from slides.shared.slide_count import SLIDES, SLIDES_NO
# SLIDE_NO = SLIDES.index('Initial') + 1
SLIDE_NO = 9



# ---------- Your slide ----------
class Evaluation2(BaseSlide):
    TITLE = 'Evaluation (2) (TODO)'

    def create_content(self):
        s = self.slide

        Y_LENGTH, X_LENGTH = 5, 5

        aspforaba_df = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.ASP_FOR_ABA])
        flexable_df  = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.FLEXABLE])
        msdis_df     = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.MS_DIS])
        flex_a05_df  = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.FLEXABLE_A_05])
        flex_a25_df  = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.FLEXABLE_A_25])
        ms_a05_df    = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.MS_DIS_A_5])
        ms_a10_df    = ev1.load_and_sort(ev1.RESULT_PATHS[ev1.MS_DIS_A_10])

        ax = Axes(
            y_range=[0, 430, 100], x_range=[0, 700, 100],
            x_length=X_LENGTH, y_length=Y_LENGTH, tips=True,
            axis_config={"include_numbers": True, "font_size": 28, "color": BLACK},
        ).to_edge(RIGHT).shift(LEFT*.5)
        ax.add_coordinates().set_color(BLACK)

        # labels = ax.get_axis_labels(x_label=TexWrapper(r'\textit{t[s]}', color=GREY).scale(0.8).shift(DOWN*10), y_label=TexWrapper(r"\textit{n[\#]}", color=GREY).scale(0.8).shift(DOWN+LEFT))
        # ax.add(labels)
        x_lbl = TexWrapper(r'\textit{t[s]}', color=GREY).scale(0.8).next_to(ax.x_axis, RIGHT, buff=0.1).shift(DOWN*0.1+LEFT*0.1)
        y_lbl = TexWrapper(r'\textit{n[\#]}', color=GREY).scale(0.8).next_to(ax.y_axis, UP, buff=0.1).shift(LEFT*0.1+DOWN*0.1)
        ax.add(x_lbl, y_lbl)
        grid = NumberPlane(
            x_range=ax.x_range, y_range=ax.y_range,
            x_length=ax.x_axis.get_length(), y_length=ax.y_axis.get_length(),
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.25},
            axis_config={"stroke_opacity": 0},
        )
        grid.shift(ax.c2p(0, 0) - grid.c2p(0, 0))
        FONT_SIZE = 14

        flex_plot, flex_lbl   = ev1.create_plot(flexable_df, ax, ev1.FLEXABLE_COLOR, 'solid', ev1.FLEXABLE_COLOR, ev1.FLEXABLE_COLOR, WHITE, 510, ev1.FLEXABLE, font_size=FONT_SIZE)
        ms_plot, ms_lbl       = ev1.create_plot(msdis_df, ax, ev1.MSDIS_COLOR, 'solid', ev1.MSDIS_COLOR, ev1.MSDIS_COLOR, WHITE, 540, ev1.MS_DIS, font_size=FONT_SIZE)
        asp_plot, asp_lbl     = ev1.create_plot(aspforaba_df, ax, ev1.ASPFORABA_COLOR, 'solid', ev1.ASPFORABA_COLOR, ev1.ASPFORABA_COLOR, WHITE, 450, ev1.ASP_FOR_ABA, font_size=FONT_SIZE)
        fa25_plot, fa25_lbl   = ev1.create_plot(flex_a25_df, ax, ev1.FLEXABLE_COLOR, 'dashed', ev1.FLEXABLE_COLOR, WHITE, ev1.FLEXABLE_COLOR, 200, ev1.FLEXABLE_A_25, font_size=FONT_SIZE)
        ma10_plot, ma10_lbl   = ev1.create_plot(ms_a10_df, ax, ev1.MSDIS_COLOR, 'dashed', ev1.MSDIS_COLOR, WHITE, ev1.MSDIS_COLOR, 550, ev1.MS_DIS_A_10, font_size=FONT_SIZE)
        fa05_plot, fa05_lbl   = ev1.create_plot(flex_a05_df, ax, ev1.FLEXABLE_COLOR, 'dashed', ev1.FLEXABLE_COLOR, WHITE, ev1.FLEXABLE_COLOR, 220, ev1.FLEXABLE_A_05, font_size=FONT_SIZE)
        ma05_plot, ma05_lbl   = ev1.create_plot(ms_a05_df, ax, ev1.MSDIS_COLOR, 'dashed', ev1.MSDIS_COLOR, WHITE, ev1.MSDIS_COLOR, 265, ev1.MS_DIS_A_5, font_size=FONT_SIZE)

        s.add(
            grid, ax,
            flex_plot, flex_lbl,
            ms_plot, ms_lbl,
            asp_plot, asp_lbl,
            fa25_plot, fa25_lbl,
            ma05_plot, ma05_lbl,
            ma10_plot, ma10_lbl,
            fa05_plot, fa05_lbl,
        )

        # HERE the table
        table_placeholder = TexWrapper(r'Here will be the table', font_size=30).to_edge(LEFT)

        s.add(table_placeholder)

        s.wait()


class Evaluation2Scene(Slide):
    def construct(self):
        Evaluation2(self, show_footer=True,
                slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()


if __name__ == '__main__':
    Evaluation2Scene().construct()
