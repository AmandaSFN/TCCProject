class APIRequests(object):
   
    def RequestCurrentForecast(url):
        import requests
        response = requests.get(url)
        if APIRequests.IsValidResponse(response):
            return response
        else: return 
  
    def IsValidResponse(response):
        if response.status_code == 200:
            return True
        else:
            return False

    def CurrentForeacast(url):
        return APIRequests.RequestCurrentForecast(url).json()['results']['condition_slug']
