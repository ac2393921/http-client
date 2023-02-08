import src.http_client as http_client


def main():
    url = 'https://www.google.co.jp/search'
    client: http_client.HttpClient = http_client.DefaultHttpClient()
    response = client.get(url, params={'q': 'python'})
    print(response.text)


if __name__ == "__main__":
    main()
