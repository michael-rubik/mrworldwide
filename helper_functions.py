def checkContainsError(response):
    if response.contains("error"):
        
        print("Something went wrong with the api request!")
        print("Error message: ", response)