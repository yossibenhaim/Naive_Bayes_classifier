import logging

classifier_logger = logging.getLogger("classifier_logger")
classifier_logger.setLevel(logging.INFO)
fh = logging.FileHandler("logs/classifier_server.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
classifier_logger.addHandler(fh)

classifier_logger.info("Classifier server started.")


class Classifier:

    def __init__(self, data_dict, data_frame):
        """
        Initialize with the probability dictionary and dataset.

        Args:
            data_dict (dict): The trained probability dictionary.
            data_frame (pandas.DataFrame): The dataset used for reference.
        """
        self._data_dict = data_dict
        self._data_frame = data_frame
        classifier_logger.info("Classifier initialized with data dictionary and data frame.")

    def check_probability(self, dict_row):
        """
        Classify a single input row using the Naive Bayes model.

        Args:
            dict_row (dict): Dictionary with feature values for classification.

        Returns:
            dict: A dictionary of class probabilities or 'error' string on failure.
        """
        if not dict_row:
            classifier_logger.error("Empty input row received for classification.")
            return "error"

        if not self._data_dict:
            classifier_logger.error("Probability dictionary is empty or not initialized.")
            return "error"

        class_probs = {}
        total_count = len(self._data_frame)
        classifier_logger.info(f"Starting probability calculation for input: {dict_row}")

        try:
            for class_name in self._data_dict.keys():
                prob = 1.0
                for column, value in dict_row.items():
                    try:
                        prob *= self._data_dict[class_name][column][value]["probability"]
                    except KeyError:
                        classifier_logger.warning(
                            f"Unseen value '{value}' for column '{column}' in class '{class_name}', applying smoothing.")
                        prob *= 1e-6

                class_count = len(self._data_frame[self._data_frame.index == class_name])
                prior = class_count / total_count if total_count > 0 else 0
                prob *= prior
                class_probs[class_name] = prob
                classifier_logger.info(f"Probability for class '{class_name}': {prob}")

        except Exception as e:
            classifier_logger.error(f"Exception during probability calculation: {e}")
            return "error"

        classifier_logger.info(f"Completed probability calculation: {class_probs}")
        return class_probs
