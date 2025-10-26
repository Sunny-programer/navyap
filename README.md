# Student Academic Dashboard Web Application

A Flask-based web application that generates personalized academic performance reports and graphs for students.

## Features

- **Student Login**: Students can enter their roll number to access their dashboard
- **Academic Performance Graphs**: 
  - Subject-wise marks bar chart
  - CGPA vs Class Average comparison
  - Month-wise attendance tracking
  - Performance grade distribution
  - Student photo display
  - Personalized feedback report
- **Modern UI**: Beautiful, responsive design with gradient backgrounds
- **Real-time Data**: Graphs are generated dynamically from CSV data

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

### 1. Prepare Your CSV File

Create a CSV file named `bunny.csv` with the following structure:

- `roll`: Student roll number
- `name`: Student name
- `cgpa`: CGPA value
- `attendance`: Overall attendance percentage
- `behavior_grade`: Behavior grade (A, B, C, D)
- `performance_grade`: Performance grade (A, B, C, D)
- Monthly attendance columns: `jun`, `jul`, `aug`, `sep`, `oct`, `nov`, `dec`, `jan`, `feb`, `mar`
- Additional subject columns (e.g., `math`, `physics`, `chemistry`, etc.)

### 2. Add Student Images (Optional)

Place student photos in the `images/` folder named as `<roll_number>.jpg` or `<roll_number>.png`

Example:
- `images/101.jpg` for student with roll number 101
- `images/102.png` for student with roll number 102

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter a student's roll number
3. Click "View Dashboard" to see the personalized academic report with graphs

## File Structure

```
.
├── app.py                  # Flask backend application
├── bunny.csv              # Student data CSV file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── images/               # Student photos directory
│   ├── 101.jpg
│   ├── 102.png
│   └── ...
├── templates/            # HTML templates
│   ├── index.html       # Login/dashboard page
│   └── student_details.html  # Student details page
└── static/              # CSS and static files
    └── style.css        # Stylesheet
```

## API Endpoints

- `GET /` - Main dashboard/login page
- `POST /login` - Authenticate student by roll number
- `GET /student/<roll>` - View student details and graphs
- `GET /api/student/<roll>` - Get student data as JSON

## Customization

### Adding More Subject Columns

Simply add new columns to your CSV file (e.g., `english`, `history`, `geography`). The application will automatically detect and display them.

### Modifying Graph Styles

Edit the plotting code in the `generate_graph_base64()` function in `app.py` to customize colors, layouts, and chart types.

### Changing Feedback Messages

Modify the comment functions (`commentcgpa`, `commentmarks`, etc.) in `app.py` to customize the feedback messages.

## Troubleshooting

### CSV File Not Found
- Make sure `bunny.csv` is in the same directory as `app.py`
- Check that the file name is spelled correctly

### Student Not Found
- Verify the roll number exists in the CSV
- Ensure roll numbers in CSV match the entered value

### Images Not Displaying
- Check that images are in the `images/` folder
- Verify image filenames match the roll number (e.g., `123.jpg` for roll 123)
- Supported formats: `.jpg`, `.png`

## License

This project is open source and available for educational purposes.

