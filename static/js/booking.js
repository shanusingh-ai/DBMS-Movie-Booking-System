document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("bookingForm");
    const input = document.getElementById("selectedSeatsInput");
    const seatText = document.getElementById("selectedSeatText");
    const seatCount = document.getElementById("seatCount");
    const totalText = document.getElementById("bookingTotal");
    const seatMap = document.querySelector(".seat-map");
    const price = Number(seatMap?.dataset.price || 0);
    const selected = new Set((input?.value || "").split(",").filter(Boolean));

    const formatCurrency = (amount) =>
        new Intl.NumberFormat("en-IN", {
            style: "currency",
            currency: "INR",
            minimumFractionDigits: 2,
        })
            .format(amount)
            .replace("₹", "Rs. ");

    const renderSummary = () => {
        const seats = Array.from(selected);
        if (input) {
            input.value = seats.join(",");
        }
        if (seatText) {
            seatText.textContent = seats.length ? seats.join(", ") : "None";
        }
        if (seatCount) {
            seatCount.textContent = String(seats.length);
        }
        if (totalText) {
            totalText.textContent = formatCurrency(seats.length * price);
        }
    };

    document.querySelectorAll(".seat-btn:not(.booked)").forEach((button) => {
        const seat = button.dataset.seat;
        if (selected.has(seat)) {
            button.classList.add("selected");
        }
        button.addEventListener("click", () => {
            if (selected.has(seat)) {
                selected.delete(seat);
                button.classList.remove("selected");
            } else {
                if (selected.size >= 8) {
                    window.alert("You can book a maximum of 8 seats at once.");
                    return;
                }
                selected.add(seat);
                button.classList.add("selected");
            }
            renderSummary();
        });
    });

    form?.addEventListener("submit", (event) => {
        if (selected.size === 0) {
            event.preventDefault();
            window.alert("Please select at least one seat.");
        }
    });

    renderSummary();
});