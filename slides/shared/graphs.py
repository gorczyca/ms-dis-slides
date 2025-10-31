from re import S
from turtle import width
from webbrowser import Opera
from manim import *
from manim_slides import Slide
import numpy as np

from pygments import highlight
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


def fixed_arrow_graph(n1, n2, tip_h=0.2, tip_w=0.16, stroke=2, color=BLACK):
    get_pt = lambda x: x.get_center() if hasattr(x, "get_center") else np.array(x, dtype=float)
    c1, c2 = get_pt(n1), get_pt(n2)
    v = c2 - c1
    u = normalize(v)
    ang = angle_of_vector(v)
    p1 = n1.point_at_angle(ang) if hasattr(n1, "point_at_angle") else c1
    p2 = n2.point_at_angle(ang + PI) if hasattr(n2, "point_at_angle") else c2
    end = p2 - u * tip_h
    shaft = Line(p1, end, color=color, stroke_width=stroke)
    w = rotate_vector(u, PI / 2) * (tip_w / 2)
    base_center = end
    apex = end + u * tip_h
    tip = Polygon(apex, base_center - w, base_center + w).set_fill(color, 1).set_stroke(width=0)
    return VGroup(shaft, tip)
