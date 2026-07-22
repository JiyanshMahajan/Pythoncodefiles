class Robot:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"Hello! I am {self.name}.Nice to meet you!")
    def main():
        print("Harsh bought 2 new robots!Lets make them introduce themselves.\n" )
        robot1=Robot("Tom")
        robot2=Robot("Jerry")
        robot1.introduce()
        robot2.introduce()
if __name__=="__main__":
    main()
