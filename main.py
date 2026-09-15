from pyscript import display, document

name = "Julia" #string
age = 15 #int
height5ft = "152.4 cm" #string
dream_countries = ['Italy', 'Japan', 'and France.']  #list
student_type = False #boolean
others = {'favorite_color':'pink', 'car_brand':'ford','shoe_size':'7','best_friend':'Jacque'} #dictionary
fruitsiluv = set(['Watermelon', 'Melon','Honeydew']) #set
sevendaysaweek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #tuple


a = f"Hello, my name is {name}. I am {age} years old."
h = f"Spiritually, I am 213.36 cm tall, but physically, I am {height5ft} tall."
d1 = f"I dream of visiting {", ".join(dream_countries)}"
st = f"People ask if I am a new student, and the answer is no. That is extremely {student_type}."
oth = f"My favorite color is {others['favorite_color']}, my car brand is {others['car_brand']}, my shoe size is {others['shoe_size']}, and my best friend is {others['best_friend']}."
dayz = f"I'm available every {", ".join(sevendaysaweek)}."

display(a,target='div1')
display(h,target='div2')
display(d1,target='div3')
display(st,target='div4')
display(oth,target='div5')
display(dayz,target='div6')



def add(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 + n2 #adds first number and second number and displays in result div

def subtract(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 - n2 #sub first number and second number and displays in result div

def multiply(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 * n2 #multiplies first number and second number and displays in result div

def divide(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 / n2 #divides first number and second number and displays in result div

# references: 
# Background garis | Hiasan kelas, Inspirasi desain website, Walpaper. (n.d.). Pinterest. https://ph.pinterest.com/pin/1145884699012575953/

