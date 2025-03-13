# Quiz Performance Visualization - README

## Overview
This project provides an interactive visualization of quiz performance using **Chart.js**. The data includes **accuracy, time spent per question, difficulty trends, and overall quiz insights**. It features multiple visualizations such as bar charts, pie charts, radar charts, and a calendar heatmap.

## Features
- **Accuracy Analysis**: Displays the number of correct vs. incorrect answers.
- **Time Tracking**: Shows time spent per question and total quiz duration.
- **Stacked Time Segments**: Categorizes time into reading, answering, and reviewing.
- **Progress Gauge**: Measures how much of the allowed time was used.
- **Pie Chart for Time Spent**: Breakdown of activities.
- **Calendar Heatmap**: Tracks daily quiz activity.

## How It Works
1. **Data Source**: The quiz results are passed as a JSON object.
2. **Chart Generation**: Uses Chart.js to create interactive graphs.
3. **Dynamic Updates**: Displays real-time calculations for total time and average time per question.
4. **Comparison with Benchmark**: Highlights if the user spent excessive time.

## Installation & Usage
1. Clone the repository or download the `visualization.html` file.
2. Ensure you have an environment that supports JavaScript and Chart.js.
3. Open the `visualization.html` file in a browser.
4. Pass quiz results as JSON to visualize performance.

## Dependencies
- Chart.js (CDN)
- Chart.js Matrix Plugin (For Calendar Heatmap)

## Customization
- Modify the **benchmark time per question** in the script.
- Adjust colors and layout by editing CSS styles.
- Extend functionality by integrating with a backend to store quiz history.

## Future Enhancements
- Export results as a report.
- Add user login for personalized insights.
- Integrate AI-based recommendations for improvement.

Enjoy analyzing your quiz performance! 🚀

