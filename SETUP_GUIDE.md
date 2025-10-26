# Quick Setup Guide

## How to Run the Application

### Step 1: Install Dependencies
Open terminal/PowerShell in the project directory and run:
```bash
pip install -r requirements.txt
```

### Step 2: Add Student Data
The file `bunny.csv` contains sample data. You can:
- Use the existing sample data (5 students with roll numbers 101-105)
- Replace it with your own CSV file following the same format

### Step 3: Add Student Photos (Optional)
Place student photos in the `images/` folder:
- Name them as `<roll_number>.jpg` or `<roll_number>.png`
- Example: `images/101.jpg`, `images/102.png`

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Website
Open your browser and go to:
```
http://localhost:5000
```

### Step 6: Test the Application
Try logging in with:
- Roll Number: **101** (Alice Johnson)
- Roll Number: **102** (Bob Smith)
- Roll Number: **103** (Charlie Brown)
- Roll Number: **104** (Diana Prince)
- Roll Number: **105** (Emma Watson)

## Features Explained

1. **Dashboard**: Enter roll number to access student dashboard
2. **Student Details Page**: Shows personalized graphs including:
   - Subject-wise marks
   - CGPA comparison with class average
   - Monthly attendance tracking
   - Performance grade distribution
   - Personalized feedback

## Customizing the CSV

Your CSV should include:
- **roll**: Student roll number (unique)
- **name**: Student name
- **cgpa**: Cumulative Grade Point Average
- **attendance**: Overall attendance percentage
- **behavior_grade**: Behavior grade (A, B, C, D)
- **performance_grade**: Performance grade (A, B, C, D)
- **Monthly columns**: jun, jul, aug, sep, oct, nov, dec, jan, feb, mar
- **Subject columns**: Add as many as needed (e.g., math, physics, chemistry, english, computer)

## Troubleshooting

**Error: No module named 'Flask'**
- Run: `pip install -r requirements.txt`

**Error: Student not found**
- Make sure the roll number exists in `bunny.csv`
- Check for typos in the CSV file

**Graphs not displaying**
- Make sure matplotlib is properly installed
- Check that all required columns exist in the CSV

**Port already in use**
- Change the port in `app.py` from `app.run(debug=True)` to `app.run(debug=True, port=5001)`

## Need Help?

Check the main `README.md` for detailed documentation.

