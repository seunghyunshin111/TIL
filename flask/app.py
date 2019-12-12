# Flask + Python
# html

from flask import Flask
from flask import request
from flask import render_template
import random
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mulcam')
def mulcam():
    return 'This is mulcam!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Hello, {name}!'

@app.route('/cube/<int:num>')
def cube(num1):
    result = num**3
    return str(result)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '간짜장', '삼선짜장']
    order = random.sample(menu, people)
    return str(order)

@app.route('/html')
def html():
    return '<h1>안녕하세요!!</h1>'

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html',your_name = name)

@app.route('/naver')
def naver():
    return render_template('naver.html')




# 클릭하면 원하는 곳으로 가기

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('pong.html', name = name, message = message)




# 입력한 문자열이 아스키 코드로 나오게 만들기

@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/ascii_result')
def ascii_result():
    # 1. form 태그로 날린 데이터(word)를 받는다.
    word = request.args.get('keyword')
    # 2. word를 가지고 ascii_art API 요청 주소로 요청을 보낸다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}').text
    # 3. API 응답 결과를 html 파일에 담아서 보여준다.
    return render_template('ascii_result.html', result = result)




# 로또 번호 당첨 여부 확인

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():


    lotto_round = request.args.get('lotto_round')
    response = request.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()

    winner = []

    # 1. for문을 활용한다.
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])


    numbers = request.args.get('numbers') # string
    numbers = numbers.split() # list - ['1', '2', '3']
    numbers_int = []

    for number in numbers:
        numbers_int.append(int(numbers))

    matched = len(set(winner) & set(numbers_int)) # 두 리스트의 교집합 찾기(일치하는 로또 번호 찾기)

    if matched == 6:
        result = '1등입니다!!'
    elif matched == 5:
        if lotto["bonusNo"] in numbers_int:
            result = '2등입니다!!'
        else:
            result = '3등입니다!!'
    elif matched == 4:
        result = '4등입니다!'
    elif matched == 3:
        result = '5등입니다!'
    else: 
        result = '꽝입니다...'


    # 2. List Comprehension
    # winner = [lotto[f'drwtNo{i}']] for i in range(1,7)]

    # drwtNo6 = lotto["drwtNo6"] # Error가 뜸
    # drwtNo6 = lotto.get("drwtNo6") # None이 나옴, 이것을 권장


    return render_template('lotto_result.html',
    lotto_round = lotto_round, winner = winner, numbers = numbers_int,
    result = result)

if __name__ == '__main__':
    app.run(debug = True)
