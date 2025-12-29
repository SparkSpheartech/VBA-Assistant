import os
import re
import PyPDF2
from openai import OpenAI
import sys

# ✅ Define Assistant Name
ASSISTANT_NAME = "VBA Assistant"

# ✅ Initialize LM Studio AI Client
# Note: This assumes LM Studio is running locally.
client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
MODEL = "deepseek-r1-distill-qwen-7b"
MAX_TOKENS = 4000

# ✅ Store chat history
chat_history = [
    {"role": "system", "content": "You are the VBA Assistant, an expert on the 'Virtual Benefits Administrator' (VBA) software and the 834 Benefit Enrollment Companion Guide. Help users understand the file specifications, segment requirements, and account structures."}
]

# ✅ Step 1: Extract text from the PDF
# RELATIVE PATH: Looks for 'docs/vba_834_guide.pdf' relative to this script
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "docs", "vba_834_guide.pdf")

def extract_text_from_pdf(pdf_path):
    """ Extracts text from the entire PDF document while handling errors and empty pages. """
    if not os.path.exists(pdf_path):
        print(f"❌ Error: Required PDF not found at {pdf_path}")
        print("Please ensure 'vba_834_guide.pdf' is in the 'docs' folder.")
        return []

    extracted_text = []
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"✅ Loading {len(reader.pages)} pages from documentation...")
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text.append(text.strip())
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return []
        
    return extracted_text

# Extract PDF content
pdf_content = extract_text_from_pdf(pdf_path)

# ✅ Step 2: Extract Keywords from User Query
def extract_keywords(user_query):
    """ Extracts relevant keywords from the user's query to filter PDF content. """
    common_words = {"what", "is", "the", "how", "do", "i", "a", "to", "of", "and", "in", "on", "for", "with", "by", "it", "guide", "tell", "me", "about"}
    words = re.findall(r'\b\w+\b', user_query.lower())
    keywords = [word for word in words if word not in common_words]
    return keywords

# ✅ Step 3: Filter Relevant PDF Pages Based on Keywords
def filter_pdf_content(user_query, pdf_content, max_chars=12000):
    """ Returns only relevant PDF sections based on keywords. """
    keywords = extract_keywords(user_query)
    
    # If no keywords (e.g. "Summarize this"), take beginning
    if not keywords:
        return ''.join(pdf_content[:5])[:max_chars]

    scores = []
    for page in pdf_content:
        score = sum(1 for k in keywords if k in page.lower())
        scores.append((score, page))
    
    # Sort by relevance (highest score first)
    scores.sort(key=lambda x: x[0], reverse=True)
    
    # Take top 5 relevant pages
    filtered_pages = [page for score, page in scores if score > 0][:5]
    
    if not filtered_pages:
        # Fallback to first few pages if no keyword match
        return ''.join(pdf_content[:3])[:max_chars]

    relevant_text = ''.join(filtered_pages)[:max_chars]
    return relevant_text

# ✅ Step 4: Chatbot Function
def chatbot_response(user_query):
    """ Generates a response based on the user's question and relevant document content. """
    relevant_content = filter_pdf_content(user_query, pdf_content)

    if not relevant_content.strip():
        return "⚠️ No relevant content found in the document."

    # Construct Prompt
    chat_history.append({"role": "user", "content": f"{user_query}\n\nReference Documentation Content:\n{relevant_content}"})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=chat_history,
            max_tokens=MAX_TOKENS,
            stream=True
        )

        print("\n🤖 VBA ASSISTANT:")
        collected_response = ""
        for chunk in response:
            text = chunk.choices[0].delta.content or ""
            collected_response += text
            print(text, end="", flush=True)
        
        print("\n")
        chat_history.append({"role": "assistant", "content": collected_response})
        return collected_response

    except Exception as e:
        print("\n")
        print(f"⚠️ Error connecting to AI: {e}")
        print("Ensure LM Studio is running and the server is started on port 1234.")
        return "AI Error"

# ✅ Step 5: Interactive Chat Loop
if __name__ == "__main__":
    print("\n" + "="*50)
    print(f"👋 {ASSISTANT_NAME} Online")
    print(f"📚 Loaded Knowledge Base: {os.path.basename(pdf_path)}")
    print("="*50 + "\n")

    while True:
        try:
            user_question = input("📝 Ask about the spec: ")
            if user_question.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Saving session. Goodbye!\n")
                break
            
            chatbot_response(user_question)
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            break
