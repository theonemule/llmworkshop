from flask import Flask, request, jsonify, send_from_directory
import whisper
from io import BytesIO
import os
import uuid  # Import the uuid module

model = whisper.load_model("base")

def transcribe_audio(request, client, deployment_name):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    prompt = request.form['prompt'] or "You are an assistant to smooth out the raw text from a transcription. Please correct the text so that it smooth and reads well rather than just raw text."

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Save the file temporarily
        filename = f"{uuid.uuid4().hex}_temp_audio.ogg"
        file.save(filename)

        print(filename)

        # Transcribe the audio file
        result = model.transcribe(filename)

        # Remove the temporary file
        os.remove(filename)
        
        print(result["text"])


        completion = client.chat.completions.create(
            model=deployment_name,  # e.g. gpt-35-instant
            messages=[
            {"role": "system", "content": prompt},
                {"role": "user", "content": result["text"]}
            ]
        )        


        return jsonify({'transcription': result["text"],'formatted': completion.choices[0].message.content})

    return jsonify({'error': 'Invalid file'}), 400

