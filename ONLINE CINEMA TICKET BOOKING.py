class MovieTicketBooking:
    def _init_(self):
        print("WELCOME TO THE MOVIE SHOWS")
        
    def TicketBooking(self):
        while True:
            print("WELCOME TO THE MOVIE SHOWS")
            print("LANGUAGES:")
            print("1. ENGLISH")
            print("2. TAMIL")
            print("3. TELUGU")
            print("4. HINDI")
            print("5. KANNADA")
            print("6. MALAYALAM")
            movies = { "ENGLISH" : ["BAD-BOYS RIDE OR DIE","KUNG-FU-PANDA 4","GARFIELD","FURIOSA MAD-MAX"],
            "TAMIL" : ["GARUDAN","WEAPON","ARANMANAI-4","PT SIR"],
            "TELUGU" : ["MANAMEY","SATHYABHAMA","GANGS OF GODAVARI","MAHARAJA"],
            "HINDI" : ["CHANDU CHAMPION","SRIKANTH","MR & MRS MAHI","SAVI"],
            "KANNADA" : ["SAHARA","ANARTHA","ROBERT","THE JUDGEMENT"],
            "MALAYALAM" : ["THALAM","GOLAM","MANJUMMEL-BOYS","GRRR"] }
            
            Language = input("CHOOSE YOUR LANGUAGE: ").upper()
            if Language in ["ENGLISH","TAMIL","TELUGU","HINDI","KANNADA","MALAYALAM"]:
                break
            else:
                print("PLEASE .........ENTER AVAILABLE LANGUAGES")
            
        while True:
            print("AVAILABLE MOVIES:")
            for movie in movies[Language]:
              print(movie)
            selected_movie = input("CHOOSE YOUR MOVIE: ").upper()
            if selected_movie in [movie.upper() for movie in movies[Language]]:
                print("HELLO & WELCOME!..PLEASE CHECK THE LOCATION OF THE THEATRES")
                break
            else:
                print("PLEASE.........ENTER AVAILABLE MOVIES")
                
        while True:
            print("AVAILABLE THEATRES:") 
            print("1. AGS") 
            print("2. SATHYAM CINEMAS") 
            print("3. PVR CINEMAS") 
            print("4. IMAX")
            print("5. CASINO")
            Theatre = input("CHOOSE YOUR THEATRE: ")
            if Theatre in ["AGS","SATHYAM CINEMAS","PVR CINEMAS","IMAX","CASINO"]:
                print("WONDERFULL SELECT.........PLEASE PROCEED THE TIMINGS OF THE SHOW")
                break
            else:
                print("PLEASE.......ENTER AVAILABLE THEATRES")
                
        while True:
            Time=input("10:30AM // 12:00PM // 1:30PM // 2:45PM // 3:00PM ")
            if Time=="10:30AM" or Time=="12:00PM" or Time=="1:30PM" or Time=="2:45PM" or Time=="3:00PM":
                print("PLEASE SELECT YOUR SEATS")
                print("AVAILABLE SEATS = 70")
                print("PRICE = 210")
                Price = 210
                break
            else:
                print("PLEASE.......ENTER AVAILABLE TIMINGS")
                
        while True:
            Tickets=int(input("ENTER YOUR TICKETS: "))
            if Tickets <= 10:
                Money=Tickets*Price
                print("Total Price :", Money)
                break
            else:
                print("YOU CAN BOOK A MAXIMUM OF 10 TICKETS AT A TIME.")
                
        while True:
            Payment=input("PLEASE SELECT A PAYMENT METHOD: CASH || CARD ").upper()
            if Payment == "CASH":
                print("YOU HAVE SELECTED TO PAY BY CASH")
                print("\nBOOKING DETAILS:")
                print("MOVIE:", selected_movie,[Language])
                print("THEATRE:", Theatre)
                print("SHOW TIME:", Time)
                print("NUMBER OF TICKETS:", Tickets)
                print("TOTAL COST:", Money)
                print("PAYMENT METHOD:", Payment)
                print("PAYMENT STATUS: PAYMENT PENDING")
                print("PLEASE PROCEED TO THE COUNTER TO COMPLETE YOUR PAYMENT.")
                break
            
            elif Payment == "CARD":
                print("YOU HAVE SELECTED TO PAY BY CARD")
                Card_Number = input("ENTER YOUR CARD NUMBER: ")
                Expiry_Date = input("ENTER YOUR CARD EXPIRY DATE (MM // YY): ")
                PIN = int(input("ENTER YOUR PIN: "))
                print("PROCESSING YOUR PAYMENT...........")
                print("PAYMENT SUCCESSFULL! YOUR TICKETS HAVE BEEN BOOKED")
                print("\nBOOKING DETAILS:")
                print("MOVIE:", selected_movie,[Language])
                print("THEATRE:", Theatre)
                print("SHOW TIME:", Time)
                print("NUMBER OF TICKETS:", Tickets)
                print("TOTAL COST:", Money)
                print("PAYMENT METHOD:", Payment)
                print("PAYMENT STATUS: PAYMENT SUCCESSFULL")
                print("THANK YOU.....PLEASE VISIT NEXT TIME")
                print("HAVE A NICE DAY :)")
                break
            else:
                print("INVALID PAYMENT METHOD SELECTED! PLEASE ENTER CASH OR CARD.")
                
booking = MovieTicketBooking()
booking.TicketBooking()
                
                
                
                
                
                
                


