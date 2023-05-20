people = []
numbers=[]
def hello_people():
    for person in people:
        print(f"Привет, {person}.")

def calculation(sum=0):
    for num in numbers:
        sum=num+sum
    print(sum)


people.append("Крош")
people.append("Ёжик")
hello_people()

numbers.append(4)
numbers.append(2)
calculation()