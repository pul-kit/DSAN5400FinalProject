
def welcome_message():
    print("Hello! Welcome to an AI assistant designed for Canvas, Turnitin and Zoom!")
    print("Directly type your question and I will do my best to answer!")
    print("Type 'help' to learn more about me.")

def get_user_input():
    return input("You: ")

def display_bot_response(response):
    print("AI:", response)

def ask_for_rating():
    rating = input("Was I helpful? Let me know how I can be improved.")
    #TODO Replace File path with actual path
    with open(file_path, 'a', newline='') as csv:
        csv_writer = csv.writer(csv)
        csv_writer.writerow([rating])
    print(f'Data appended to CSV file successfully.')
    
def main():
    welcome_message()

    while True:
        user_input = get_user_input()

        # Help user if input is help
        if user_input.lower() == 'help':
            display_bot_response("I am a bot that has been trained on FAQs about Canvas, Turnitin and Zoom. I don't have the capabliity to remember previous inputs. Type 'data' to know more about my training data.")
        
        # Exit if input is exit 
        elif user_input.lower() == 'exit':
            display_bot_response("Goodbye!")
        
        # Tell user data used if input is data
        elif user_input.lower() == 'data':
            display_bot_response("Here is a link to the data I have been trained on.")
            display_bot_response("Zoom: https://uis.georgetown.edu/zoom/faq/")
            display_bot_response("Canvas: https://community.canvaslms.com/t5/Instructor-Guide/tkb-p/Instructor")
            display_bot_response("Turnitin: https://www.turnitin.com/help_pages/instructor_faq.asp?")
        
        # Answer user's question
        else:
            #TODO Connect to Tianze's work
            rating = ask_for_rating()

if __name__ == "__main__":
    main()