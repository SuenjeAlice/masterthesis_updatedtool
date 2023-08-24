# Updated Masterthesis Tool
### Using the OpenAI API Quickstart Tutorial

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup
1. Clone repository and add .env files:
    ```bash
   $ git clone https://github.com/SuenjeAlice/masterthesis_updatedtool.git
   $ cp .env.example .env
   ```
3. Install requirements:

   ```bash
   $ Set-ExecutionPolicy Unrestricted -Scope Process
   $ python -m venv venv
   $ . venv/Scripts/activate
   $ pip install -r requirements.txt
   ```
4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.
5. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
