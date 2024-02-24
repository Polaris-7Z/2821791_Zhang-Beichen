# HTTP Error Codes
def errorcode(n):
    match n:
        case 500:
            print("Internal Server Error")
        case 401:
            print("Unauthorised")
        case 400:
            print("Bad Request")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 501:
            print("Not Implemented")
        case 502:
            print("Service Temporarily Overloaded")
        case 503:
            print("Service Unavailable")

a = int(input("Your errorcode: "))
errorcode(a)
quit()
