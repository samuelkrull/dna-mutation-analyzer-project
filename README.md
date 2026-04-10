 DNA Sequence Mutation Comparator

A Flask-based web application that compares two DNA sequences and identifies mutations, visualizes them using green and red then exports results to a CSV file.

Features
Compares two DNA sequences of equal length
Detects mutation positions
Visual mutation map  using Matplotlib
Export mutation results to CSV
Simple web interface built with Flask

Tech Stack
Python
Flask
Pandas
Matplotlib
HTML (templates)

How to Run Locally
1. Clone the repository
git clone https://github.com/samuelkrull/dna-mutation-analyzer-project
[cd your-repo-name](https://github.com/samuelkrull/dna-mutation-analyzer-project)

3. Install dependencies
pip install -r requirements.txt

5. Run the app
python app.py

7. Open in browser
http://127.0.0.1:5000

 Project Structure
   dna-mutation-analyzer-project/
│
├── app.py
├── templates/
│   └── compare.html
├── static/
├── requirements.txt
├── README.md
└── .gitignore

 Examples

Input:

Seq1: ATGCTAGCTAGGCTAATCGGATCGA
Seq2: ATGCTAGATAGGCTTATCGGATAGA

Output:

Mutation detection
Visualization shows mutation highlighted in red
CSV file generated with mutation details
 Output Files
mutations.csv → contains mutation positions and base changes

 Warning:
Sequences must be of equal length
Only basic DNA comparison is supported (A, C, T, G)

 Author
Martin Kouadjo

