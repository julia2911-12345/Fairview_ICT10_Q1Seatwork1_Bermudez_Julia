from pyscript import display

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
oth = f"My favorite color is {(others.favorite_color)}, my car brand is {(others.car_brand)}, my shoe size is {(others.shoe_size)}, and my best friend is {(others.best_friend)}."
dayz = f"The days of the week are: {", ".join(sevendaysaweek)}."

display(a,target='div1')
display(h,target='div2')
display(d1,target='div3')
display(st,target='div4')
display(oth,target='div5')
display(dayz,target='div6')

# display((a),target='div1')
# display(i),target='div2')
# display(str(height5ft),target='div3')
# display(list(dream_countries),target='div4')
# display(bool(student_type),target='div5')
# display(dict(others),target='div6')
# display(set(fruitsiluv),target='div7')
# display(tuple(sevendaysaweek),target='div8')


