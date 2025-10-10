### Installation

```
uv venv .venv   # create environment
source .venv/bin/activate # activate environment 
uv pip install "manim-slides[manim]" #  install manim / manim-slides
uv pip install PySide6
```

### Workflow
For each new slide `slide_x`, create a new script in the `slides/` directory. Make sure it has the following structure and naming convention:

```python
from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide

class SlideX(BaseSlide):
    TITLE = "Hello"

    def create_content(self):
        eq = MathTex(r"E=mc^2", r"\text{not true}" , color=self.FONT_COLOR)
        self.slide.add(eq)
        
        
class SlideXScene(Slide):  
    def construct(self):
        Slide1(self)
        self.wait()
```
then, to view this standalone slide run:
```
make slide_x
```
which should display the standalone slide. Make sure to follow the naming convention, script name in snake case, i.e. `my_first_slide.py`, then the main class name inside `MyFirstSlide` and for running standalone `MyFirstSlideScene` inside of the same script. For reference check [`slides/slide1.py`](slides/slide1.py).

### Showing whole slide deck
Run `make` in the main directory. Make sure to add your slide class in the [`slide_deck.py`](slide_deck,py) `main_slides` array.

