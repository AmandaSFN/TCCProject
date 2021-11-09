import Knn_Algoritm
import FileFunctions
import APIRequests
import DataProcessing
import Automacao
import MongoDBClass
import pandas


knn = Knn_Algoritm.Knn_Algoritm
file = FileFunctions.FileFunctions
api = APIRequests.APIRequests
dataP = DataProcessing.DataProcessing
automacao = Automacao.Automacao
mongoDbClass = MongoDBClass.MongoDBClass



#Exporta dados da collection IA do Mongo DB para CSV
mongoDbClass.ImportIADatabase()

#Obtem Arquivo de Treinamento para IA
dbToTrain = file.SearchFile('Export_IA_Traning.csv')

#Treina a IA
trainedAI = knn.TrainAI(dbToTrain)

#Obtem dados de Meteorologia da API
currentForecast = api.CurrentForeacast('https://api.hgbrasil.com/weather')

#Mede a Umidade do solo
currentUmidity = automacao.MedirUmidadeDoSolo()

#Formata Input de Dados para criar Predição
dataP.FormatData(currentForecast, currentUmidity)

#Cria o arquivo CSV com os dados para Predição
dataP.SaveCurrentData(file, 'CurrentValues.csv')

#Obtem dados para Predição
dataToPredict = file.SearchFile('CurrentValues.csv')

#Prediz a resposta com base no dado informado e na IA treinada
predictedValue = knn.PredictData(dataToPredict, trainedAI)

#Adiciona o Valor retornado da IA nos dados de Predição
finalData = dataP.SaveProcessedData(file, predictedValue)

#Cria um documento apartir do finalData
newDocument = ReturnDocument(finalData)

#Insere o documento no MongoDB
mongoDbClass.InsertMongoDBCollection_IA_DATABASE_TRAINING(newDocument)



automacao.AcionarRele(predictedValue,5)



