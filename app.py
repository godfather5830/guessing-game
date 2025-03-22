from flask import Flask, render_template, request, session, redirect, url_for
import random
import math

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_game():
    target = random.randint(0, 10**6)  # Infinite-like range
    session['target'] = target
    session['attempts'] = 10
    session['hints'] = []
    session['range_start'] = max(0, target - random.randint(50, 500))
    session['range_end'] = target + random.randint(50, 500)
    return redirect(url_for('game'))


@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'target' not in session:
        return redirect(url_for('index'))

    target = session['target']
    attempts = session['attempts']
    hints = session['hints']
    range_start = session['range_start']
    range_end = session['range_end']
    guess = None
    message = None
    sound = None

    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts -= 1
        session['attempts'] = attempts

        if guess == target:
            sound = 'you-win-sequence-2-183949'
            return redirect(url_for('result', result='win'))
        elif attempts == 0:
            sound = 'calm-god-dammit-82692'
            return redirect(url_for('result', result='lose'))
        else:
            if guess < target:
                message = "📈 Go Higher!"
            else:
                message = "📉 Go Lower!"

            # Provide a hint every 3rd attempt, limit to 3 hints
            if attempts % 3 == 0 and len(hints) < 3:
                hint = generate_hint(target, len(hints) + 1)
                hints.append(hint)
                session['hints'] = hints
                sound = 'in-game-level-uptype-2-230567'

    return render_template(
        'game.html',
        attempts=attempts,
        message=message,
        hints=hints,
        range_start=range_start,
        range_end=range_end,
        sound=sound,
    )


@app.route('/result/<result>')
def result(result):
    win_video = '6265099-uhd_2160_3840_30fps.mp4'
    lose_video = '7915046-hd_1080_1920_30fps.mp4'

    sound = 'you-win-sequence-2-183949' if result == 'win' else 'calm-god-dammit-82692'
    return render_template(
        'result.html',
        result=result,
        video=win_video if result == 'win' else lose_video,
        sound=sound,
    )


def generate_hint(target, level):
    """Dynamically generates hints based on difficulty."""
    if level == 1:
        return f"Hint: The number is {'even' if target % 2 == 0 else 'odd'}."
    elif level == 2:
        divisor = random.choice([2, 3, 4, 5, 8, 10])
        return (
            f"Hint: The number is a multiple of {divisor}."
            if target % divisor == 0
            else f"Hint: The number is not a multiple of {divisor}."
        )
    elif level == 3:
        sqrt_val = math.isqrt(target)
        return f"Hint: The square root is approximately {sqrt_val}."
    else:
        return "No more hints available."


if __name__ == '__main__':
    app.run(debug=True)
