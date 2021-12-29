import requests

if __name__ == '__main__':
    
    sepal_length = float(input('Sepal length in cm: '))
    sepal_width = float(input('Sepal width in cm: '))
    petal_length = float(input('Petal length in cm: '))
    petal_width = float(input('Petal width in cm: '))

    headers = {'content-type' : 'application/json'}
    
    data = {
            'sepal_length': sepal_length,
            'sepal_width':  sepal_width,
            'petal_length': petal_length,
            'petal_width':  petal_width
            }
    
    
    resp = requests.post('http://127.0.0.1:5000/', headers = headers, json = data)
    
    if resp.status_code == 200:
        print(f'This plant is a {resp.json()["class"]}')
    else:
        # This means something went wrong.
        print('Error')
    
    