from re import S
from turtle import width
from webbrowser import Opera
from manim import *
from manim_slides import Slide

from pygments.lexers.prolog import PrologLexer
from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Number, String, Operator, Punctuation, Comment, Text
# from pygments.lexers import register
import manim.mobject.text.code_mobject as cm
import pygments.lexers as pyg_lex


from pygments.style import Style
from pygments.styles import get_style_by_name, STYLE_MAP

from pathlib import Path
from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper, TexWrapper, TextWrapper
from slides.shared.colors import D_BLUE, LAT_ORANGE




from slides.shared.slide_count import SLIDES, SLIDES_NO
SLIDE_NO = 4

class ASPLexer(RegexLexer):
    name = "ASP"; aliases = ["asp","clingo"]; filenames = ["*.lp"]
    tokens = {
        "root": [
            (r"%.*?$", Comment.Single),
            (r"#(show|const|include|program|external|minimize|maximize|heuristic)\b", Keyword),
            # (r"(not|#count|#sum|#min|#max|#int)\b", Keyword),
            (r"(#count|#sum|#min|#max|#int)\b", Keyword),
            # (r":-|-->|<-|==|!=|<=|>=|=|\+|-|\*|/", Operator),
            (r"[A-Z][A-Za-z0-9_]*", Name.Variable),
            (r"[a-z][A-Za-z0-9_]*", Name),
            (r"\d+", Number),
            (r'"[^"]*"', String),
            # (r"[(),.\[\]{};:<>]", Punctuation),
            (r"[(),.\[\]{}]", Operator),
            (r"\s+", Text),
        ],
    }

_orig = pyg_lex.get_lexer_by_name
def _asp_get(alias, **opts):
    return ASPLexer(**opts) if alias.lower() in ("asp","clingo") else _orig(alias, **opts)


pyg_lex.get_lexer_by_name = _asp_get
cm.get_lexer_by_name = _asp_get



STYLE_MAP["aspvs"] = "__main__:ASPVSStyle"   # register alias
setattr(cm, "DEFAULT_CODE_STYLE", "aspvs")   # force Code's default style
setattr(cm, "DEFAULT_STYLE", "aspvs")        # (covers other versions)

# style = get_style_by_name("one-dark")
# style.styles[Punctuation] = "#7aa2f7"  # brighter blue for parens

def create_code_block(code, a, b, color=YELLOW, opacity=0.05, pad=0.04):
    lines = code.code_lines
    chunk = VGroup(*lines[a-1:b])
    r = SurroundingRectangle(chunk, buff=pad).set_fill(color, opacity).set_stroke(width=0)
    r.stretch_to_fit_width(code.width).align_to(code, LEFT)
    return r
    # return VGroup(*[
    #     SurroundingRectangle(ln, buff=0.00)
    #     .set_fill(YELLOW, opacity=0.0)
    #     .set_stroke(width=0)
    #     .stretch_to_fit_width(bg_w)
    #     .align_to(code, LEFT)
    #     for ln in lines
    # ])



class AFCode(BaseSlide):
    TITLE = r'AF Code (TODO)'

    def create_content(self):
        s = self.slide

        code = Code(
            tab_width=2,
            code_string=Path("./code/af.lp").read_text(encoding="utf-8"),
            language='asp',
            # line_spacing=0.7,        # tighter vertically
            formatter_style='one-dark'  # tried with perldoc, gruvbox-dark, vs, dracula, one-dark, monokai, nord-darker, paraiso-dark, solarized-dark, coffee, github-dark, stata-dark
            ).set(width=7).to_edge(LEFT)

        s.add(code)

        # --- sliding highlight setup ---
        # lines = getattr(code, "code_lines", code.code)


        self._active = VGroup(); s.add(self._active)

        def show_step(ranges, on=0.25, rt=0.3, pad=0.04):
            if len(self._active):
                s.play(*[r.animate.set_opacity(0) for r in self._active], run_time=rt/2)
                s.remove(self._active)
            if len(ranges):
                new_rects = VGroup(*[create_code_block(code, a, b, opacity=on, pad=pad) for a, b in ranges])
                for r in new_rects: r.set_opacity(0)
                s.add(new_rects)
                s.play(*[r.animate.set_opacity(on) for r in new_rects], run_time=rt)
                self._active = new_rects

        # usage
        s.next_slide(); show_step([(1, 1)])
        #
        s.next_slide(); show_step([(5, 5)])
        #
        s.next_slide(); show_step([(17, 17)])
        #
        s.next_slide(); show_step([])  # clear

        # # 
        s.next_slide(); show_step([(3, 3)])
        s.next_slide(); show_step([(6, 6)])
        s.next_slide(); show_step([(7, 9)])
        s.next_slide(); show_step([(10, 11)])
        s.next_slide(); show_step([(12, 13)])
        s.next_slide(); show_step([(14, 15)])
        s.next_slide(); show_step([(18, 18)])
        s.next_slide(); show_step([(19, 19)])
        s.next_slide(); show_step([])  # clear


class AfCodeScene(Slide):
    def construct(self):
        AFCode(self, show_footer=True, slide_no=SLIDE_NO, slide_total=SLIDES_NO)
        self.wait()
