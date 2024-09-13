import csv

def generate_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        csv_writer.writerow(['Name', 'Age', 'Email'])

        # Write data rows
        for row in data:
            csv_writer.writerow(row)

if __name__ == "__main__":
    # Sample data
    data = [
        ['John Doe', 30, 'john.doe@example.com'],
        ['Jane Smith', 25, 'jane.smith@example.com'],
        ['Michael Johnson', 28, 'michael.johnson@example.com']
    ]
    x = ['Michael Johnson', 28, 'michael.johnson@example.com']
    for i in range(60):
        data.append(x)

    # File path for the CSV
    file_path = 'sample_data_big.csv'

    # Generate the CSV file
    generate_csv(file_path, data)

    print(f"CSV file '{file_path}' has been generated successfully!")