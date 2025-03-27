
# Project Setup Instructions

Follow these steps to set up and run the project:

## 1. Create a Python Virtual Environment

Use the following command to create a virtual environment:

```bash
python -m venv {name_of_env}
```

### Activate the Environment
```bash
{name_of_env}\Scripts\activate
```

## 2. Install Requirements

Ensure your environment is activated, then install the required dependencies:

```bash
pip install -r requirements.txt
```

## 3. Generate the Model File

Run the model preprocessing script to generate the `.pkl` file:

```bash
python model_preprocessing.py
```

This will process the data and save the model as a `.pkl` file for later use.

## 4. Run the Application

After the model is created, you can launch the web application using:

```bash
python app.py
```

The application will be accessible at:

http://127.0.0.1:5000/

## 5. Usage
- Enter your ticket description in the text box.
- Click on **Classify Ticket**.
- The application will predict and display the category of your ticket.

## Troubleshooting
- Ensure Python and `pip` are installed and available in your system path.
- Check if `requirements.txt` has been installed successfully.
- Confirm that `model.pkl` is generated after running `model_preprocessing.py`.
- Verify the app is running using `http://127.0.0.1:5000/` in your browser.

## Additional Notes
- Update the `model_preprocessing.py` if you need to retrain the model with new data.
- The data is available in the dataset directory, and you can update it as needed.
- Logs and error messages will be printed in the terminal while running the app.
