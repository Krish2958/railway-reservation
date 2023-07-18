# Railway Reservation Management System

This is a simple Online Railway Reservation System built using Python & MySQL. The project allows users to sign up, log in, book tickets, check ticket details, and cancel tickets for railway journeys.

## Features

- User Authentication: Users can sign up, log in, and delete their accounts.
- Ticket Booking: Users can book tickets for their train journeys, specifying their name, phone number, age, gender, starting station, destination station, and date of travel.
- Ticket Checking: Users can check the details of their booked tickets using the unique ticket number generated during booking.
- Ticket Cancelling: Users can cancel their booked tickets using the unique ticket number.
- Account Details: Users can view their account details, including name, phone number, age, gender, date of birth, and age.

## Dependencies

- MySQL: The database system used for storing user information and ticket details.
- Python: The programming language used for implementing the project logic.

## How to Run

1. Install Python and MySQL on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory:

```bash
cd railway_reservation_system
```
4. Open `railway_reservation.py` and run the file using  <kbd>F5</kbd>. Make sure to update the `DB_passwd`. By default it is set to `Your_Password`


## Future Goals

- Implementing a user-friendly frontend using React.js to replace the current console-based interface.
- Implement the backend using Django Rest Framework
- Adding real-time features such as live train status, seat availability, and train search functionality using third-party railway APIs.
- Enhancing security measures, such as password encryption and user authentication using JWT tokens.
- Implementing a dashboard for admin users to manage train schedules, seat availability, and user bookings.
- Introducing payment gateways to enable online ticket booking and payments.
- Deploying the application on cloud hosting platforms to make it accessible to users worldwide.

## Contribution

Contributions to this project are welcome! Feel free to open issues or submit pull requests to improve the project. Please ensure that your contributions align with the goals and features mentioned above.
