

class Test_classifier:
    def __init__(self, model ):
        self._model = model

    def check_probability(self, dict_row):
        if not dict_row:
            return "error"
        if not self._model._data_dict:
            return "Error!"
        class_probs = {}
        for class_name in self._model._data_dict:
            prob = 1
            for column, value in dict_row.items():
                try:
                    prob *= self._model._data_dict[class_name][column][value]["probability"]
                except KeyError:
                    prob *= 1e-6

            class_count = len(self._model._data_frame[self._model._data_frame.index == class_name])
            total_count = len(self._model._data_frame)
            prior = class_count / total_count
            prob *= prior
            class_probs[class_name] = prob
        for class_name, prob_value in class_probs.items():
            print(f"Class '{class_name}' probability: {prob_value}")
        best_class = max(class_probs, key=class_probs.get)
        return best_class

    def test(self, data_frame):
        count = 0
        for idx, row in data_frame.iterrows():
            result = self.check_probability(row.to_dict())
            if result == idx:
                count += 1
        accuracy = count / len(data_frame)
        print(f"Accuracy: {accuracy * 100:.2f}%")
        return accuracy




