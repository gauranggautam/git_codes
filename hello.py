import matplotlib.pyplot as plt
def plot_hello_world():
    plt.figure(figsize=(6, 4))
    plt.text(0.5, 0.5, 'Hello, World!', fontsize=24, ha='center', va='center')
    plt.axis('off')  # Turn off the axis
    plt.title('Hello World Plot')
    plt.show()      

plot_hello_world()
# This code creates a simple plot with "Hello, World!" text in the center.
