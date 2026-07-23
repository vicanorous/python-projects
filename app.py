from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = "game-secret-key"

@app.route("/")
def home():
    # Render the initial page setup
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def process_guess():
    # Extract JSON data sent from JavaScript
    data = request.get_json()
    guess = int(data.get("guess"))
    
    session["attempts"] += 1
    secret = session.get("secret_number")
    
    if guess < secret:
        return jsonify({
            "status": "continue", 
            "message": "Too low! Try higher.",
            "attempts": session["attempts"]
        })
    elif guess > secret:
        return jsonify({
            "status": "continue", 
            "message": "Too high! Try lower.",
            "attempts": session["attempts"]
        })
    else:
        attempts_taken = session["attempts"]
        # Reset game session for next time
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0
        return jsonify({
            "status": "win", 
            "message": f"🎉 Correct! You won in {attempts_taken} attempts.",
            "attempts": attempts_taken
        })

if __name__ == "__main__":
    app.run(debug=True)