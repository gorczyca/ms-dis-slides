from manim import *
from manim_slides import Slide

from slides.shared.wrappers import MathTexWrapper, TexWrapper
from slides.shared.common import highlight_box
from slides.shared.graphs import fixed_arrow_graph, curved_arrow
from slides.shared.base_slide import BaseSlide
from slides.shared.slide_count import SLIDES, SLIDES_NO


class DisputeDiagramAnimator:
    """
    Builds the ABA dispute diagram (your version: z-indices, colors, highlight boxes)
    and provides a looping step-by-step animation over it.
    """
    def __init__(self, pos=ORIGIN):
        self.elems = self._build()
        self.elems["diagram"].move_to(pos)

    def _build(self):
        RADIUS = 0.25
        STROKE_WIDTH = 1
        HOR_DIST = 0.5

        PROP_COLOR = ["#E8FFE8", "#B5FFB5"]
        OPPONENT_COLOR = ["#FFFBE8", "#FFF1B5"]

        # --- NODES ---
        # IMPORTANT: stroke_opacity=1 so Create(...) can draw it
        s_node = Circle(radius=RADIUS, color=WHITE, stroke_opacity=1, fill_opacity=0) \
            .add(MathTexWrapper("s")).set_z_index(999)

        d = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH) \
            .add(MathTexWrapper("d")).set_z_index(99) \
            .next_to(s_node, LEFT, buff=HOR_DIST).shift(UP)
        p = Circle(radius=RADIUS, color=WHITE, stroke_opacity=0, fill_opacity=0) \
            .add(MathTexWrapper("p")).set_z_index(99) \
            .next_to(s_node, LEFT, buff=HOR_DIST)
        a = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH) \
            .add(MathTexWrapper("a")).set_z_index(99) \
            .next_to(s_node, LEFT, buff=HOR_DIST).shift(DOWN)

        xc = Circle(radius=RADIUS, color=WHITE, stroke_opacity=0, fill_opacity=0) \
            .add(MathTexWrapper(r"\bar{c}")).set_z_index(99) \
            .next_to(p, LEFT, buff=HOR_DIST)
        f = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH) \
            .add(MathTexWrapper("f")).set_z_index(99) \
            .next_to(xc, LEFT, buff=HOR_DIST)

        xd = Circle(radius=RADIUS, color=WHITE, stroke_opacity=0, fill_opacity=0) \
            .add(MathTexWrapper(r"\bar{d}")).set_z_index(99) \
            .next_to(f, LEFT, buff=1.5 * HOR_DIST).shift(UP)
        e = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH) \
            .add(MathTexWrapper("e")).set_z_index(99) \
            .next_to(xd, LEFT, buff=HOR_DIST)

        xa = Circle(radius=RADIUS, color=WHITE, stroke_opacity=0, fill_opacity=0) \
            .add(MathTexWrapper(r"\bar{a}")).set_z_index(99) \
            .next_to(f, LEFT, buff=1.5 * HOR_DIST).shift(DOWN)
        b = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH) \
            .add(MathTexWrapper("b")).set_z_index(99) \
            .next_to(xa, LEFT, buff=HOR_DIST).shift(0.5 * UP)
        t = Circle(radius=RADIUS, color=WHITE, stroke_opacity=0, fill_opacity=0) \
            .add(MathTexWrapper("t")).set_z_index(99) \
            .next_to(xa, LEFT, buff=HOR_DIST).shift(0.5 * DOWN)
        c = Circle(radius=RADIUS, color=BLACK, stroke_width=STROKE_WIDTH) \
            .add(MathTexWrapper("c")).set_z_index(99) \
            .next_to(t, LEFT, buff=HOR_DIST)

        xe = Circle(
            radius=RADIUS,
            color=BLACK,
            stroke_width=STROKE_WIDTH,
            fill_color=PROP_COLOR[0],
            fill_opacity=1,
        ).add(MathTexWrapper(r"\bar{e}")).set_z_index(99) \
         .next_to(e, LEFT, buff=HOR_DIST)

        # --- EDGES ---
        edges = VGroup(
            fixed_arrow_graph(d, s_node.get_left() + UP * 0.1, color=BLACK),
            fixed_arrow_graph(p, s_node.get_left(), color=BLACK),
            fixed_arrow_graph(a, s_node.get_left() + DOWN * 0.1, color=BLACK),

            fixed_arrow_graph(xc, p.get_left(), color=BLACK),
            fixed_arrow_graph(f, xc.get_left(), color=BLACK),

            fixed_arrow_graph(e, xd.get_left(), color=BLACK),
            fixed_arrow_graph(xd, d.get_left(), color=RED),

            fixed_arrow_graph(b, xa.get_left() + UP * 0.1, color=BLACK),
            fixed_arrow_graph(t, xa.get_left() + DOWN * 0.1, color=BLACK),
            fixed_arrow_graph(xa, a.get_left(), color=RED),

            fixed_arrow_graph(c, t.get_left(), color=BLACK),

            fixed_arrow_graph(xe, e.get_left(), color=RED),

            curved_arrow(xc.get_bottom(), c.get_right() + 0.1 * DOWN + 0.2 * RIGHT, bend=1, color=RED),
        )

        # --- HIGHLIGHTS ---
        proponent_core = highlight_box(
            VGroup(s_node, d, p, a),
            fill_opacity=1,
            fill_color=PROP_COLOR[0],
            buff=0.1,
            dashed=True
        ).set_z_index(3)

        e_xd_block = highlight_box(
            VGroup(e, xd),
            fill_opacity=1,
            fill_color=OPPONENT_COLOR[0],
            buff=0.1,
            dashed=False
        ).set_z_index(0)

        t_b_xa_block = highlight_box(
            VGroup(t, b, xa),
            fill_opacity=1,
            fill_color=OPPONENT_COLOR[0],
            buff=0.15,
            dashed=True
        ).set_z_index(0)

        c_t_block = highlight_box(
            VGroup(c, t),
            fill_opacity=1,
            fill_color=OPPONENT_COLOR[0],
            buff=0.1,
            dashed=True
        ).set_z_index(5)

        opp_arg_block = highlight_box(
            VGroup(c_t_block, b, xa),
            fill_opacity=1,
            fill_color=OPPONENT_COLOR[0],
            buff=0.2,
            dashed=False
        )

        xc_p_block = highlight_box(
            VGroup(xc, p),
            fill_opacity=1,
            fill_color=PROP_COLOR[0],
            buff=0.15,
            dashed=True
        ).set_z_index(4)

        f_xc_block = highlight_box(
            VGroup(f, xc),
            fill_opacity=1,
            fill_color=PROP_COLOR[0],
            buff=0.1,
            dashed=True
        ).set_z_index(5)

        s_arg_block = highlight_box(
            VGroup(f, s_node, d, a),
            fill_opacity=1,
            fill_color=PROP_COLOR[0],
            buff=0.3,
            dashed=False
        ).set_z_index(0)

        diagram = VGroup(
            s_arg_block,
            e_xd_block,
            t_b_xa_block,
            c_t_block,
            opp_arg_block,
            xc_p_block,
            f_xc_block,
            proponent_core,
            s_node, d, p, a,
            xc, f, xd, e, xa, b, t, c, xe,
            edges,
        )

        return {
            "diagram": diagram,
            "s_node": s_node,
            "d": d,
            "p": p,
            "a": a,
            "xc": xc,
            "f": f,
            "xd": xd,
            "e": e,
            "xa": xa,
            "b": b,
            "t": t,
            "c": c,
            "xe": xe,
            "proponent_core": proponent_core,
            "e_xd_block": e_xd_block,
            "t_b_xa_block": t_b_xa_block,
            "c_t_block": c_t_block,
            "opp_arg_block": opp_arg_block,
            "xc_p_block": xc_p_block,
            "f_xc_block": f_xc_block,
            "s_arg_block": s_arg_block,
            "edges": edges,
        }

    def add_to(self, scene: Scene):
        scene.add(self.elems["diagram"])

    def _hide_all(self):
        # hide everything; arrows lose stroke, nodes/text lose opacity
        for name, m in self.elems.items():
            if not isinstance(m, Mobject):
                continue
            m.set_opacity(0)
            m.set_stroke(opacity=0)

    def _show_full(self, m: Mobject):
        m.set_opacity(1)
        m.set_stroke(opacity=1)
        return m

    def _play_one_pass(self, s: Slide, step_time=0.7):
        e = self.elems

        # 1. center node (now has stroke_opacity=1)
        self._show_full(e["s_node"])
        s.play(Create(e["s_node"]), run_time=step_time)

        return

        # 2. d/p/a
        for k in ("d", "p", "a"):
            self._show_full(e[k])
        s.play(FadeIn(VGroup(e["d"], e["p"], e["a"])), run_time=step_time)

        # 3. proponent core
        self._show_full(e["proponent_core"])
        s.play(e["proponent_core"].animate.set_opacity(1), run_time=step_time)

        # 4. edges
        self._show_full(e["edges"])
        s.play(FadeIn(e["edges"]), run_time=step_time)

        # 5. upper opponent
        self._show_full(e["e"]); self._show_full(e["xd"])
        s.play(FadeIn(VGroup(e["e"], e["xd"])), run_time=step_time)
        self._show_full(e["e_xd_block"])
        s.play(e["e_xd_block"].animate.set_opacity(1), run_time=step_time)

        # 6. lower opponent
        for k in ("xa", "b", "t"):
            self._show_full(e[k])
        s.play(FadeIn(VGroup(e["xa"], e["b"], e["t"])), run_time=step_time)
        self._show_full(e["t_b_xa_block"])
        s.play(e["t_b_xa_block"].animate.set_opacity(1), run_time=step_time)

        # 7. c + opp arg
        self._show_full(e["c"])
        s.play(FadeIn(e["c"]), run_time=step_time)
        self._show_full(e["c_t_block"])
        s.play(e["c_t_block"].animate.set_opacity(1), run_time=step_time)
        self._show_full(e["opp_arg_block"])
        s.play(e["opp_arg_block"].animate.set_opacity(1), run_time=step_time)

        # 8. proponent reply
        self._show_full(e["xc"]); self._show_full(e["f"])
        s.play(FadeIn(VGroup(e["xc"], e["f"])), run_time=step_time)
        self._show_full(e["xc_p_block"])
        s.play(e["xc_p_block"].animate.set_opacity(1), run_time=step_time)
        self._show_full(e["f_xc_block"])
        s.play(e["f_xc_block"].animate.set_opacity(1), run_time=step_time)

        # 9. final attacker
        self._show_full(e["xe"])
        s.play(FadeIn(e["xe"]), run_time=step_time)

        s.wait(step_time)

    def loop(self, s: Slide, loops=5, step_time=0.7):
        for _ in range(loops):
            self._hide_all()
            self._play_one_pass(s, step_time=step_time)
