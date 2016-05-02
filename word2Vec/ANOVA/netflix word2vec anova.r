data.reg <- read.csv(file='regression_input.csv', sep=',', header=TRUE)
mod <- lm(avg_rating ~ ., data = data.reg)
ns <- step(mod)
mod1 <- aov(avg_rating ~ X2 + X5 + X14 + X16 + X22 + X24 + X25 + X31 + X36 + 
              X46 + X57 + X58 + X60 + X65 + X67 + X73 + X75 + X78 + X79 + 
              X93 + X94 + X103 + X110 + X111 + X116 + X118 + X119 + X126 + 
              X134 + X137 + X138 + X143 + X144 + X148 + X150 + X158 + X162 + 
              X166 + X168 + X171 + X172 + X173 + X178 + X179 + X181 + X184 + 
              X189 + X196, data = data.reg)
summary(mod1)
summary(ns)
mod2 <- lm(avg_rating ~X189 + X119 + X118 + X111 + X75 + X57,data = data.reg)
summary(mod2)
