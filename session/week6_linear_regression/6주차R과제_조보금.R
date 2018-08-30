library(ggplot2)
library(dplyr)

setwd('C:/Users/USER/Desktop/BOAZ/session/week6_linear_regression/회귀분석+과제')
#1
sales<-read.csv('sales.csv')
head(sales)
#1-(a)
sales %>% ggplot(aes(x,y)) +geom_point()

#1-(b)
lr1 <- lm(y ~ x, sales)
lr1
#1-(c)
summary(lr1)

#2
multiple<-read.csv('multiple.txt',sep = '')
head(multiple)

#2-(a)
multiple %>% ggplot(aes(x1,y)) +geom_point()
multiple %>% ggplot(aes(x2,y)) +geom_point()
pairs(multiple)

#2-(b)
lr2 <- lm(y ~ x1+x2, multiple)
lr2
summary(lr2)
# y bar=62.39738+0.74071*x1-0.08067*x2

#2-(c)
#backward elimination(default)
step(lr2)
#forward selection
step(lr2, direction="forward")
#both
step(lr2, direction='both')
#y=50.2619+0.7347*x1