import os
from utils import load_data
from regularization import regularize_paths
from symmetry import find_symmetries
from completion import complete_curves
from convert import polylines2svg

def main(input_file, output_file):
    input_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples', input_file)
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples', output_file)

    data = load_data(input_path)
    print(f"Loaded data shape: {data.shape}")

    regularized_data = regularize_paths(data)
    symmetries = find_symmetries(regularized_data)
    completed_curves = complete_curves(regularized_data, symmetries)

    polylines2svg(completed_curves, output_path)

if __name__ == "__main__":
    input_file = 'isolated.csv'
    output_file = 'output.svg'
    main(input_file, output_file)
