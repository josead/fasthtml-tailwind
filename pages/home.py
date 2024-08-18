from fasthtml.common import P, Div
from components import (
    PlusIcon,
    RotateCCW,
    TWButton,
    TWCard,
    TWContainer,
    TWHtml,
    TWContent,
)


class CounterState:
    def __init__(self):
        self.count = 0

    def increment(self):
        print("incrementing")
        self.count += 1
        return self.count

    def reset(self):
        print("resetting")
        self.count = 0
        return self.count


counter_state = CounterState()


def HomePage(app, _):

    # Registers the routes
    app.post("/increment")(counter_state.increment)
    app.post("/reset")(counter_state.reset)

    return TWHtml(
        Div(
            TWContainer(
                TWContent(
                    Div(
                        TWCard(
                            P(f"{counter_state.count}", id="count"),
                            header=P("Counter App", cls="text-lg font-semibold"),
                            footer=Div(
                                P(
                                    "Click the + button to increment the counter, and the ⟲ button to reset it.",
                                    cls="w-40",
                                ),
                                Div(
                                    TWButton(
                                        PlusIcon(cls="bg-white w-5 h-5"),
                                        hx_post="/increment",
                                        hx_target="#count",
                                        hx_swap="textContent",
                                    ),
                                    TWButton(
                                        RotateCCW(cls="bg-white w-5 h-5"),
                                        hx_post="/reset",
                                        hx_target="#count",
                                        hx_swap="textContent",
                                    ),
                                ),
                                cls="flex justify-between",
                            ),
                        ),
                        cls="h-screen flex justify-center items-center",
                    )
                ),
            ),
            cls="bg-black/50",
        )
    )
