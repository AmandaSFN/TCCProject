class Knn_Algoritm:
        
        def TrainAI (dataToTrain):
                from sklearn.model_selection import train_test_split
                from sklearn.neighbors import KNeighborsClassifier
                X = dataToTrain.drop('Start', axis=1)
                y = dataToTrain['Start']
                X_train,X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30)
                knn = KNeighborsClassifier(n_neighbors=3)
                knn.fit(X_train, y_train)
                return knn
        
       
        def PredictData(inputedData, trainedAI):
             return int (trainedAI.predict(inputedData))   


        
        