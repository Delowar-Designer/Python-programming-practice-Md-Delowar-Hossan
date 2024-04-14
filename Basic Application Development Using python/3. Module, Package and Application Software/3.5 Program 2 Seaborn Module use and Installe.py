# Seaborn Module use and Installe
'''import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset('iris')

# Create a pairplot with species as hue and pastel palette
sns.pairplot(iris, hue='species', palette='pastel')

iris[0].plot(x,y, color = 'green', lw = 3)
iris[0].set_xlabel('x')
iris[0].set_ylabel('y')

iris[1].plot(x,z, color = 'blue', lw = 2, ls = '--')
iris[1].set_xlabel('x')
iris[1].set_ylabel('z')
plt.show()
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')

# Create a pairplot with species as hue and pastel palette
sns.pairplot(iris, hue='species', palette='pastel')

# Plot additional graphs separately
plt.figure(figsize=(12, 6))

# Plot for the first variable
plt.subplot(1, 2, 1)
sns.lineplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='pastel')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Plot for the second variable
plt.subplot(1, 2, 2)
sns.lineplot(data=iris, x='petal_length', y='petal_width', hue='species', palette='pastel')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.tight_layout()
plt.show()
