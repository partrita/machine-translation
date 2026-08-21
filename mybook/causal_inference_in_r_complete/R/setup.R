# Setup script sourced by the setup-main chunk in
# causal-inference-in-r-complete.qmd

# Chapter status helper (draft / polishing / complete)
status <- function(state = NULL) {
  invisible(NULL)
}

# Okabe-Ito / viridis defaults + book theme (see "Theming" section)
options(
  ggplot2.discrete.colour = ggokabeito::palette_okabe_ito(),
  ggplot2.discrete.fill = ggokabeito::palette_okabe_ito(),
  ggplot2.continuous.colour = "viridis",
  ggplot2.continuous.fill = "viridis",
  book.base_family = "sans",
  book.base_size = 14
)

library(ggplot2)

theme_set(
  theme_minimal(
    base_size = getOption("book.base_size"),
    base_family = getOption("book.base_family")
  ) %+replace%
    theme(
      panel.grid.minor = element_blank(),
      legend.position = "bottom"
    )
)
