import Knn_Algoritm
import FileFunctions
import APIRequests
import DataProcessing


knn = Knn_Algoritm.Knn_Algoritm
file = FileFunctions.FileFunctions
api = APIRequests.APIRequests
dataP = DataProcessing.DataProcessing

currentForecast = api.CurrentForeacast('https://api.hgbrasil.com/weather')

dbToTrain = file.SearchFile('./src/modules/Plantation/UseCases/GetPlantation/AI_DataBase.csv')
trainedAI = knn.TrainAI(dbToTrain)


currentUmidity = 0.4
dataP.FormatData(currentForecast, currentUmidity)
dataP.SaveCurrentData(file, './src/modules/Plantation/UseCases/GetPlantation/CurrentValues.csv')

dataToPredict = file.SearchFile('./src/modules/Plantation/UseCases/GetPlantation/CurrentValues.csv')


predictedValue = knn.PredictData(dataToPredict, trainedAI)

finalData = dataP.SaveProcessedData(file, predictedValue)

file.SaveArrayIntoCsvFIle(finalData,'./src/modules/Plantation/UseCases/GetPlantation/AI_DataBase.csv')

print(predictedValue)


