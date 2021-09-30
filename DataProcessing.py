class DataProcessing:
    data = ['storm','snow','hail','rain','fog','clear_day','clear_night','cloud','cloudly_day','cloudly_night','none_day','none_night','Current Umidity']
    forecastValues = [0,0,0,0,0,0,0,0,0,0,0,0,0.0]

    def FormatData (currentCondition, currentUmidity):
        currentConditionIndex = DataProcessing.data.index(currentCondition)
        DataProcessing.forecastValues[currentConditionIndex] = 1
        DataProcessing.forecastValues[12] = currentUmidity
        
    def SaveCurrentData(file, fileName):
        file.SaveNewArrayIntoCsvFile(DataProcessing.data, fileName)
        file.SaveArrayIntoCsvFIle(DataProcessing.forecastValues, fileName)


    def SaveProcessedData(file ,value):
        return file.AddInputedDataWithItsResult(DataProcessing.forecastValues, value)


