

#hello 123 world 중에서 123만 표시되게
def ex3():
    s1 = 'hello 123 world'
    num = s1[6:9]
    print(num)

    r = len(s1)
    print(r)

def ex4():
    s1 = ' hello world   \n'
    r1 = len(s1)
    r2 = len(s1.strip())
    print(r1)
    print(r2)

def ex5():
    rec="홍길동,100,95,88"
    item=rec.split(",")
    print(item)

 
def ex6():
    name = "홍길동"
    age = 32
    s = f"{name}의 나이는 {age}세 입니다"
    print(s)
       
    


class Stock:
    종목코드 = None
    회사명 = None
    현재가 = None
    거래량 = None
    예측 = None

    def evaluate(self):
        ret = f"종목코드: {self.종목코드}, 회사명: {self.회사명}, 현재가: {self.현재가}, 거래량: {self.거래량}, 예측: {self.예측}"
        print(ret)


def ex6():
    a = 5
    b = 'hello'
    c = Stock()
    c.종목코드 ='005930'
    c.회사명 = '삼성전자'
    c.현재가 = 70000
    c.거래량 = 10000000
    c.예측 = 1
    d = Stock()
    d.종목코드 ='000660'
    d.회사명 = 'SK하이닉스'
    d.현재가 = 130000
    d.거래량 = 5000000
    d.예측 = 0
    
    c.evaluate()
    d.evaluate()


def getStocks():
    f = open("stock.csv",'rt', encoding='utf-8')

    stocks = []

    for i, stock in enumerate(f.readlines()):
        if i == 0:
            continue

        r1 = stock.strip()
        r2 = r1.split(',')

        s = Stock()
        s.종목코드 = r2[0]
        s.회사명 = r2[1]
        s.현재가 = int(r2[2])
        s.거래량 = int(r2[3])
        s.예측 = int(r2[4])

        s.evaluate()
        stocks.append(s)


    return stocks

if __name__ == "__main__":
    r = getStocks()
    print(r)


python app.py