# Masked ggdag helpers (see "Theming" section of the book)

theme_dag <- function() {
  ggdag::theme_dag(base_family = getOption("book.base_family"))
}

geom_dag_label_repel <- function(..., seed = 10) {
  ggdag::geom_dag_label_repel(
    aes(x, y, label = label),
    box.padding = 3.5,
    inherit.aes = FALSE,
    max.overlaps = Inf,
    family = getOption("book.base_family"),
    seed = seed,
    label.size = NA,
    label.padding = 0.1,
    size = getOption("book.base_size") / 3,
    ...
  )
}
