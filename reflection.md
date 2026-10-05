# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
  1. The hints were backwards: In my first game, the secret was 35. I submitted for 50 for the first attempt, but the hint was "Go higher", which should have been "Go lower". The code is located in function check_guess() in app.py.
  2. Pressing Enter did nothing: Every time I tried to press "Enter" to submit my answer, nothing happened. I had to manually click on the submit answer button. The code is located in lines 121 - 128 in app.py
  3. New Game doesn't really reset: After I used all my attempts in first game, I pressed the new Game to restart. But the page still says "Game over". The code is in app.py lines 134-138

**Bug Reproduction Log**

| # | Input / Trigger | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|---|-----------------|-------------------|-----------------|------------------------|-------------------------|
| 1 | Guess a number above the secret (e.g. secret is 40, guess 60) | "Too High" with a hint to go **lower** | Shows "Too High" but the message says "Go HIGHER!". A guess below the secret gets "Go LOWER!". The hints are backwards. | None (no error, just wrong output) | `app.py`, `check_guess()` (lines 37-40) |
| 2 | Type a number in the text box and press **Enter** (without clicking Submit) | The guess is submitted, like clicking "Submit Guess" | Nothing is submitted and no attempt is counted. Only clicking the button works. | None | `app.py`, the `st.text_input` + `st.button("Submit Guess")` section (lines 121-128, and `if submit:` at line 147). |
| 3 | Win or lose a round, then click **New Game** and try to guess again | A fresh game: new secret, attempts, score and history cleared, and guessing works again | The page still says "You already won" / "Game over" and stops. Score and history carry over. The secret is always drawn from 1-100 even on Easy/Hard, and attempts resets to 0 (not 1 like the first game). | None | `app.py`, `if new_game:` block (lines 134-138). |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - **A correct suggestion: swap the backwards hint messages in `check_guess()`.**
    - *What the AI suggested:* Claude pointed at `check_guess()` and said the two hint strings were attached to the wrong outcomes: "Too High" returned "Go HIGHER!" and "Too Low" returned "Go LOWER!". Its fix was to swap the messages, not to change the `guess > secret` comparison. It also changed the same strings in the `except TypeError` fallback branch, which had the same mistake.
    - *Why it was correct:* The comparison itself was fine. The bug was only in the text shown to the player, so swapping the messages is the smallest change that fixes it. Changing the comparison instead would have mislabeled the outcome that `update_score()` uses for scoring.
    - *How I verified it:* I added regression tests in `tests/test_game_logic.py` that check the message, not just the outcome: `check_guess(60, 50)` must return "Too High" with "LOWER" in the message, and `check_guess(40, 50)` must return "Too Low" with "HIGHER". The original tests only checked the outcome label, which is why they never caught this bug.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  - **A suggestion I did not accept as written: wrap the input in `st.form` to make Enter submit.**
    - *What the AI suggested:* To fix "pressing Enter does nothing", Claude put the text box and a `st.form_submit_button` inside an `st.form`. That is the standard Streamlit way to get Enter-to-submit.
    - *Why I changed it:* A form can't contain a normal `st.button`, so the form version forced the layout to change from three columns (Submit / New Game / Show hint) to two. The "Submit Guess" button also moved out of the row it was in. I wanted the original layout kept, so it was a poor fit for how I wanted the page to look. We switched to giving `st.text_input` an `on_change` callback that sets a flag in `st.session_state`, and `submit` is true if either the flag or the button fired. This keeps all three columns.
    - *Trade-off I'm aware of:* `on_change` also fires if the text changes and the box loses focus (for example clicking elsewhere), so it can submit without Enter. I accepted that for now to keep the layout.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
