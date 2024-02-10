# Course Evaluator

This is the course evaluation automation for SIS. There are 3 categories of evaluation here:
1. Good evaluation - The teachers who are in the good list will be evaluated with good evaluations. With all rating 5. And a good comment will be added to the evaluation.
2. Bad evaluation - The teachers who are in the bad list will be evaluated with bad evaluations. With all rating 1. And a bad comment will be added to the evaluation.
3. Neutral evaluation - The teachers who are not in the good list or the bad list will be evaluated with neutral evaluations. With all rating 3. And a neutral comment will be added to the evaluation.

To use this application follow the steps below.
```bash
git clone github.com/talha76/course-evaluator  # Clone the repository
cd course-evaluator  # Change directory to the repository
pip install -r requirements.txt  # Install the required packages
```

## Usage
Before running the application, provide your username, password of the IUT SIS website and the full-name or partial-substring of the names of the teachers for good evaluations in the good list and bad evaluations in the bad list in the `config.py` file. Then run the application using the following command.
```bash
python scraper.py  # Run the application
```
