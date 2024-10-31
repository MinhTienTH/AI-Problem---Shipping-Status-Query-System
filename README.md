# Shipping Status Query System

A Python-based interactive system for managing and tracking shipping orders. This system allows users to create orders, track their shipping status, and query order information using natural language processing.

## Features

- Create new shipping orders with customer ID and multiple items
- Track shipping status through various stages (Processing, Shipped, In Transit, etc.)
- Query order status using natural language
- View detailed tracking history with timestamps and locations
- Interactive command-line interface

## Installation

1. Clone this repository to your local machine
2. Ensure you have Python 3.6+ installed
3. No additional dependencies are required as the system uses only Python standard library

## Usage

To run the system:

```bash
python shipping_system.py
```

### Main Menu Options

1. **Create a new order**
   - Enter customer ID
   - Add multiple items (press Enter twice when finished)
   - System generates a unique order ID

2. **Check order status**
   - Enter order ID
   - Choose from various query options:
     - Current status
     - Location
     - Estimated delivery
     - Tracking history

3. **Exit**
   - Exit the application

### Order Status Types

The system supports the following shipping statuses:
- Processing
- Shipped
- In Transit
- Out for Delivery
- Delivered
- Delayed

### Query Examples

The system can process various natural language queries such as:
- "Where is my order?"
- "When will it arrive?"
- "What is the current status?"
- "Show me the tracking history"

## Code Structure

- `ShippingStatus`: Enum class defining possible shipping statuses
- `Order`: Class representing an order with tracking information
- `ShippingQuerySystem`: Main class handling order management and queries
- `run_interactive_system()`: Function implementing the interactive CLI

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for any bugs found or feature requests.

## License

This project is open source and available under the MIT License.

## Support

For any questions or issues, please open a GitHub issue in the repository.