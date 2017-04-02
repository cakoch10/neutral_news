dtable <- read.table('alldata.txt',header=FALSE,sep = "%")

df <- data.frame(dtable)

df$V1

dFR <- df[df$V1 == '_*0',]
dFL <- df[df$V1 == '_*1',]
dM <- df[df$V1 == '_*2',]
dCR <- df[df$V1 == '_*3',]
dCL <- df[df$V1 == '_*4',]


dFR1 <- dFR
dFR1$V1<-NULL
dFR1$ind <- NULL

dFL2 <- dFL
dFL2$V1<-NULL

dM2 <- dM
dM2$V1<-NULL

dCR2 <- dCR
dCR2$V1<-NULL

dCL2 <- dCL
dCL2$V1<-NULL

dFR1$V2 <- substring(dFR1$V2, 29)
dFL2$V2 <- substring(dFL2$V2, 2)
dM2$V2 <- substring(dM2$V2, 2)
dCR2$V2 <- substring(dCR2$V2, 2)
dCL2$V2 <- substring(dCL2$V2, 2)

max.len = max(length(dFR1$V2), length(dFL2$V2),length(dM2$V2),length(dCR2$V2),length(dCL2$V2))
dFR1$V2 = c(dFR1$V2, rep(NA, max.len - length(dFR1$V2)))
dFL2$V2 = c(dFL2$V2, rep(NA, max.len - length(dFL2$V2)))
dM2$V2 <- c(dM2$V2, c(rep(NA, max.len-length(dM2$V2) )))

dCR2$V2 = c(dCR2$V2, rep(NA, max.len - length(dCR2$V2)))
dCL2$V2 = c(dCL2$V2, rep(NA, max.len - length(dCL2$V2)))

dFR3 = c(dFR1$V2, rep(NA, max.len - length(dFR1$V2)))


#insert all dataframes in list to manipulate
myls <- list(dFR1$V2,dFL2$V2,dM2$V2,dCR2$V2,dCL2$V2)

#maximum number of rows
max.len = max(length(dFR1$V2), length(dFL2$V2),length(dM2$V2),length(dCR2$V2),length(dCL2$V2))

#insert the needed `NA`s to each dataframe
new_myls <- lapply(myls, function(x) { x[1:max.len] })


#create  wanted dataframe
do.call(cbind, lapply(new_myls, '[', "accepted"))

finalDF<-as.data.frame(new_myls)
colnames(finalDF)<-c("FarRight","FarLeft","Moderate","CenterRight","CenterLeft")

##MAKE THE FINAL DATA FRAME
# FINALDATAFRAME <- data.frame(dFR1$V2,dFL2$V2,dM2$V2,dCR2$V2,dCL2$V2)
# 
# final <- makePaddedDataFrame(dFR1$V2,dFL2$V2,dM2$V2,dCR2$V2,dCL2$V2)
# 
# colnames(FINALDATAFRAME) <- 
# 
# dtable$V1
# h = c("FarRight","FarLeft","Moderate","CenterRight","CenterLeft")
# 
# require(reshape2)

melt(dFR)

df = data.frame()
library(data.table)

d2<-dcast(setDT(dFR)[, ind:= 1:.N ,.(dFR$V1)],dFR$V1~ind, value.var=names(dFR)[0:1])
d2<-dcast(setDT(dFR)[, ind:= 1:.N ,.(dFR$V1)],dFR$V1~ind, value.var=names(dFR)[1:1])


write.table(finalDF, "C:/Users/Dell/Documents/final_table.csv", sep=",", row.names = FALSE)

#####################################################

#LET'S START MACHINE LEARING!!

dtMatrix <- create_matrix(list(finalDF$FarRight,finalDF$FarLeft,finalDF$Moderate,finalDF$CenterRight,finalDF$CenterLeft))
container <- create_container(dtMatrix, colnames(finalDF), trainSize=1:235, virgin=FALSE)

docs <- Corpus(VectorSource(finalDF))
docsTDM <- TermDocumentMatrix(docs)
docsdissim <- dist(as.matrix(docsTDM), method = "cosine")

h <- hclust(docsdissim, method = "ward")
plot(h, labels = colnames(finalDF), sub = "")





# load libraries
library(caret)
library(mlbench)
library(randomForest)
# load dataset
data("final_table.csv")
set.seed(7)
# create 80%/20% for training and validation datasets
validation_index <- createDataPartition(colnames(finalDF), p=0.80, list=FALSE)
validation <- finalDF[-validation_index,]
training <- finalDF[validation_index,]
# train a model and summarize model
set.seed(7)
control <- trainControl(method="repeatedcv", number=10, repeats=3)
fit.rf <- train(Class~., data=training, method="rf", metric="Accuracy", trControl=control, ntree=2000)
print(fit.rf)
print(fit.rf$finalModel)
# create standalone model using all training data
set.seed(7)
finalModel <- randomForest(Class~., training, mtry=2, ntree=2000)
# make a predictions on "new data" using the final model
final_predictions <- predict(finalModel, validation[,1:60])
confusionMatrix(final_predictions, validation$Class)















