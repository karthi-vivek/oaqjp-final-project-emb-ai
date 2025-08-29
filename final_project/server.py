"""Flask server for emotion detection API."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze text input from request and return detected emotions."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return_text = "Invalid text! Please try again!"
    else:
        r1 = response['anger']
        r2 = response['disgust']
        r3 = response['fear']
        r4 = response['joy']
        r5 = response['sadness']
        # Return a formatted string with the sentiment label and score
        return_text = (
            f"For the given statement, the system response is "
            f"'anger': {r1}, 'disgust': {r2}, 'fear': {r3}, 'joy': {r4},"
            f" and 'sadness': {r5}. "
            f"The dominant emotion is {dominant_emotion}"
            )

    return return_text

@app.route("/")
def render_index_page():
    """Render the index HTML page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
