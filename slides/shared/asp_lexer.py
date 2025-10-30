from manim import *
from manim_slides import Slide
from pathlib import Path



from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Number, String, Operator, Comment, Text
# from pygments.lexers import register
import manim.mobject.text.code_mobject as cm
import pygments.lexers as pyg_lex


from pygments.styles import STYLE_MAP


class ASPLexer(RegexLexer):
    name = "ASP"
    aliases = ["asp", "clingo"]
    filenames = ["*.lp"]
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


def set_asp_lexer():
    _orig = pyg_lex.get_lexer_by_name


    def _asp_get(alias, **opts):
        return ASPLexer(**opts) if alias.lower() in ("asp", "clingo") else _orig(alias, **opts)


    pyg_lex.get_lexer_by_name = _asp_get
    cm.get_lexer_by_name = _asp_get


    STYLE_MAP["aspvs"] = "__main__:ASPVSStyle"   # register alias
    setattr(cm, "DEFAULT_CODE_STYLE", "aspvs")   # force Code's default style
    setattr(cm, "DEFAULT_STYLE", "aspvs")        # (covers other versions)


def get_asp_code(code_path, font_size=24, add_line_numbers=False, buff=0.2):
        code = Code(
            tab_width=2,
            code_string=Path(code_path).read_text(encoding="utf-8"),
            language='asp',
            # padding=padding,
            add_line_numbers=add_line_numbers,
            # font_size=font_size,
            paragraph_config={"font_size": font_size},
            background_config={"buff": buff},
            # line_spacing=line_spacing,        # tighter vertically
            formatter_style='one-dark'  # tried with perldoc, gruvbox-dark, vs, dracula, one-dark, monokai, nord-darker, paraiso-dark, solarized-dark, coffee, github-dark, stata-dark
        )
        # code.background..stretch_to_fit_width(width)
        return code