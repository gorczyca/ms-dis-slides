import textwrap
from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper, get_tex_template, IconDocument
import pandas as pd

from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = SLIDES.index('Initial') + 1


ASP_FOR_ABA = 'aspforaba'
FLEXABLE = 'flexABle'
MS_DIS = 'MS-DIS'
FLEXABLE_A_05 = 'flexABle a=.05'
FLEXABLE_A_25 = 'flexABle a=.25'
FLEXABLE_A_5 = 'flexABle a=.5'
MS_DIS_A_5 = 'MS-DIS a=5'
MS_DIS_A_10 = 'MS-DIS a=10'
MS_DIS_A_25 = 'MS-DIS a=25'

RESULT_PATHS = {
    ASP_FOR_ABA: 'results/aspforaba-adm_iccma_ver.csv',
    FLEXABLE: 'results/flexable-adm_iccma_ver.csv',
    MS_DIS: 'results/msdis-adm_iccma_ver.csv',
    FLEXABLE_A_05: 'results/flexable-adm-app-0.05_iccma_ver.csv',
    FLEXABLE_A_25: 'results/flexable-adm-app-0.25_iccma_ver.csv',
    FLEXABLE_A_5: 'results/flexable-adm-app-0.5_iccma_ver.csv',
    MS_DIS_A_5: 'results/msdis-adm-app-5_iccma_ver.csv',
    MS_DIS_A_10: 'results/msdis-adm-app-10_iccma_ver.csv',
    MS_DIS_A_25: 'results/msdis-adm-app-25_iccma_ver.csv',
}


def load_and_sort(path):
    df = pd.read_csv(path)
    df = df[df['verdict'] != 'TIMEOUT'].sort_values(
        'duration').reset_index(drop=True)
    df['X'] = df.index + 1
    return df


def compute_pos(ax, x, y, x_at):
    x = np.array(x); y = np.array(y)
    y_at = float(np.interp(x_at, x, y))
    p = ax.c2p(x_at, y_at)
    return p



def curve_label(ax, x, y, x_at, text, bg=BLUE_E, fg=WHITE, font="Consolas", offset=UR*0.0,
                border_color=WHITE, border_width=2, border_style="solid"):
    p = compute_pos(ax, x, y, x_at)
    lbl = Text(text, font_size=28, color=fg, font=font)
    w, h = lbl.width + 0.3, lbl.height + 0.2

    fill_box = RoundedRectangle(corner_radius=0.15, width=w, height=h,
                                fill_color=bg, fill_opacity=1, stroke_width=0)
    outline = RoundedRectangle(corner_radius=0.15, width=w, height=h,
                               stroke_color=border_color, stroke_width=border_width, fill_opacity=1)
    if border_style == "dotted":
        outline = DashedVMobject(outline, num_dashes=80, dashed_ratio=0.12)
    elif border_style == "dashed":
        outline = DashedVMobject(outline, num_dashes=30, dashed_ratio=0.5)

    return VGroup(fill_box, outline, lbl).move_to(p).shift(offset)



# ---------- Your slide ----------
class Initial(BaseSlide):
    TITLE = 'Motivation'

    def create_content(self):
        s = self.slide

        aspforaba_df = load_and_sort(RESULT_PATHS[ASP_FOR_ABA])

        flexable_df = load_and_sort(RESULT_PATHS[FLEXABLE])
        msdis_df = load_and_sort(RESULT_PATHS[FLEXABLE])

        #
        flexable_a_05_df = load_and_sort(RESULT_PATHS[FLEXABLE_A_05])
        flexable_a_25_df = load_and_sort(RESULT_PATHS[FLEXABLE_A_25])
        flexable_a_5_df = load_and_sort(RESULT_PATHS[FLEXABLE_A_5])

        #
        msdis_a_05_df = load_and_sort(RESULT_PATHS[MS_DIS_A_5])
        msdis_a_10_df = load_and_sort(RESULT_PATHS[MS_DIS_A_10])
        msdis_a_25_df = load_and_sort(RESULT_PATHS[MS_DIS_A_25])

        ax = Axes(
            x_range=[0, 610, 100],
            y_range=[0, 210, 100],
            tips=True,
            axis_config={"include_numbers": True,
                         "font_size": 28, "color": BLACK},
        )
        coords = ax.add_coordinates()
        coords.set_color(BLACK)


        grid = NumberPlane(
            x_range=ax.x_range,
            y_range=ax.y_range,
            x_length=ax.x_axis.get_length(),
            y_length=ax.y_axis.get_length(),
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.25},
            axis_config={"stroke_opacity": 0},
        )

        grid.shift(ax.c2p(0, 0) - grid.c2p(0, 0))  # pin origins together



        s.play(Create(grid), Create(ax))
        s.next_slide()

        flex_g_x, flex_g_y = flexable_df["duration"], flexable_df["X"]
        flex_g = ax.plot_line_graph(
            flex_g_x, flex_g_y,
            stroke_width=3, line_color=BLUE_E, add_vertex_dots=True,
            vertex_dot_radius=0.03,
            vertex_dot_style={"fill_color": BLACK, "stroke_color": BLACK, "stroke_width": 1},
        )

        flex_g_x_at = 510
        flex_g_label = curve_label(ax, flex_g_x, flex_g_y, x_at=flex_g_x_at, text=FLEXABLE, border_style='solid', border_color=RED, bg=WHITE, fg=RED, offset=UR*0)


        s.play(Create(flex_g), DrawBorderThenFill(flex_g_label))
        s.next_slide()



        #

        new_ax = Axes(
            y_range=[0, 410, 100],
            x_range=[0, 610, 100],
            tips=True,
            axis_config={"include_numbers": True,
                         "font_size": 28, "color": BLACK},
        ).move_to(ax)
        new_coords = new_ax.add_coordinates()
        new_coords.set_color(BLACK)

        new_grid = NumberPlane(
            x_range=new_ax.x_range,
            y_range=new_ax.y_range,
            x_length=new_ax.x_axis.get_length(),
            y_length=new_ax.y_axis.get_length(),
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.25},
            axis_config={"stroke_opacity": 0},
        )

        new_grid.shift(new_ax.c2p(0, 0) - new_grid.c2p(0, 0))  # pin origins together        

        # s.play(Create(grid), Create(ax))


        new_g = new_ax.plot_line_graph(
            flexable_df['duration'], flexable_df['X'], stroke_width=3, line_color=BLUE_E, add_vertex_dots=True,
            vertex_dot_radius=0.03,
            vertex_dot_style={"fill_color": BLACK, "stroke_color": BLACK},
        )

        # move label
        new_flex_g_label_p = compute_pos(new_ax, flex_g_x, flex_g_y, flex_g_x_at)

        s.play(Transform(ax, new_ax), FadeOut(grid), Create(new_grid),  Transform(flex_g, new_g), flex_g_label.animate.move_to(new_flex_g_label_p))

        s.next_slide()
        s.wait()


class InitialScene(Slide):
    def construct(self):
        Initial(self, show_footer=True,
                slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()


if __name__ == '__main__':
    InitialScene().construct()
