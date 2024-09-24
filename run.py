import random


class State:
    def insert_quarter(self):
        raise NotImplementedError()

    def eject_quarter(self):
        raise NotImplementedError()

    def turn_crank(self):
        raise NotImplementedError()

    def dispense(self):
        raise NotImplementedError()


class BaseState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Invalid action for the current state")

    def eject_quarter(self):
        print("Invalid action for the current state")

    def turn_crank(self):
        print("Invalid action for the current state")

    def dispense(self):
        print("Invalid action for the current state")


class GumballMachine:
    def __init__(self, number_gumballs):
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)

        self.state = (
            self.sold_out_state if number_gumballs == 0 else self.no_quarter_state
        )
        self.count = number_gumballs

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        if self.count > 0:
            print("A gumball comes rolling out the slot...")
            self.count -= 1

    def get_count(self):
        return self.count

    def has_gumballs(self):
        return self.count > 0

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_winner_state(self):
        return self.winner_state


class SoldOutState(BaseState):
    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there are no gumballs")


class SoldState(BaseState):
    def insert_quarter(self):
        print("Please wait, we’re already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn’t get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.has_gumballs():
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())


class NoQuarterState(BaseState):
    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def turn_crank(self):
        print("You turned, but there’s no quarter")


class HasQuarterState(BaseState):
    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned...")
        winner = random.randint(0, 9)
        if winner == 0 and self.gumball_machine.get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())


class WinnerState(BaseState):
    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.has_gumballs():
            self.gumball_machine.release_ball()
            print("YOU’RE A WINNER! You got two gumballs for your quarter")
            if self.gumball_machine.has_gumballs():
                self.gumball_machine.set_state(
                    self.gumball_machine.get_no_quarter_state()
                )
            else:
                print("Oops, out of gumballs!")
                self.gumball_machine.set_state(
                    self.gumball_machine.get_sold_out_state()
                )
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())


if __name__ == "__main__":
    gumball_machine = GumballMachine(5)

    print("\nInitial State:")
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print("\nAfter one gumball is dispensed:")
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(f"\nRemaining gumballs: {gumball_machine.get_count()}")
