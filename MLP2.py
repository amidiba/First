from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits=load_digits()
x=digits.data
y=digits.target

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2)

mlp=MLPClassifier(hidden_layer_sizes=(100,100), max_iter=500)
mlp.fit(x_train, y_train)
print(mlp.score(x_test, y_test))