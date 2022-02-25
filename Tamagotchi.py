class Tamagotchi():
    def __init__(self, name):
        self.name = name
        self.init_stats()
        print("""Please take good care of your new loving pet. \nTry to get them to full size, but please be aware,the bigger they are, the hungrier they will get!
A good walk is a cure for boredom and a big boy meal will fill the stomach of even the biggest pets \n(make sure they're hungry enough for it though!)""")
        pass

    def init_stats(self):
        self.hunger = 0
        self.boredom = 0
        self.size = 0
        self.bathroom = 0

    def show_stats(self):
        print("name: %s" % (self.name))
        print("hunger: %s" % (self.hunger))
        print("boredom: %s" % (self.boredom))
        print("size: %s" % (self.size))
        print("bathroom: %s" % (self.bathroom))

    def survival_check(self):
        if self.boredom > 10:
            print("%s said 'Sod this' and ran away!" % (self.name))
            return
        if self.hunger > 10:
            print("%s ran away to find food elsewhere!" % (self.name))
            return
        if self.bathroom == 4:
            print("%s will need the toilet soon!" % (self.name))
        if self.bathroom == 5:
            print("%s had a little bathroom accident then ran away" % (self.name))
            return
        if self.size >= 10 and self.hunger >= 9:
            print("%s got hungry and ate you" % (self.name))
            return
        if self.hunger < 0:
            return
        self.care()

    def time_passes(self):
        self.hunger += (1 + self.size / 10)
        self.hunger = round(self.hunger, 2)
        if self.hunger <= 5:
            self.size += 1
        self.boredom += 1
        if self.size >= 15:
            print("%s has grown to maturity, and as all pets do, has consumed it's carer and made a bid for freedom" % (
                self.name))
            print("Thanks for playing!")
            return
        self.survival_check()

    def feed(self):
        print("fed")
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        self.bathroom += 1

    def feed_big_boy_meal(self):
        print("fed lots")
        self.hunger -= 6
        self.bathroom += 3
        if self.hunger < 0:
            print(
                "%s had eyes bigger than its belly, and after throwing up all over you, was so embarrassed it ran away!" % (
                    self.name))
            return

    def walk(self):
        print("walked")
        self.boredom -= 3
        if self.boredom < 0:
            self.boredom == 0
        self.hunger += .5

    def toilet(self):
        self.bathroom = 0

    def care(self):
        self.show_stats()
        # the users input is stored in self.option
        self.care_options = ["walk", "feed", "toilet", "bbm"]

        self.keys = [key for key in self.care_options]
        print(
            "Please enter one of the following options : %s bbm = Big boy meal, make sure your pet is hungry enough!" % (
                self.keys))
        self.option = input("How would you like to care for %s " % (self.name))
        while True:
            if self.option.lower() in self.care_options:
                break
            else:
                print("Not a valid care option, please re-enter")
                self.option = input("How would you like to care for %s " % (self.name))
        if self.option.lower() == "walk":
            self.walk()
        if self.option.lower() == "toilet":
            self.toilet()
        if self.option.lower() == "feed":
            self.feed()
        if self.option.lower() == "bbm":
            self.feed_big_boy_meal()
        self.time_passes()


Numpi = Tamagotchi("Numpi")  # Numpi the nobel gerbil
Numpi.time_passes()
