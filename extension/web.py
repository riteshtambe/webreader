class webreader:
    def __init__(self , url_link):
        self.url_link = url_link
        # self.question = question
    def scrape(self):
        import requests
        from bs4 import BeautifulSoup
        import re
        import spacy
        import openai

        # URL of the website you want to scrape
        url = self.url_link   # Replace with your desired URL

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove script and style tags and their content
            for script in soup(['script', 'style']):
                script.extract()

            #  Get the remaining text
            text = soup.get_text()

            # Clean up the text by removing extra whitespace and newlines
            text = re.sub(r'\s+', ' ', text).strip()

            # Print the cleaned and extracted text
            # print("This is the text from the website which we are scraping")
            # print(text)
            # print()
            # print(len(text))
            # print("-----------------------------------------------")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


        # The text you want to clean
        text = f'''{text}'''

        # Remove special characters and icons
        cleaned_text = re.sub(r'[^\w\s]', '', text)

        # Remove extra whitespaces
        clean_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        # print("This is the text with the removal of the Whitespaces and icons which is not important")
        # print(cleaned_text)
        # print("-----------------------------------------------")
        # print()
        # print(len(cleaned_text))
        # Load the spaCy English language model
        nlp = spacy.load('en_core_web_sm') #English language model provided by spaCy

        # The text you want to process
        text = f"""{clean_text}"""

        # Process the text with spaCy
        doc = nlp(text)

        # Remove stop words
        filtered_tokens = [token.text for token in doc if not token.is_stop]

        # Join the remaining tokens into a string
        cleaned_text = ' '.join(filtered_tokens)

        # print("This is the text with the removal of the Stopwords")
        # print(cleaned_text)
        # print()
        # print(len(cleaned_text) ) 
        # print("-----------------------------------------------")

        # Load the spaCy English language model
        nlp = spacy.load('en_core_web_sm')

        # The text you want to process
        text = f"""{cleaned_text}"""

        # Process the text with spaCy
        doc = nlp(text)

        # Remove spaces and punctuation
        filtered_tokens = [token.text for token in doc if not token.is_space and not token.is_punct]

        # Join the remaining tokens into a string
        cleaned_text = ''.join(filtered_tokens)

        # print("This is the text with the removal of the Spaces and Punctuations")
        # print(cleaned_text)
        # print()
        # print(len(cleaned_text))
        # print("-----------------------------------------------")

        return cleaned_text

    def Q_and_a(self,cleaned,):
        import openai
        cleaned_text = cleaned
            # Set your OpenAI API key
        api_key = "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"
        openai.api_key = api_key

        # Your context and question
        context = f"{cleaned_text}"
        question = input("Question : ")
        print(question + "?")
        print()

        # Parameters for completions.create
        max_tokens = 100
        stop_sequence = None  # Define your stop sequence if needed

        # Make the API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\n"},
                {"role": "user", "content": f"Context: {context}\n\n---\n\nQuestion: {question}\nAnswer:"}
            ],
            temperature=0.5,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=stop_sequence,
        )

        # Extract the generated answer from the response
        generated_answer = response['choices'][0]['message']['content']

        return "This is the generated ans: "+generated_answer
        







        
        
url = "https://docs.djangoproject.com/en/4.2/"
# question = "What is inside the text"
obj = webreader(url)
print(obj.Q_and_a(obj.scrape()))