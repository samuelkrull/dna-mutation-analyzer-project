from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt 
import io 
import base64 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    img = None 
    result_text = ''
    
    if request.method == 'POST':
        seq1 = request.form['Seq1']
        seq2 = request.form['Seq2']

        if len(seq1) != len(seq2):
            result_text = "Sequences must be the same length."
            return render_template('compare.html', img=None, result_text=result_text)

        mutations = compare_sequences(seq1, seq2)
        result_text = f'Mutations found: {len(mutations)} at positions {mutations}'

        # Visualization
        fig, ax = plt.subplots(figsize=(len(seq1)/2, 2))
        mutation_positions = [m[0] for m in mutations]
        colors = ['green' if i not in mutation_positions else 'red' for i in range(len(seq1))]
        
        ax.bar(range(len(seq1)), [1]*len(seq1), color=colors)
        ax.set_xticks(range(len(seq1)))
        ax.set_yticks([])
        ax.set_title("Mutation Map")

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close(fig)

        # Save CSV
        df = pd.DataFrame(mutations, columns=['Position', 'Seq1', 'Seq2'])
        df.to_csv('mutations.csv', index=False)

    return render_template('compare.html', img=img, result_text=result_text)


def compare_sequences(seq1, seq2):
    mutations = []
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a != b:
            mutations.append((i, a, b))
    return mutations


if __name__ == '__main__':
    app.run(debug=True)