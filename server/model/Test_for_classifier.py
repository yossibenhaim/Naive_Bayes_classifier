import logging

main_server_logger = logging.getLogger("main_server_logger")


class Test_classifier:

    def __init__(self, data_dict, data_frame):
        """
        Initializes the classifier tester with the trained probability dictionary and dataset.

        Args:
            data_dict (dict): Trained probability dictionary mapping class and feature probabilities.
            data_frame (pandas.DataFrame): Dataset to use as reference for testing.
        """
        self._data_dict = data_dict
        self._data_frame = data_frame
        main_server_logger.info("Test_classifier instance created.")

    def check_probability(self, dict_row):
        """
        Classifies a single input row using the Naive Bayes model.

        Args:
            dict_row (dict): Feature values for classification.

        Returns:
            str: Predicted class label or "error" if input invalid.
        """
        if not dict_row:
            main_server_logger.error("Empty input row provided to check_probability.")
            return "error"
        if not self._data_dict:
            main_server_logger.error("Probability dictionary is empty in check_probability.")
            return "error"

        class_probs = {}
        try:
            for class_name in self._data_dict:
                prob = 1
                for column, value in dict_row.items():
                    try:
                        prob *= self._data_dict[class_name][column][value]["probability"]
                    except KeyError:
                        prob *= 1e-6  # Small smoothing probability
                class_count = len(self._data_frame[self._data_frame.index == class_name])
                total_count = len(self._data_frame)
                prior = class_count / total_count
                prob *= prior
                class_probs[class_name] = prob
            best_class = max(class_probs, key=class_probs.get)
            main_server_logger.debug(f"Class probabilities: {class_probs}, predicted: {best_class}")
            return best_class
        except Exception as e:
            main_server_logger.error(f"Exception during classification: {e}")
            return "error"

    def test(self, data_frame):
        """
        Tests classification accuracy on the provided dataset.

        Args:
            data_frame (pandas.DataFrame): Dataset to test against.

        Returns:
            str: Accuracy as a formatted percentage string.
        """
        if data_frame is None or data_frame.empty:
            main_server_logger.error("Empty or None data_frame passed to test method.")
            return "Accuracy: 0.00%"

        correct_count = 0
        total = len(data_frame)
        try:
            for idx, row in data_frame.iterrows():
                result = self.check_probability(row.to_dict())
                if result == idx:
                    correct_count += 1
            accuracy = correct_count / total
            main_server_logger.info(f"Test accuracy calculated: {accuracy * 100:.2f}%")
            return f"Accuracy: {accuracy * 100:.2f}%"
        except Exception as e:
            main_server_logger.error(f"Exception during testing: {e}")
            return "Accuracy: 0.00%"
