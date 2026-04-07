# 🏨 Hotel Booking System

A Python-based, object-oriented console application that manages hotel reservations, processes secure credit card payments, and generates booking tickets. This project demonstrates the application of Object-Oriented Programming (OOP) principles, including inheritance, abstraction, and various method types.

## ✨ Features

* **🔍 Hotel Availability Checking:** Queries a dataset to verify real-time room availability based on hotel ID.
* **⚡ Automated Booking Process:** Updates hotel availability and automatically overwrites the local database to lock in reservations.
* **🛡️ Secure Payment Validation:** * Validates standard credit card details (Number, Expiration, CVC, Cardholder Name).
    * Implements a secondary security layer (`SecurityCreditCard`) requiring password authentication.
* **🎟️ Dynamic Ticket Generation:** Generates customized string representations of Reservation Tickets and optional Spa Tickets.
* **🗄️ Data Management:** Utilizes `pandas` to read and manipulate external CSV files acting as the system's database.

## 🛠️ Prerequisites

Before running this project, ensure you have the following installed:
* Python 3.7+
* Pandas library

You can install the required dependency via pip:
```bash
pip install pandas
```
## 📂 Project Structure
​The system relies on external CSV files to simulate a database environment. Ensure the following files are present in the root directory:  

​📄 main.py / advance_methods.py: The core application logic and execution scripts.  

​🏨 hotels.csv: Contains hotel data (id, name, available).  

​💳 cards.csv: Contains standard credit card data (number, expiration, cvc, holder).  

​🔐 card_security.csv: Contains authentication data (number, password).  

## 🚀 Usage   

​1.Clone the repository to your local machine.  

​2.Ensure the structural CSV files are populated with test data.  

​3.Run the primary execution script from your terminal:  

```bash
python main.py
```
​ 4.**Follow the console prompts:**

🏨 Enter the desired Hotel ID.  

​💳 If the hotel is available, the system will proceed to payment validation.  

​👤 Enter your customer name.  

​🧖‍♀️ Choose whether to add a Spa reservation.  

​✅ The system will output your final reservation tickets.
