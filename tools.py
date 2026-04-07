
from langchain_core.tools import tool

CITY_ALIASES = {
	"ha noi": "Hà Nội",
	"hanoi": "Hà Nội",
	"da nang": "Đà Nẵng",
	"danang": "Đà Nẵng",
	"phu quoc": "Phú Quốc",
	"phuquoc": "Phú Quốc",
	"ho chi minh": "Hồ Chí Minh",
	"hochiminh": "Hồ Chí Minh",
	"hcm": "Hồ Chí Minh",
	"hcmc": "Hồ Chí Minh",
}


def normalize_city_name(city: str) -> str:
	key = city.strip().lower()
	return CITY_ALIASES.get(key, city.strip())

FLIGHTS_DB = {
	("Hà Nội", "Đà Nẵng"): [
		{"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
		{"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
		{"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
		{"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
	],
	("Hà Nội", "Phú Quốc"): [
		{"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
		{"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
		{"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
	],
	("Hà Nội", "Hồ Chí Minh"): [
		{"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
		{"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
		{"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
		{"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
	],
	("Hồ Chí Minh", "Đà Nẵng"): [
		{"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
		{"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
	],
	("Hồ Chí Minh", "Phú Quốc"): [
		{"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
		{"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
	],
}

HOTELS_DB = {
	"Đà Nẵng": [
		{"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
		{"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
		{"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
		{"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
		{"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
	],
	"Phú Quốc": [
		{"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
		{"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
		{"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
		{"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
	],
	"Hồ Chí Minh": [
		{"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
		{"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
		{"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
		{"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
	],
}

@tool
def search_flights(origin: str, destination: str) -> str:
	"""Search flights between two cities using mock data.

	Args:
		origin: Departure city.
		destination: Arrival city.

	Returns:
		A formatted list of matching flights, or a not-found message.
	"""
	origin = normalize_city_name(origin)
	destination = normalize_city_name(destination)
	key = (origin, destination)
	flights = FLIGHTS_DB.get(key)

	if flights:
		lines = [f"Flight from {origin} to {destination}:"]
		for i, flight in enumerate(flights, start=1):
			price = f"{flight['price']:,}".replace(",", ".")
			lines.append(
				f"{i}. {flight['airline']} | {flight['departure']} - {flight['arrival']} | {flight['class']} | {price}đ"
			)
		return "\n".join(lines)

	reverse_key = (destination, origin)
	reverse_flights = FLIGHTS_DB.get(reverse_key)
	if reverse_flights:
		lines = [
			f"Cannot find flight from {origin} to {destination}.",
			f"However, there are return flights from {destination} to {origin}:"
		]
		for i, flight in enumerate(reverse_flights, start=1):
			price = f"{flight['price']:,}".replace(",", ".")
			lines.append(
				f"{i}. {flight['airline']} | {flight['departure']} - {flight['arrival']} | {flight['class']} | {price}đ"
			)
		return "\n".join(lines)

	return f"Cannot find flight from {origin} to {destination}."

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
	"""Search hotels in a city and filter by maximum nightly price.

	Args:
		city: Destination city.
		max_price_per_night: Maximum acceptable price per night (VND).

	Returns:
		A formatted list of hotels sorted by rating, or a not-found message.
	"""
	city = normalize_city_name(city)
	hotels = HOTELS_DB.get(city, [])
	filtered_hotels = [
		hotel for hotel in hotels
		if hotel["price_per_night"] <= max_price_per_night
	]

	filtered_hotels.sort(key=lambda x: (-x["rating"], x["price_per_night"]))

	if not filtered_hotels:
		budget_text = f"{max_price_per_night:,}".replace(",", ".")
		return (
			f"Cannot find hotels in {city} with price per night less than or equal to {budget_text}đ. Try to increate your budget"
		)

	lines = [f"Hotels in {city} with price per night less than or equal to {max_price_per_night:,}đ:"]
	for i, hotel in enumerate(filtered_hotels, start=1):
		price_text = f"{hotel['price_per_night']:,}".replace(",", ".")
		lines.append(
			f"{i}. {hotel['name']} | {hotel['stars']} stars | {hotel['area']} | Rating: {hotel['rating']} | Price per night: {price_text}đ"
		)
	return "\n".join(lines)


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
	"""Calculate remaining budget from a total budget and expense string.

	Args:
		total_budget: Initial total budget in VND.
		expenses: Comma-separated items in name:amount format.

	Returns:
		A formatted expense summary and remaining budget, with over-budget warning when applicable.
	"""

	def format_vnd(amount: int) -> str:
		return f"{amount:,}".replace(",", ".") + "đ"

	if total_budget < 0:
		return "Total budget cannot be negative."

	expense_items: list[tuple[str, int]] = []

	if expenses and expenses.strip():
		parts = [p.strip() for p in expenses.split(",") if p.strip()]

		for part in parts:
			if ":" not in part:
				return (
					"Wrong format expenses. Each expense should be in the format"
					"'name:amount', e.g., 'flight:890000,hotel:650000'."
				)

			name, amount_str = part.split(":", 1)
			name = name.strip()
			amount_str = amount_str.strip().replace(".", "")

			if not name or not amount_str:
				return "Wrong format expenses. Each expense should have a name and an amount, e.g., 'flight:890000,hotel:650000'."

			try:
				amount = int(amount_str)
			except ValueError:
				return (
					f"Error in expense format at '{part}'. "
					"Amount must be an integer (e.g., 890000)."
				)

			if amount < 0:
				return f"Expense amount cannot be negative (found in '{part}')."

			expense_items.append((name, amount))

	total_expense = sum(amount for _, amount in expense_items)
	remaining = total_budget - total_expense

	lines = ["Expenses table:"]
	if expense_items:
		for name, amount in expense_items:
			display_name = name.replace("_", " ")
			lines.append(f"- {display_name}: {format_vnd(amount)}")
	else:
		lines.append("- (No expenses)")

	lines.append("---")
	lines.append(f"Total expenses: {format_vnd(total_expense)}")
	lines.append(f"Budget: {format_vnd(total_budget)}")
	lines.append(f"Remaining: {format_vnd(remaining)}")

	if remaining < 0:
		lines.append(f"Over budget by {format_vnd(abs(remaining))}! Please adjust your expenses.")

	return "\n".join(lines)