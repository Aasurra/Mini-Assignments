#Student Name: Michael Lin
#Student ID: 101484021

import threading
import time
import random

class TicketBooking:
    pass
    def __init__(self, total_seats):
        self.available_seats = total_seats
        self.lock = threading.Lock()

    def book_seat(self, counter_id):
        with self.lock:
            if self.available_seats > 0:
                time.sleep(random.uniform(0.1, 0.5))
                seat_number = self.available_seats
                self.available_seats -= 1
                print(f'Counter {counter_id} booked seat {seat_number}')
            else:
                print(f"No seats available for the Counter {counter_id}")

def create_and_start_thread(ticket_booking, num_counters):
    threads = []
    for i in range(1, num_counters + 1):
        thread = threading.Thread(target=ticket_booking.book_seat, args=(i,))
        threads.append(thread)
        thread.start()
    return threads

def main():
    total_seats = 100
    num_counters = 110
    ticket_booking = TicketBooking(total_seats)

    threads = create_and_start_thread(ticket_booking, num_counters)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
