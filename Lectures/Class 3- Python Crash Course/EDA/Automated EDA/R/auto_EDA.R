
library(DataExplorer)
library(tidyverse)
library(fastDummies)
library(wooldridge)

library(skimr)

# DATA ----

df <- wage2
head(df)
str(df)

df[c('married','black')] <- df %>% select(married,black) %>% lapply(factor)
str(df)


df %>% skim()

# Automated EDA Report 

df %>%
  create_report(
    output_file  = "wage_report",
    output_dir   = "wage_eda_R/",
    y            = "wage",
    report_title = "EDA Report - wage data set"
  )


# Done!































# 2.0 Data Introduction ----

df %>% introduce()

df %>% plot_intro()

# 3.0 Missing Values ----

df %>% plot_missing()

df %>% profile_missing()

# 4.0 Continuous Features ----

df %>% plot_density()

df %>% plot_histogram()

# 5.0 Categorical Features ----

df %>% plot_bar()

# 6.0 Relationships ----

df %>% plot_correlation(maxcat = 15)




