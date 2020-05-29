def inputData():
    while True:
        try :   
            print("(숫자 연산자 숫자)형식으로 입력해주세요.(띄어씌기 주의!!)")            
            arr = input()
            if arr=="c":
                print("다시 입력해주세요.")
            elif arr == "e":
                return "e","e","e"  # e 반환시 종료        
            else :
                arr_list = arr.split()
                a,op,b = arr_list
                a=int(a)
                b=int(b)
                return a,op,b

        except :
            print("다시 입력해주세요.")


def calculate(a,op,b):
    ok = True
    if(op=="+"):
        res = a+b
    elif(op=="-"):
        res = a-b
    elif(op=="*"):
        res = a*b
    elif(op=="/"):
        res = a/b
    return res,ok

def start():
    while True:
        a,op,b = inputData()
        if a=="e":
            break
        res,ok = calculate(a,op,b)
        if ok:
            f = open("result.txt",'a')
            result = "%d \n" %res
            f.write(result)

    print("종료되었습니다.")

print("사칙연산 시작")
start()
