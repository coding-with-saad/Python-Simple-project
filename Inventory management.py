class Product:
    """Class representing a product in the inventory."""
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return (f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, "
                f"Price: ${self.price:.2f}, Stock: {self.stock_quantity}")


class Inventory:
    """Class to manage inventory."""
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added successfully!")

    def edit_product(self, product_id):
        if product_id not in self.products:
            print("Product ID not found.")
            return
        product = self.products[product_id]
        print("Leave blank to skip updating a field.")
        name = input(f"Enter new name (current: {product.name}): ")
        category = input(f"Enter new category (current: {product.category}): ")
        try:
            price = input(f"Enter new price (current: {product.price}): ")
            stock = input(f"Enter new stock quantity (current: {product.stock_quantity}): ")
            if name: product.name = name
            if category: product.category = category
            if price: product.price = float(price)
            if stock: product.stock_quantity = int(stock)
            print("Product updated successfully!")
        except ValueError:
            print("Invalid input. No changes made.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully!")
        else:
            print("Product ID not found.")

    def view_products(self):
        if not self.products:
            print("No products in the inventory.")
        else:
            for product in self.products.values():
                print(product)

    def search_product(self, keyword):
        results = [p for p in self.products.values() if keyword.lower() in p.name.lower() or keyword.lower() in p.category.lower()]
        if results:
            for product in results:
                print(product)
        else:
            print("No matching products found.")

    def restock_prompt(self, threshold=5):
        low_stock = [p for p in self.products.values() if p.stock_quantity <= threshold]
        if low_stock:
            print("Products low on stock:")
            for product in low_stock:
                print(product)
        else:
            print("No products below the threshold.")

    def adjust_stock(self, product_id, amount):
        if product_id in self.products:
            self.products[product_id].stock_quantity += amount
            print(f"Stock adjusted. New quantity: {self.products[product_id].stock_quantity}")
        else:
            print("Product ID not found.")


class IMS:
    """Main Inventory Management System."""
    def __init__(self):
        self.inventory = Inventory()
        self.users = {"admin": "admin123", "user": "user123"}  # Default credentials
        self.current_user = None

    def login(self):
        print("\n=== Login ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password.")

    def logout(self):
        print(f"Goodbye, {self.current_user}!")
        self.current_user = None

    def run(self):
        while True:
            if not self.current_user:
                self.login()
                continue

            print("\n--- Menu ---")
            print("1. View Products")
            if self.current_user == "admin":
                print("2. Add Product")
                print("3. Edit Product")
                print("4. Delete Product")
                print("5. Adjust Stock")
                print("6. Restock Prompt")
            print("7. Search Product")
            print("8. Logout")
            print("9. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.inventory.view_products()
            elif choice == "2" and self.current_user == "admin":
                try:
                    pid = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    category = input("Enter Product Category: ")
                    price = float(input("Enter Product Price: "))
                    stock = int(input("Enter Stock Quantity: "))
                    self.inventory.add_product(Product(pid, name, category, price, stock))
                except ValueError:
                    print("Invalid input. Please try again.")
            elif choice == "3" and self.current_user == "admin":
                pid = input("Enter Product ID to edit: ")
                self.inventory.edit_product(pid)
            elif choice == "4" and self.current_user == "admin":
                pid = input("Enter Product ID to delete: ")
                self.inventory.delete_product(pid)
            elif choice == "5" and self.current_user == "admin":
                try:
                    pid = input("Enter Product ID: ")
                    amount = int(input("Enter stock adjustment amount (+/-): "))
                    self.inventory.adjust_stock(pid, amount)
                except ValueError:
                    print("Invalid input.")
            elif choice == "6" and self.current_user == "admin":
                threshold = input("Enter threshold (default is 5): ")
                self.inventory.restock_prompt(int(threshold) if threshold else 5)
            elif choice == "7":
                keyword = input("Enter keyword to search: ")
                self.inventory.search_product(keyword)
            elif choice == "8":
                self.logout()
            elif choice == "9":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    ims = IMS()
    ims.run()
