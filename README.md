# TanX.fi Application Task

This application processes customer orders data and provides various insights such as total revenue per month, revenue per product, and more. The project uses Docker and Docker Compose to manage the application and testing environments.

## Project Structure

```
.
├── .dockerignore
├── .gitignore
├── app.py
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.test
├── LICENSE
├── orders.csv
├── README.md
├── requirements.txt
└── test.py
```

## Files

-   **app.py**: Contains the main code for processing and analyzing the customer orders data.
-   **docker-compose.yml**: Configuration file for Docker Compose to build and run the application and test environments.
-   **Dockerfile**: Dockerfile for building the application image.
-   **Dockerfile.test**: Dockerfile for building the test image.
-   **orders.csv**: Sample CSV file containing customer orders data.
-   **requirements.txt**: Lists the dependencies for the project.
-   **test.py**: Contains the test cases for the application using pytest.

## Requirements

-   Docker
-   Docker Compose

## Setup

### Using Docker Compose

1. **Clone the repository**:

```bash
git clone https://github.com/IJPenguin/TanX.fi-task.git
cd TanX.fi-task
```

2. **Build and run the containers**:

```bash
docker-compose up --build
```

3. **Run the tests**:

```bash
docker-compose run test
```

### Using Standalone Docker Commands

1. **Clone the repository**:

```bash
git clone https://github.com/IJPenguin/TanX.fi-task.git
cd TanX.fi-task
```

2. **Build the application image**:

```bash
docker build -t tanx-fi-app .
```

3. **Run the application container**:

```bash
docker run -d -p 4000:80 tanx-fi-app
```

4. **Build the test image**:

```bash
docker build -t tanx-fi-test -f Dockerfile.test .
```

5. **Run the test container**:

```bash
docker run tanx-fi-test
```

## Functions

### `compute_total_revenue_per_month`

This function calculates the total revenue per month.

### `compute_total_revenue_per_product`

This function calculates the total revenue per product.

### `compute_total_revenue_per_customer`

This function calculates the total revenue per customer.

### `top_10_customers_by_revenue`

This function returns the top 10 customers by revenue.

## Usage

### Using Docker Compose

To run the application:

```bash
docker-compose up
```

To run the tests:

```bash
docker-compose run test
```

### Using Standalone Docker Commands

To run the application:

```bash
docker run -d -p 4000:80 tanx-fi-app
```

To run the tests:

```bash
docker run tanx-fi-test
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
