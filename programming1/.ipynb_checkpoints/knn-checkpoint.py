class KNearestNeighborsClassifier:
    # K: the number of training data points joining the voting
    def __init__(self, K):
        self.K = K

    # fit: train this model on training inputs X and outputs Y
    # X: training inputs -- np.ndarray
    #      (shape: [# of data points, # of features])
    # Y: training outputs -- np.ndarray
    #      (shape: [# of data points])
    def fit(self, X, Y):
        # TODO: IMPLEMENT ME
        pass

    # predict: classify given data points
    # X: inputs to the classifier -- np.ndarray
    #      (shape: [# of data points, # of features])
    def predict(self, X):
        # TODO: IMPLEMENT ME

        # Hint: Euclid distances between the training inputs X_ and
        #   prediction inputs X with shape [# of data points, # of features] are
        #   calculuated by ``numpy.sqrt( ((X_ - X) ** 2.).sum(axis=1) )``
        pass


# check this is a main file
if __name__ == '__main__':
    import numpy as np
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    iris_dataset = load_iris()
    X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset.data,
                                                        iris_dataset.target,
                                                        random_state=0)
    knn = KNearestNeighborsClassifier(3)
    knn.fit(X_train, Y_train)
    X_test_predict = knn.predict(X_test)
    accuracy = np.sum(Y_test == X_test_predict) / Y_test.shape[0]
    assert(accuracy > 0.7)
    print('acc:', accuracy)
