install.packages("mlbench")
library(mlbench)

data(BreastCancer, package = "mlbench")
bc <- BreastCancer
str(bc)

bc <- na.omit(bc)          # remove missing cells
bc$Id <- NULL              # drop ID column
bc$Class <- factor(bc$Class, levels = c("B","M"), labels = c(0,1))

num_cols <- setdiff(names(bc), "Class")
bc[num_cols] <- lapply(bc[num_cols], function(x) as.numeric(as.character(x)))


model <- glm(Class ~ Cl.thickness + Cell.size + Marg.adhesion, 
             data = bc, family = binomial)
summary(model)

exp(cbind(OR = coef(model), confint(model)))


pred_prob <- predict(model, type = "response")
pred_class <- factor(ifelse(pred_prob > 0.5, 1, 0), levels = c(0,1))
table(Predicted = pred_class, Actual = bc$Class)


install.packages("pROC")
library(pROC)

roc_obj <- roc(bc$Class, pred_prob)
plot(roc_obj, main = "ROC Curve")
auc(roc_obj)
