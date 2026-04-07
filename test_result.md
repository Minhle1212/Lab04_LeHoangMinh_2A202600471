Test case 1:
You: I want to travel but i don't know where to go
TravelBuddy is thinking...
Direct response from LLM, no tool calls.

TravelBuddy: Sure! Vietnam has so many great spots. To help narrow it down, could you let me know:  
1) When and for how long you’d like to travel  
2) Your approximate budget (in VND)  
3) What you enjoy most—beaches, mountains/trekking, culture/history, food, or a bit of everything  

With that info, I can recommend destinations that fit your style and budget.
Test case 2:
You: Check for me flights from Hanoi to Da Nang

TravelBuddy is thinking...
Use tool: search_flights({'origin': 'Hanoi', 'destination': 'Da Nang'})
Direct response from LLM, no tool calls.

TravelBuddy: Here are all the available flights from Hanoi to Da Nang:

1. Vietnam Airlines | 06:00–07:20 | economy | 1.450.000 VND  
2. Vietnam Airlines | 14:00–15:20 | business | 2.800.000 VND  
3. VietJet Air     | 08:30–09:50 | economy |   890.000 VND  
4. Bamboo Airways  | 11:00–12:20 | economy | 1.200.000 VND  

Let me know if you’d like to book or need hotel options!
Test case 3:
You: I am living in Hanoi, I want to travel to Phu Quoc and stay there for 3 nights with a budget of 50 million VND

TravelBuddy is thinking...
Use tool: search_flights({'origin': 'Hanoi', 'destination': 'Phu Quoc'})
Use tool: search_hotels({'city': 'Phu Quoc', 'max_price_per_night': 2000000})
Use tool: calculate_budget({'total_budget': 50000000, 'expenses': 'Flights:2200000,Hotel:2400000,Meals&Transport:3000000,Activities:2000000'})
Direct response from LLM, no tool calls.

TravelBuddy: Here’s a quick 3-night Phú Quốc getaway from Hà Nội within your 50 million VND budget:

Flight:
- VietJet Air, 16:00–18:15, economy: 1 100 000 VND one-way (2 200 000 VND round-trip)

Hotel (3 nights):
- Lahana Resort (3★) in Dương Đông  
  • Rating: 4.0  
  • 800 000 VND/night → 2 400 000 VND total  

Estimated total cost:
- Flights: 2 200 000 VND  
- Hotel: 2 400 000 VND  
- Meals & local transport: ~3 000 000 VND  
- Activities (snorkeling, park entrance, etc.): ~2 000 000 VND  
- Estimated grand total: ~9 600 000 VND  
- Remaining budget: ~40 400 000 VND  

Additional suggestions:
- Upgrade to Sol by Meliá (4★, 1 500 000 VND/night) if you’d like more comfort; still well under budget.
- Rent a scooter (~150 000 VND/day) to explore remote beaches.
- Try local night market eats in Dương Đông for authentic flavors on a budget.

Enjoy your trip to Phú Quốc!
Test case 4:
You: I want to travel to Phu Quoc

TravelBuddy is thinking...
Direct response from LLM, no tool calls.

TravelBuddy: Sure—let’s get you set up for Phú Quốc! To find the best flights and hotels, could you please let me know:  
1. Your departure city  
2. Travel dates (arrival and departure)  
3. Your budget for flights + hotel  
4. How many nights you’d like to stay  

With those details, I can pull up options that fit your needs.
Test case 5:
You: calculate 1 + 3

TravelBuddy is thinking...
Direct response from LLM, no tool calls.

TravelBuddy: I’m TravelBuddy, your friendly Vietnam travel assistant. It looks like you’re asking for a math calculation, which isn’t in my travel expertise. How can I help you plan your trip to Vietnam today?

You: write a python code for me

TravelBuddy is thinking...
Direct response from LLM, no tool calls.

TravelBuddy: I’m sorry, but I can’t help with that. If you need assistance planning a trip—flights, hotels, or budgeting—just let me know!