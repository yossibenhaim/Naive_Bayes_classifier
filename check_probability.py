class CheckProbability:

    def __init__(self,data_dict, all_data):
        self.data_dict = data_dict
        self.all_data = all_data

    def check(self):
        a = self.create_dict()
        if not a:
            return "error"
        b = []
        for k, v in a.items():
            for x in self.data_dict:
                if x == "Yes":
                    continue
                b.append(self.data_dict[x][k][v]["probability"])

        c = []
        for k, v in a.items():
            for x in self.data_dict:
                if x == "No":
                    continue
                c.append(self.data_dict[x][k][v]["probability"])

        result_No = 1
        for x in b:
            result_No *= x
        result_No *= (len(self.all_data[(self.all_data.index == "no")]) / len(self.all_data))
        result_Yes = 1
        for x in c:
            result_Yes *= x
        result_Yes *= (len(self.all_data[(self.all_data.index == "yes")]) / len(self.all_data))
        if result_No > result_Yes:
            print(f"the probability is No = {result_No}")
        else:
            print(f"the probability is Yes = {result_Yes}")

    def create_dict(self):
        my_dict = {}
        while True:
            choice = input("menu")
            if choice == "2":
                return my_dict
            if choice == "1":
                column = input("send name column\n")
                my_dict[column] = input("send name type\n")