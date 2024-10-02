"""
Retrieve a quote from ChatGPT using a user provided subject and a predefined system prompt.
"""

from flask import jsonify


def generate_quote(request, client, deployment_name):

    data = request.json
    userPrompt = data.get("prompt")
    systemPrompt = "You are a tutor teaching about LLMs. The stidents are entering prompts for you to execute and ealuate."

    if userPrompt:

        completion = client.chat.completions.create(
            model=deployment_name,  # e.g. gpt-35-instant
            messages=[
                {
                    "role": "system",
                    "content": systemPrompt,
                },
                {
                    "role": "user",
                    "content": userPrompt,
                },
            ],
        )

        print(completion.model_dump_json(indent=2))

        quote = completion.choices[0].message.content

        return jsonify({"quote": quote})

    else:
        return jsonify({"error": "User prompt parameter is missing."})
