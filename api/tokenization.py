from flask import jsonify
import tiktoken

def tokenize_text(request, deployment_name):
    """
    Tokenize user input.

    Args:
        request (object): The request object containing the user input.
        deployment_name (str): The token reference model from which the encoding is derived.

    Returns:
        Response: A Flask Response object containing the JSON representation of the tokens and the count of tokens.

    Raises:
        ValueError: If the token count is zero.
    """
    data = request.json
    user_input = data.get("prompt")

    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    tokens = encoding.encode(user_input)

    token_count = len(encoding.encode(user_input))
    if not token_count:
        raise ValueError("Token count is zero.")

    tokens_json = {
        "tokens": tokens,
        "count": token_count
    }

    return jsonify(tokens_json)
