from datetime import datetime, timedelta
from enum import Enum
import random

class ShippingStatus(Enum):
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    IN_TRANSIT = "In Transit"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"
    DELAYED = "Delayed"

class Order:
    def __init__(self, order_id: str, customer_id: str, items: list, 
                 order_date: datetime, estimated_delivery: datetime):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.order_date = order_date
        self.estimated_delivery = estimated_delivery
        self.status = ShippingStatus.PROCESSING
        self.tracking_updates = []
        self.current_location = ""
        
    def update_status(self, new_status: ShippingStatus, location: str = None):
        self.status = new_status
        if location:
            self.current_location = location
        self.tracking_updates.append({
            'timestamp': datetime.now(),
            'status': new_status.value,
            'location': location
        })

class ShippingQuerySystem:
    def __init__(self):
        self.orders = {}
        
    def create_order(self, customer_id: str, items: list) -> str:
        order_id = f"ORD-{random.randint(10000, 99999)}"
        order_date = datetime.now()
        estimated_delivery = order_date + timedelta(days=5)
        
        order = Order(order_id, customer_id, items, order_date, estimated_delivery)
        self.orders[order_id] = order
        return order_id
    
    def get_shipping_status(self, order_id: str) -> dict:
        if order_id not in self.orders:
            return {"error": "Order not found"}
            
        order = self.orders[order_id]
        return {
            "order_id": order.order_id,
            "current_status": order.status.value,
            "order_date": order.order_date.strftime("%Y-%m-%d %H:%M"),
            "estimated_delivery": order.estimated_delivery.strftime("%Y-%m-%d %H:%M"),
            "current_location": order.current_location,
            "tracking_history": order.tracking_updates
        }
    
    def process_query(self, query: str, order_id: str) -> str:
        """Process natural language queries about shipping status"""
        if order_id not in self.orders:
            return "I'm sorry, but I couldn't find an order with that ID. Please verify your order number and try again."
            
        order = self.orders[order_id]
        query = query.lower()
        
        if "where" in query or "location" in query:
            return f"Your order is currently {order.current_location}" if order.current_location else "Location information is not available yet."
            
        elif "when" in query or "delivery" in query or "arrive" in query:
            return f"Your order is estimated to be delivered by {order.estimated_delivery.strftime('%B %d, %Y')}"
            
        elif "status" in query or "tracking" in query:
            return f"Your order is currently {order.status.value}"
            
        elif "history" in query or "updates" in query:
            updates = "\n".join([
                f"- {update['timestamp'].strftime('%Y-%m-%d %H:%M')}: {update['status']} {update['location'] if update['location'] else ''}"
                for update in order.tracking_updates
            ])
            return f"Tracking history for your order:\n{updates}"
            
        else:
            return f"Current status: {order.status.value}. Estimated delivery: {order.estimated_delivery.strftime('%B %d, %Y')}"

def run_interactive_system():
    print("Welcome to the Shipping Status Query System!")
    shipping_system = ShippingQuerySystem()
    
    while True:
        print("\n" + "="*50)
        print("1. Create a new order")
        print("2. Check order status")
        print("3. Exit")
        
        choice = input("\nPlease select an option (1-3): ")
        
        if choice == "1":
            # Create new order
            customer_id = input("Enter customer ID: ")
            print("Enter items (one per line, press Enter twice when done):")
            items = []
            while True:
                item = input()
                if item == "":
                    break
                items.append(item)
            
            order_id = shipping_system.create_order(customer_id, items)
            print(f"\nOrder created successfully! Your order ID is: {order_id}")
            
            # Simulate some shipping updates for demo purposes
            order = shipping_system.orders[order_id]
            order.update_status(ShippingStatus.PROCESSING)
            order.update_status(ShippingStatus.SHIPPED, "Warehouse A")
            order.update_status(ShippingStatus.IN_TRANSIT, "Distribution Center B")
            
        elif choice == "2":
            # Query existing order
            order_id = input("Enter your order ID: ")
            
            while True:
                print("\nWhat would you like to know about your order?")
                print("1. Current status")
                print("2. Location")
                print("3. Estimated delivery")
                print("4. Tracking history")
                print("5. Back to main menu")
                
                query_choice = input("\nSelect an option (1-5): ")
                
                if query_choice == "5":
                    break
                    
                query_map = {
                    "1": "What is the status?",
                    "2": "Where is my order?",
                    "3": "When will it arrive?",
                    "4": "Show me the tracking history"
                }
                
                if query_choice in query_map:
                    response = shipping_system.process_query(query_map[query_choice], order_id)
                    print("\nResponse:", response)
                else:
                    print("\nInvalid option. Please try again.")
                
        elif choice == "3":
            print("\nThank you for using the Shipping Status Query System. Goodbye!")
            break
            
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    run_interactive_system()