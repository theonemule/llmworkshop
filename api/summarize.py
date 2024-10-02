from flask import jsonify, request
import requests
from bs4 import BeautifulSoup
import tiktoken

def scrape_wikipedia_article(url):
    # Send a GET request to the Wikipedia URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title of the article
        title = soup.find('h1', id='firstHeading').text
        
        # Find the content of the article
        content = soup.find('div', id='mw-content-text')
        
        if content:
            # Extract text from all paragraphs within the content
            paragraphs = content.find_all('p')
            
            # Join all paragraph texts into a single string
            article_text = '\n'.join([p.text for p in paragraphs])
            
            return {
                'title': title,
                'content': article_text
            }
        else:
            return {'error': 'Failed to find the content section of the Wikipedia article.'}
    else:
        return {'error': f'Failed to retrieve the Wikipedia article. Status code: {response.status_code}'}

def summarize_text(text, prompt, client, deployment_name):
    # Tokenize the text to get an accurate token count
   
    enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
    
    tokens = enc.encode(text)
     
    chunks = []
    while tokens:
        chunk_tokens = tokens[:15000]
        chunk_text = enc.decode(chunk_tokens)
        chunks.append(chunk_text)
        tokens = tokens[15000:]
    
    summaries = []
    for chunk in chunks:
        completion = client.chat.completions.create(
            model=deployment_name,  # e.g. gpt-35-instant
            messages=[
                {
                    "role": "system",
                    "content": "Summarize the user's text according to this scheme: " + prompt,
                },
                {
                    "role": "user",
                    "content": chunk,
                },
            ],
        )
        
        print (completion.model_dump_json(indent=2))
        
        summary = completion.choices[0].message.content
        
        summaries.append(summary)
                       
    return '\n'.join(summaries)


def scrape_and_summarize(request, client, deployment_name):
    # Get the URL from the request query parameters
    url = request.args.get('url')
    prompt = request.args.get('prompt') or "Summarize the content from Wikipedia in one or two paragraphs."
    
    if url:
        # Call the scrape_wikipedia_article function
        article_data = scrape_wikipedia_article(url)
        
        if 'error' not in article_data:
            # Call the summarize_text function
            summary = summarize_text(article_data['content'], prompt, client, deployment_name)
            return jsonify({'title': article_data['title'], 'summary': summary})
        else:
            return jsonify({'error': article_data['error']})
    else:
        return jsonify({'error': 'URL parameter is missing.'})

