import matplotlib.pyplot as plt


__all__ = ('plot', )


def plot(data, labels):
    """
    Function for represent data and each groups
    :param data: np.ndarray
    :param labels: list
    """
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(
        data[0, :], data[1, :], marker='o',
        cmap=plt.get_cmap('Spectral')
    )

    for label, x, y in zip(labels, data[0, :], data[1, :]):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    plt.show()
