import requests
from requests import Response

def get_response(url : str) -> Response :
    return requests.get(url)

def show_response_info(response : Response) -> None :
    print("status",response.status_code)
    print("ok",response.ok)
    print("link",response.links)
    print("Encoding :",response.encoding)
    print("Is Redirect :",response.is_redirect)
    print("Is Permanent Redirect :",response.is_permanent_redirect)

def main() -> None :
    website: str  = 'https://www.google.com'
    response : Response = get_response(website)
    show_response_info(response)



if __name__ == '__main__':
    main()