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


.PHONY: %
%:
	@lc=$$(echo $@ | tr '[:upper:]' '[:lower:]'); \
	cap=$$(echo $@ | awk '{print toupper(substr($$0,1,1)) tolower(substr($$0,2))}'); \
	PYTHONPATH=. manim slides/$$lc.py $$cap"Scene"; \
	PYTHONPATH=. manim-slides $$cap"Scene"





# manim slides all
# manim-slides convert SemTitleScene gorczyca-semantics.pdf
# manim-slides convert SemTitle SemTitle.html

# manim-slides SemTitleScene SemMotivationScene SemCurrentPracticesScene SemRiskmanMethodScene SemGraphEncodingScene SemEncRules1Scene SemEncRules2Scene SemReasoningValidationScene SemMoreShaclScene SemRiskmanStatsScene SemHumanReadabilityScene SemVideoScene SemConclusionScene  