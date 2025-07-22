class Classifier:

    def __init__(self, data_dict, data_frame):
        """
        Initializes with the probability dictionary and dataset.

        Args:
            data_dict (dict): The trained probability dictionary.
            data_frame (pandas.DataFrame): The dataset used for reference.
        """
        self._data_dict = data_dict
        self._data_frame = data_frame

    def check_probability(self, dict_row):
        """
        Classifies a single input row using the Naive Bayes model.

        Args:
            dict_row (dict): Dictionary with feature values for classification.

        Returns:
            str: Predicted class label.
        """
        if not dict_row:
            return "error"
        if not self._data_dict:
            return "Error!"

        class_probs = {}
        for class_name in self._data_dict:
            prob = 1
            for column, value in dict_row.items():
                try:
                    prob *= self._data_dict[class_name][column][value]["probability"]
                except KeyError:
                    prob *= 1e-6

            class_count = len(self._data_frame[self._data_frame.index == class_name])
            total_count = len(self._data_frame)
            prior = class_count / total_count
            prob *= prior
            class_probs[class_name] = prob

        best_class = max(class_probs, key=class_probs.get)
        return best_class
