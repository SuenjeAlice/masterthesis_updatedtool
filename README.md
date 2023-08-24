# Updated Masterthesis Tool
### Using the OpenAI API Quickstart Tutorial [quickstart tutorial](https://beta.openai.com/docs/quickstart)

## Setup
1. Clone repository and add .env files:
    ```bash
   git clone https://github.com/SuenjeAlice/masterthesis_updatedtool.git
   ```
   ```bash
   cp .env.example .env
   ```
3. Install requirements:

   ```bash
   Set-ExecutionPolicy Unrestricted -Scope Process
   python -m venv venv
   . venv/Scripts/activate
   pip install -r requirements.txt
   ```
4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.
5. Run the app:

   ```bash
   flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
