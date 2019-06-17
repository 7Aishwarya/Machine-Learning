#Data preprocessing

#Set working directory
dataset = read.csv('Data.csv')

#Used only when some data is missing
#taking care of missing data
#dataset$Age = ifelse(is.na(dataset$Age),ave(dataset$Age,FUN=function(x) mean(x, na.rm=TRUE)),dataset$Age)
#dataset$Salary = ifelse(is.na(dataset$Salary),ave(dataset$Salary,FUN=function(x) mean(x, na.rm=TRUE)),dataset$Salary)

#Used only when encoding of the categorical data is required
#encoding categorical data
#dataset$Country = factor(dataset$Country,
#                       levels = c('France','Spain','Germany'),
#                       labels = c(1,2,3))
#dataset$Purchased=factor(dataset$Purchased,
#                         levels=c('No','Yes'),
#                         labels=c(0,1))

#splitting the dataset into training set and test set
#install.packages('ca.Tools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

#Used if the libraries do not apply feature scaling
#Feature scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[,2:3])



