
def fun():
    n=input("enter a student ID: ")
    with open(r'C:\Users\subbu.polnati\Downloads\student.txt','r+') as file:
        res=file.readlines()
        data=[]
        try:
            for i in res:
                if i[0]==n:
                    data.append(i)
                    
            print(data)
        except:
            return ("invalid")

    fun()
    
fun()              

