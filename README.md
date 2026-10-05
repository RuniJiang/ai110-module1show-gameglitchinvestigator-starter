# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience
- [ ] Describe the game's purpose.
  - A Streamlit number guessing game. You guess a secret number and get higher/lower hints. Score and attempts depend on the difficulty.
- [ ] Detail which bugs you found.
  - The hints were backwards. "Too High" said "Go HIGHER!".
  - On even attempts the secret was passed as a string, so "9" > "50" was true.
- Pressing Enter did not submit a guess.
- [ ] Explain what fixes you applied.
  - Swapped the hint messages so "Too High" says "Go LOWER!".
  - Removed the string fallback so guesses are always compared as ints.
  - Added an `on_change` callback so Enter submits and the three-column layout stays.
  - Moved the game logic into `logic_utils.py`.
  - Updated the tests and added regression tests for hint direction and number comparison.

## 📸 Demo Walkthrough

A sample game on **Normal** difficulty (range 1–100, 8 attempts) where the secret number is 55:

1. The game starts with a score of 0. The player types `40` and presses Enter (or clicks Submit).
2. The game returns "📈 Go HIGHER!" (Too Low), and the score drops to -5.
3. The player guesses `70`. The game shows "📉 Go LOWER!" (Too High), and the score goes to 0 (a Too High guess on an even-numbered attempt adds 5).
4. The player guesses `55`. The game shows "🎉 Correct!" and balloons appear.
5. The score updates for the win: 100 - 10 × (3 + 1) = 60 points are added, so the final score is 60.
6. The game ends after the correct guess. Further guesses are blocked with "You already won. Start a new game to play again." until the player clicks New Game.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
