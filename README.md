# Playwright with Python: Free Course Code

Code for my free **Playwright with Python** course on YouTube. Each test file matches a lesson, so you can follow along or jump straight to the finished code.

- Watch the course, all lessons in order: https://www.youtube.com/playlist?list=PLSIdyj4vSRGs
- Prefer one video? Full course: https://youtu.be/oENp9z_fFmY
- Free Udemy version with quizzes: https://www.udemy.com/course/get-started-with-playwright-python-test-automation-basics/

The tests run against [qa-cart.com](https://qa-cart.com/demoshop/), a demo store built for practising test automation.

## Lessons and code

| Lesson | Video | Code |
|---|---|---|
| 1. Install and Setup | https://youtu.be/2wSkiVAXvHo | `requirements.txt` |
| 2. Your First Test, Written from Scratch | https://youtu.be/EEQmT9RYg2M | `tests/concepts/test_homepage.py` |
| 3. Locators and Auto-Waiting | https://youtu.be/FaTC1oB6rKA | `tests/concepts/test_locators.py` |
| 4. expect Assertions with a Search Test | https://youtu.be/IEWJ27rSQSg | `tests/concepts/test_search.py` |
| 5. Data-Driven Testing | https://youtu.be/TxsWwlks9J4 | `tests/concepts/test_data_driven.py` |
| 6. HTML Report and Trace Viewer | https://youtu.be/KXhrng738dw | Commands below |

## Setup

You need Python 3.10 or newer.

```bash
git clone https://github.com/anuradha-learn/playwright-python-course-yt.git
cd playwright-python-course-yt

python -m venv venv
# macOS or Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
playwright install
```

## Run the tests

```bash
# Run all tests (headless)
pytest

# Watch the browser while tests run
pytest --headed

# Run one file
pytest tests/concepts/test_search.py
```

## HTML report and Trace Viewer (lesson 6)

```bash
# HTML report
pytest --html=report.html --self-contained-html

# Record a trace only when a test fails
pytest --tracing=retain-on-failure

# Open a trace
playwright show-trace test-results/<test-folder>/trace.zip
```

## Next steps

- New to Python? Python and Git for Testers: https://www.youtube.com/playlist?list=PLbdk4_6KQS2o
- Build a full framework with Page Objects, fixtures and CI/CD in my Playwright with TypeScript course: https://www.udemy.com/course/playwright-automation-basics-to-advance-typescript/
- More free courses and articles: https://anuradhaagarwal.com

Questions or something not working? Comment on the lesson video and I'll help.
