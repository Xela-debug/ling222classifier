library(tidyverse)

annotated <- read_csv("Desktop/LING 222/annotated2.csv")
counted <- group_by(annotated, Classification) |>
  summarise(Count = n()) |>
  mutate(Class = recode(Classification, i = "interj.", v = "verb", n = "noun",
                        d = "det.", c = "conj.", p = "prep.",
                        neg = "neg.", aj = "adj.", "ad" = "adv.",
                        nv = "contr.", vp = "contr."))

plot <- ggplot(counted,
                      aes(x = fct_reorder(Class, Count, .desc = TRUE),
                          y = Count)) +
  geom_bar(stat = "identity") +
  labs(x = "Classification",
       y = "Count",
       title = "Classification of 50 Utterances of 2;07.24")

show(plot)

