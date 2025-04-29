import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models
from app.schemas import ItineraryCreate, DayCreate, ActivityCreate, TransferCreate, AccommodationCreate

def seed_data():
    db = SessionLocal()
    
    Base.metadata.create_all(bind=engine)
    
    phuket_2_nights = ItineraryCreate(
        name="Phuket Beach Getaway",
        destination="Phuket",
        duration_nights=2,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Patong Beach Resort",
                    location="Patong, Phuket"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Phuket International Airport",
                        to_location="Patong Beach Resort",
                        transfer_type="Car"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Patong Beach Relaxation",
                        description="Relax on the famous Patong Beach",
                        location="Patong Beach",
                        duration_hours=3.0
                    ),
                    ActivityCreate(
                        name="Walking Street Market",
                        description="Visit the vibrant night market",
                        location="Bangla Road",
                        duration_hours=2.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Patong Beach Resort",
                    location="Patong, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Phi Phi Islands Tour",
                        description="Full day island hopping tour",
                        location="Phi Phi Islands",
                        duration_hours=8.0
                    )
                ]
            )
        ]
    )
    
    phuket_4_nights = ItineraryCreate(
        name="Phuket Explorer",
        destination="Phuket",
        duration_nights=4,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Kata Beach Resort",
                    location="Kata Beach, Phuket"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Phuket International Airport",
                        to_location="Kata Beach Resort",
                        transfer_type="Car"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Beach Relaxation",
                        description="Relax at Kata Beach",
                        location="Kata Beach",
                        duration_hours=4.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Kata Beach Resort",
                    location="Kata Beach, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Big Buddha Visit",
                        description="Visit the iconic Big Buddha",
                        location="Chalong, Phuket",
                        duration_hours=3.0
                    ),
                    ActivityCreate(
                        name="Wat Chalong",
                        description="Visit Phuket's largest Buddhist temple",
                        location="Chalong, Phuket",
                        duration_hours=2.0
                    )
                ]
            ),
            DayCreate(
                day_number=3,
                accommodation=AccommodationCreate(
                    hotel_name="Kata Beach Resort",
                    location="Kata Beach, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Phi Phi Islands Tour",
                        description="Full day island hopping tour",
                        location="Phi Phi Islands",
                        duration_hours=8.0
                    )
                ]
            ),
            DayCreate(
                day_number=4,
                accommodation=AccommodationCreate(
                    hotel_name="Kata Beach Resort",
                    location="Kata Beach, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Phuket Old Town Tour",
                        description="Explore the charming old town",
                        location="Phuket Old Town",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Thai Cooking Class",
                        description="Learn to cook authentic Thai dishes",
                        location="Kata Beach",
                        duration_hours=3.0
                    )
                ],
                transfers=[
                    TransferCreate(
                        from_location="Kata Beach Resort",
                        to_location="Phuket International Airport",
                        transfer_type="Car"
                    )
                ]
            )
        ]
    )
    
    krabi_3_nights = ItineraryCreate(
        name="Krabi Island Adventure",
        destination="Krabi",
        duration_nights=3,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Ao Nang Cliff Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Krabi International Airport",
                        to_location="Ao Nang Cliff Beach Resort",
                        transfer_type="Car"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Ao Nang Beach",
                        description="Relax at Ao Nang Beach",
                        location="Ao Nang Beach",
                        duration_hours=3.0
                    ),
                    ActivityCreate(
                        name="Night Market",
                        description="Visit the local night market",
                        location="Ao Nang",
                        duration_hours=2.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Ao Nang Cliff Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Four Islands Tour",
                        description="Island hopping to Chicken Island, Tup Island, Poda Island, and Phra Nang Cave",
                        location="Krabi Islands",
                        duration_hours=7.0
                    )
                ]
            ),
            DayCreate(
                day_number=3,
                accommodation=AccommodationCreate(
                    hotel_name="Ao Nang Cliff Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Railay Beach Visit",
                        description="Visit the stunning Railay Beach",
                        location="Railay Beach",
                        duration_hours=5.0
                    ),
                    ActivityCreate(
                        name="Rock Climbing",
                        description="Try rock climbing at one of the world's best spots",
                        location="Railay Beach",
                        duration_hours=3.0
                    )
                ],
                transfers=[
                    TransferCreate(
                        from_location="Ao Nang Cliff Beach Resort",
                        to_location="Krabi International Airport",
                        transfer_type="Car"
                    )
                ]
            )
        ]
    )
    
    phuket_krabi_7_nights = ItineraryCreate(
        name="Phuket & Krabi Combo",
        destination="Phuket & Krabi",
        duration_nights=7,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Patong Beach Resort",
                    location="Patong, Phuket"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Phuket International Airport",
                        to_location="Patong Beach Resort",
                        transfer_type="Car"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Patong Beach Relaxation",
                        description="Relax on the famous Patong Beach",
                        location="Patong Beach",
                        duration_hours=3.0
                    ),
                    ActivityCreate(
                        name="Walking Street Market",
                        description="Visit the vibrant night market",
                        location="Bangla Road",
                        duration_hours=2.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Patong Beach Resort",
                    location="Patong, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Phuket City Tour",
                        description="Explore Phuket's key attractions",
                        location="Phuket",
                        duration_hours=6.0
                    ),
                    ActivityCreate(
                        name="Simon Cabaret Show",
                        description="Watch the famous cabaret performance",
                        location="Patong",
                        duration_hours=2.0
                    )
                ]
            ),
            DayCreate(
                day_number=3,
                accommodation=AccommodationCreate(
                    hotel_name="Patong Beach Resort",
                    location="Patong, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Phi Phi Islands Tour",
                        description="Full day island hopping tour",
                        location="Phi Phi Islands",
                        duration_hours=8.0
                    )
                ]
            ),
            DayCreate(
                day_number=4,
                accommodation=AccommodationCreate(
                    hotel_name="Patong Beach Resort",
                    location="Patong, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Phang Nga Bay Tour",
                        description="Visit James Bond Island and sea caves",
                        location="Phang Nga Bay",
                        duration_hours=8.0
                    )
                ]
            ),
            DayCreate(
                day_number=5,
                accommodation=AccommodationCreate(
                    hotel_name="Railay Princess Resort",
                    location="Railay Beach, Krabi"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Patong Beach Resort",
                        to_location="Phuket Pier",
                        transfer_type="Car"
                    ),
                    TransferCreate(
                        from_location="Phuket Pier",
                        to_location="Krabi Pier",
                        transfer_type="Ferry"
                    ),
                    TransferCreate(
                        from_location="Krabi Pier",
                        to_location="Railay Princess Resort",
                        transfer_type="Longtail Boat"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Railay Beach Exploration",
                        description="Explore the beautiful Railay Beach",
                        location="Railay Beach",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=6,
                accommodation=AccommodationCreate(
                    hotel_name="Railay Princess Resort",
                    location="Railay Beach, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Hong Islands Tour",
                        description="Visit the stunning Hong Islands",
                        location="Hong Islands",
                        duration_hours=7.0
                    )
                ]
            ),
            DayCreate(
                day_number=7,
                accommodation=AccommodationCreate(
                    hotel_name="Railay Princess Resort",
                    location="Railay Beach, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Rock Climbing",
                        description="Experience world-class rock climbing",
                        location="Railay Beach",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Phra Nang Cave Visit",
                        description="Visit the sacred Princess Cave",
                        location="Railay Beach",
                        duration_hours=2.0
                    )
                ],
                transfers=[
                    TransferCreate(
                        from_location="Railay Princess Resort",
                        to_location="Krabi Pier",
                        transfer_type="Longtail Boat"
                    ),
                    TransferCreate(
                        from_location="Krabi Pier",
                        to_location="Krabi International Airport",
                        transfer_type="Car"
                    )
                ]
            )
        ]
    )
    
    krabi_5_nights = ItineraryCreate(
        name="Krabi Complete Experience",
        destination="Krabi",
        duration_nights=5,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Centara Grand Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Krabi International Airport",
                        to_location="Ao Nang Pier",
                        transfer_type="Car"
                    ),
                    TransferCreate(
                        from_location="Ao Nang Pier",
                        to_location="Centara Grand Beach Resort",
                        transfer_type="Boat"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Resort Beach Relaxation",
                        description="Relax at the exclusive resort beach",
                        location="Centara Grand",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Centara Grand Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Four Islands Tour",
                        description="Visit Chicken, Tup, Poda Islands and Phra Nang Cave",
                        location="Krabi Islands",
                        duration_hours=7.0
                    )
                ]
            ),
            DayCreate(
                day_number=3,
                accommodation=AccommodationCreate(
                    hotel_name="Centara Grand Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Emerald Pool & Hot Springs",
                        description="Swim in the natural Emerald Pool and relax in hot springs",
                        location="Thung Teao Forest",
                        duration_hours=6.0
                    ),
                    ActivityCreate(
                        name="Tiger Cave Temple",
                        description="Visit the sacred temple with 1,237 steps to the top",
                        location="Tiger Cave Temple",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=4,
                accommodation=AccommodationCreate(
                    hotel_name="Centara Grand Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Hong Islands Adventure",
                        description="Kayaking and swimming at Hong Islands",
                        location="Hong Islands",
                        duration_hours=7.0
                    )
                ]
            ),
            DayCreate(
                day_number=5,
                accommodation=AccommodationCreate(
                    hotel_name="Centara Grand Beach Resort",
                    location="Ao Nang, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Railay Beach Day Trip",
                        description="Visit nearby Railay Beach for climbing and relaxation",
                        location="Railay Beach",
                        duration_hours=6.0
                    ),
                    ActivityCreate(
                        name="Sunset Dinner Cruise",
                        description="Enjoy dinner while cruising around the islands",
                        location="Andaman Sea",
                        duration_hours=3.0
                    )
                ],
                transfers=[
                    TransferCreate(
                        from_location="Centara Grand Beach Resort",
                        to_location="Ao Nang Pier",
                        transfer_type="Boat"
                    ),
                    TransferCreate(
                        from_location="Ao Nang Pier",
                        to_location="Krabi International Airport",
                        transfer_type="Car"
                    )
                ]
            )
        ]
    )
    
    phuket_8_nights = ItineraryCreate(
        name="Ultimate Phuket Luxury",
        destination="Phuket",
        duration_nights=8,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Banyan Tree Resort",
                    location="Laguna Area, Phuket"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Phuket International Airport",
                        to_location="Banyan Tree Resort",
                        transfer_type="Luxury Car"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Resort Relaxation",
                        description="Relax at your private pool villa",
                        location="Banyan Tree Resort",
                        duration_hours=4.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Banyan Tree Resort",
                    location="Laguna Area, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Spa Day",
                        description="Enjoy luxury spa treatments",
                        location="Banyan Tree Spa",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Sunset Yacht Cruise",
                        description="Private yacht cruise around Phang Nga Bay",
                        location="Phang Nga Bay",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=3,
                accommodation=AccommodationCreate(
                    hotel_name="Banyan Tree Resort",
                    location="Laguna Area, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Private Phi Phi Islands Tour",
                        description="Exclusive speedboat tour to Phi Phi Islands",
                        location="Phi Phi Islands",
                        duration_hours=8.0
                    )
                ]
            ),
            DayCreate(
                day_number=4,
                accommodation=AccommodationCreate(
                    hotel_name="Banyan Tree Resort",
                    location="Laguna Area, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Golf Day",
                        description="Play at one of Phuket's premium golf courses",
                        location="Laguna Golf Phuket",
                        duration_hours=5.0
                    ),
                    ActivityCreate(
                        name="Thai Cooking Class",
                        description="Private cooking class with a master chef",
                        location="Banyan Tree Resort",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=5,
                accommodation=AccommodationCreate(
                    hotel_name="Banyan Tree Resort",
                    location="Laguna Area, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Similan Islands Tour",
                        description="Day trip to the pristine Similan Islands",
                        location="Similan Islands",
                        duration_hours=10.0
                    )
                ]
            ),
            DayCreate(
                day_number=6,
                accommodation=AccommodationCreate(
                    hotel_name="The Surin Phuket",
                    location="Surin Beach, Phuket"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Banyan Tree Resort",
                        to_location="The Surin Phuket",
                        transfer_type="Luxury Car"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Surin Beach Day",
                        description="Relax at the exclusive Surin Beach",
                        location="Surin Beach",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Sunset Cocktails",
                        description="Enjoy cocktails at a beach club",
                        location="Catch Beach Club",
                        duration_hours=2.0
                    )
                ]
            ),
            DayCreate(
                day_number=7,
                accommodation=AccommodationCreate(
                    hotel_name="The Surin Phuket",
                    location="Surin Beach, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Old Town Heritage Tour",
                        description="Private guided tour of Phuket's historical old town",
                        location="Phuket Old Town",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Luxury Shopping",
                        description="Shopping at premium boutiques and markets",
                        location="Phuket",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=8,
                accommodation=AccommodationCreate(
                    hotel_name="The Surin Phuket",
                    location="Surin Beach, Phuket"
                ),
                activities=[
                    ActivityCreate(
                        name="Island Hopping",
                        description="Visit nearby islands by private speedboat",
                        location="Coral Island, Racha Island",
                        duration_hours=6.0
                    ),
                    ActivityCreate(
                        name="Farewell Dinner",
                        description="Gourmet farewell dinner on the beach",
                        location="The Surin Phuket",
                        duration_hours=2.0
                    )
                ],
                transfers=[
                    TransferCreate(
                        from_location="The Surin Phuket",
                        to_location="Phuket International Airport",
                        transfer_type="Luxury Car"
                    )
                ]
            )
        ]
    )
    
    krabi_6_nights = ItineraryCreate(
        name="Krabi Nature Explorer",
        destination="Krabi",
        duration_nights=6,
        is_recommended=True,
        days=[
            DayCreate(
                day_number=1,
                accommodation=AccommodationCreate(
                    hotel_name="Rayavadee Resort",
                    location="Railay, Krabi"
                ),
                transfers=[
                    TransferCreate(
                        from_location="Krabi International Airport",
                        to_location="Ao Nang Pier",
                        transfer_type="Car"
                    ),
                    TransferCreate(
                        from_location="Ao Nang Pier",
                        to_location="Rayavadee Resort",
                        transfer_type="Speedboat"
                    )
                ],
                activities=[
                    ActivityCreate(
                        name="Resort Exploration",
                        description="Explore the beautiful resort grounds",
                        location="Rayavadee Resort",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=2,
                accommodation=AccommodationCreate(
                    hotel_name="Rayavadee Resort",
                    location="Railay, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Railay Beach Exploration",
                        description="Walk between the stunning beaches of Railay",
                        location="Railay Beach",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Limestone Climbing",
                        description="Try beginner rock climbing on limestone cliffs",
                        location="Railay Beach",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=3,
                accommodation=AccommodationCreate(
                    hotel_name="Rayavadee Resort",
                    location="Railay, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Four Islands Tour",
                        description="Visit stunning islands by private boat",
                        location="Krabi Islands",
                        duration_hours=7.0
                    )
                ]
            ),
            DayCreate(
                day_number=4,
                accommodation=AccommodationCreate(
                    hotel_name="Rayavadee Resort",
                    location="Railay, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Phi Phi Islands Tour",
                        description="Visit Maya Bay and Phi Phi Islands",
                        location="Phi Phi Islands",
                        duration_hours=9.0
                    )
                ]
            ),
            DayCreate(
                day_number=5,
                accommodation=AccommodationCreate(
                    hotel_name="Rayavadee Resort",
                    location="Railay, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Thung Teao Forest Natural Park",
                        description="Visit the Emerald Pool and Hot Springs",
                        location="Thung Teao Forest",
                        duration_hours=6.0
                    ),
                    ActivityCreate(
                        name="Thai Cooking Class",
                        description="Learn to cook authentic Thai dishes",
                        location="Rayavadee Resort",
                        duration_hours=3.0
                    )
                ]
            ),
            DayCreate(
                day_number=6,
                accommodation=AccommodationCreate(
                    hotel_name="Rayavadee Resort",
                    location="Railay, Krabi"
                ),
                activities=[
                    ActivityCreate(
                        name="Kayaking Adventure",
                        description="Kayak around limestone cliffs and into caves",
                        location="Ao Thalane",
                        duration_hours=4.0
                    ),
                    ActivityCreate(
                        name="Sunset Beach Dinner",
                        description="Private dinner on the beach",
                        location="Phra Nang Beach",
                        duration_hours=2.0
                    )
                ],
                transfers=[
                    TransferCreate(
                        from_location="Rayavadee Resort",
                        to_location="Ao Nang Pier",
                        transfer_type="Speedboat"
                    ),
                    TransferCreate(
                        from_location="Ao Nang Pier",
                        to_location="Krabi International Airport",
                        transfer_type="Car"
                    )
                ]
            )
        ]
    )
    
    # Create itineraries in the database
    from app import crud
    
    itineraries = [
        phuket_2_nights,
        phuket_4_nights,
        krabi_3_nights,
        phuket_krabi_7_nights,
        krabi_5_nights,
        phuket_8_nights,
        krabi_6_nights
    ]
    
    for itinerary in itineraries:
        crud.create_itinerary(db, itinerary)
    
    print("Database seeded successfully with recommended itineraries!")
    
if __name__ == "__main__":
    seed_data()