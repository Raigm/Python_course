class Parent():
    def __init__(self, last_name, eye_color):
        print ("parent instructor code")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last name - " + self.last_name)
        print ("Eye color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print ("child instructor code")
        Parent.__init__(self,last_name,eye_color)
        self.toys = toys

raimundo = Parent("Gordejuela", "verdes")
# raimundo.show_info()
rai = Child("Gordejuela", "azul",3)
rai.show_info()


# print (rai.toys)
# print (rai.last_name)