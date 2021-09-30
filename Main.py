import Knn_Algoritm
import FileFunctions
import APIRequests
import DataProcessing


knn = Knn_Algoritm.Knn_Algoritm
file = FileFunctions.FileFunctions
api = APIRequests.APIRequests
dataP = DataProcessing.DataProcessing

currentForecast = api.CurrentForeacast('https://api.hgbrasil.com/weather')


dbToTrain = file.SearchFile('AI_DataBase.csv')
trainedAI = knn.TrainAI(dbToTrain)


currentUmidity = 0.7
dataP.FormatData(currentForecast, currentUmidity)
dataP.SaveCurrentData(file, 'CurrentValues.csv')

dataToPredict = file.SearchFile('CurrentValues.csv')


predictedValue = knn.PredictData(dataToPredict, trainedAI)

finalData = dataP.SaveProcessedData(file, predictedValue)

file.SaveArrayIntoCsvFIle(finalData,'AI_DataBase.csv')



