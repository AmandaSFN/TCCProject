class MongoDBClass():
    
    from pymongo import MongoClient
    
    client = MongoClient("mongodb+srv://TCC-UNIP:tccdaunip2021@cluster0.oagef.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        
    def ConnectCollection_IA_DATABASE_TRAINING():    
        db = MongoDBClass.client.TCC
        collection = db.IA_DATABASE_TRAINING
        return collection
    
    def InsertMongoDBCollection_IA_DATABASE_TRAINING(document):
        
        collection = MongoDBClass.ConnectCollection_IA_DATABASE_TRAINING()
        collection.insert_one(document) 
    
    def ImportIADatabase():
        import pandas
        collection = MongoDBClass.ConnectCollection_IA_DATABASE_TRAINING()
        #db = client.TCC
        #collection = db.IA_DATABASE_TRAINING
        docs_mongo = collection.find()
        docs = pandas.DataFrame(columns=[
            'storm',
            'snow',
            'hail',
            'rain',
            'fog',
            'clear_day',
            'clear_night',
            'cloud',
            'cloudly_day',
            'cloudly_night',
            'none_day',
            'none_night',
            'Current Umidity'])

        for num, doc in enumerate( docs_mongo ):
            doc["_id"] = str(doc["_id"])
            doc_id = doc["_id"]
            series_obj = pandas.Series(doc, name=doc_id)
            docs = docs.append( series_obj )


        docs.drop('_id', axis=1).to_csv("Export_IA_Traning.csv", index=False)
    
    def ReturnDocument(data):
        document = {
             'storm': finalData[0],
             'snow': finalData[1],
             'hail': finalData[2],
             'rain': finalData[3],
             'fog': finalData[4],
             'clear_day': finalData[5],
             'clear_night': finalData[6],
             'cloud': finalData[7],
             'cloudly_day': finalData[8],
             'cloudly_night': finalData[9],
             'none_day': finalData[10],
             'none_night': finalData[11],
             'Current Umidity': finalData[12],
             'Start' : finalData[13]
             }
        return document