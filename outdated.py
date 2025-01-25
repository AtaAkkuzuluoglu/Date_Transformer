def GiveDate():
    while True:
        MyDate = input("Date: ")
        if "/" in MyDate:
            MyDateSlash = MyDate.split("/")
            if int(MyDateSlash[1]) <= 9 and int(MyDateSlash[0]) <= 9:
                print(f"{MyDateSlash[2]}-0{MyDateSlash[0]}-0{MyDateSlash[1]}")
                break
            elif int(MyDateSlash[1]) <= 9 and int(MyDateSlash[0]) <= 12:
                print(f"{MyDateSlash[2]}-{MyDateSlash[0]}-0{MyDateSlash[1]}")
                break
            elif int(MyDateSlash[0]) <= 9 and int(MyDateSlash[1]) <= 31:
                print(f"{MyDateSlash[2]}-0{MyDateSlash[0]}-{MyDateSlash[1]}")
                break
            elif int(MyDateSlash[1]) <= 31 and int(MyDateSlash[0]) <= 12:
                print(f"{MyDateSlash[2]}-{MyDateSlash[0]}-{MyDateSlash[1]}")               
        elif "," in MyDate: 
            MyDict = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
            MyDateComa = MyDate.split(",")
            MyDayMonthComa = MyDateComa[0].split()
            if MyDayMonthComa[0] in MyDict and int(MyDayMonthComa[1]) <= 9 and int(MyDict[MyDayMonthComa[0]] <= 9):
                print(f"{MyDateComa[1]}-0{MyDict[MyDayMonthComa[0]]}-0{MyDayMonthComa[1]}")
                break
            elif MyDayMonthComa[0] in MyDict and int(MyDayMonthComa[1]) <= 9 and int(MyDict[MyDayMonthComa[0]]) <= 12:
                print(f"{MyDateComa[1]}-{MyDict[MyDayMonthComa[0]]}-0{MyDayMonthComa[1]}")
                break
            elif MyDayMonthComa[0] in MyDict and int(MyDict[MyDayMonthComa[0]] <= 9) and int(MyDayMonthComa[1]) <= 31:
                print(f"{MyDateComa[1]}-0{MyDict[MyDayMonthComa[0]]}-{MyDayMonthComa[1]}")
                break
            elif MyDayMonthComa[0] in MyDict and int(MyDayMonthComa[1]) <= 31:
                print(f"{MyDateComa[1]}-{MyDict[MyDayMonthComa[0]]}-{MyDayMonthComa[1]}")                

GiveDate()        
          