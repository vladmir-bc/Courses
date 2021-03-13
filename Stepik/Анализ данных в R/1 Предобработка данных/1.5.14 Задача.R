library(psych)
df <- iris
describe(df)
descr <- describeBy(x = df, group = df$Species)
