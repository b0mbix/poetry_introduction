import matplotlib.pyplot as plt


def square(x):
    return x ** 2


def main():
    x = [1, 2, 3, 4, 5]
    y = [square(i) for i in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', color='blue', label='Dane')
    plt.title('Przykładowy wykres', fontsize=16)
    plt.xlabel('X', fontsize=14)
    plt.ylabel('Y', fontsize=14)
    plt.legend()
    plt.savefig('example_plot.png')
    print("Wykres zapisany jako 'example_plot.png'.")


if __name__ == "__main__":
    main()
