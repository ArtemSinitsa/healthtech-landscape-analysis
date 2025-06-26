from src.data_generation import generate_data
from src.visualization import plot_visualization

if __name__ == "__main__":
    df = generate_data()
    plot_visualization(df)
