import openai
import pdfplumber

openai.api_key = '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'

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def chat_with_gpt(prompt):
    if prompt.startswith("read"):
        pdf_path = prompt[5:].strip()  # Extract the path from user input
        text = extract_text_from_pdf(pdf_path)
        # print(text)
        response = chat_with_gpt("Become an expert on this topic and give me a brief summary: " + text)  # Recursively call chat_with_gpt with extracted text
        # response = chat_with_gpt("Can you explain what this text is: " + text)  # Recursively call chat_with_gpt with extracted text
    else:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=2000,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=10
        )
        response = response.choices[0].text.strip()
    return response

# print(extract_text_from_pdf("washer.pdf"))

while True:
    user_input = input("User: ")
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)
