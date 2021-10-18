def companyBotStrategy(trainingData):
    correctAnswers=[trainingData[i][0] for i in range(len(trainingData)) if trainingData[i][1]==1]
    if len(correctAnswers)!=0: 
        return sum(correctAnswers)/len(correctAnswers)
    else: return 0