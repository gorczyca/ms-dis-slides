# Config
MAIN_FILE := slide_deck.py
MAIN_DECK := SlideDeck
SLIDES_DIR := slides

# Default: build and serve full deck
.PHONY: all
all: build serve

.PHONY: build
build:
	manim $(MAIN_FILE) $(MAIN_DECK)

.PHONY: serve
serve:
	manim-slides SlideDeck

.PHONY: html
html:
	manim-slides convert $(MAIN_DECK) $(MAIN_DECK).html

.PHONY: pdf
pdf:
	manim-slides convert $(MAIN_DECK) $(MAIN_DECK).pdf

# Generic single slide build + show: underscore_case -> CamelCase
# Single slide build + show
.PHONY: %

%:
	PYTHONPATH=. manim $(SLIDES_DIR)/$@.py $(shell echo $@ | sed -r 's/(^|_)([a-z])/\U\2/g')Scene && manim-slides $(shell echo $@ | sed -r 's/(^|_)([a-z])/\U\2/g')Scene


# manim slides all
# manim-slides convert SemTitleScene gorczyca-semantics.pdf
# manim-slides convert SemTitle SemTitle.html

# manim-slides SemTitleScene SemMotivationScene SemCurrentPracticesScene SemRiskmanMethodScene SemGraphEncodingScene SemEncRules1Scene SemEncRules2Scene SemReasoningValidationScene SemMoreShaclScene SemRiskmanStatsScene SemHumanReadabilityScene SemVideoScene SemConclusionScene  