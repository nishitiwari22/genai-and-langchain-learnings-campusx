<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python and Generative AI Foundations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            max-width: 950px;
        }
        code {
            background: #f4f4f4;
            padding: 3px 6px;
            border-radius: 4px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background: #f0f0f0;
        }
        h1, h2, h3, h4 {
            color: #333;
        }
        hr {
            margin: 40px 0;
        }
    </style>
</head>
<body>

<h1>Python and Generative AI Foundations</h1>

<p>
This document contains structured notes on Python system concepts,
data science fundamentals, Large Language Models (LLMs),
and advanced prompt engineering techniques.
</p>

<hr>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#sys-module">Python sys Module</a></li>
  <li><a href="#python-data-science">Why Python for Data Science</a></li>
  <li><a href="#float-facts">Facts About Floats</a></li>
  <li><a href="#llm-foundations">Core Foundations of Generative AI</a></li>
  <li><a href="#prompt-engineering">Advanced Prompt Engineering</a></li>
  <li><a href="#key-takeaways">Key Takeaways</a></li>
</ul>

<hr>

<h2 id="sys-module">1. Python sys Module</h2>

<p>
The <strong>sys module</strong> provides access to system-specific parameters
and functions, allowing interaction with the Python interpreter.
</p>

<h3>Common Uses</h3>
<ul>
    <li>Command-line arguments</li>
    <li>Exiting programs</li>
    <li>Checking Python version</li>
    <li>Managing module paths</li>
</ul>

<h3>Important Functions</h3>

<h4>sys.argv</h4>
<pre><code>import sys
print(sys.argv)</code></pre>

<h4>sys.exit()</h4>
<pre><code>import sys
sys.exit()</code></pre>

<h4>sys.path</h4>
<pre><code>import sys
print(sys.path)</code></pre>

<h4>sys.version</h4>
<pre><code>import sys
print(sys.version)</code></pre>

<h4>sys.getsizeof()</h4>
<pre><code>import sys
x = 10
print(sys.getsizeof(x))</code></pre>

<hr>

<h2 id="python-data-science">2. Why Python is Favored for Data Science</h2>

<h3>1. Simple and Readable Syntax</h3>
<pre><code>for i in range(5):
    print(i)</code></pre>

<h3>2. Powerful Libraries</h3>
<table>
    <tr>
        <th>Purpose</th>
        <th>Library</th>
    </tr>
    <tr>
        <td>Data manipulation</td>
        <td>Pandas</td>
    </tr>
    <tr>
        <td>Numerical computing</td>
        <td>NumPy</td>
    </tr>
    <tr>
        <td>Visualization</td>
        <td>Matplotlib, Seaborn</td>
    </tr>
    <tr>
        <td>Machine learning</td>
        <td>Scikit-learn</td>
    </tr>
    <tr>
        <td>Deep learning</td>
        <td>TensorFlow, PyTorch</td>
    </tr>
    <tr>
        <td>NLP</td>
        <td>NLTK, spaCy, Transformers</td>
    </tr>
</table>

<h3>Other Reasons</h3>
<ul>
    <li>Large community</li>
    <li>Easy integration with databases and cloud</li>
    <li>Fast prototyping</li>
    <li>Used across many domains</li>
</ul>

<hr>

<h2 id="float-facts">3. Facts About Float in Python</h2>

<h3>1. Binary Representation</h3>
<pre><code>print(0.1 + 0.2)</code></pre>
<p>Output: <code>0.30000000000000004</code></p>

<h3>2. Limited Precision</h3>
<p>Floats use 64-bit double precision with about 15–17 digits accuracy.</p>

<h3>3. Special Values</h3>
<table>
<tr><th>Value</th><th>Meaning</th></tr>
<tr><td>inf</td><td>Positive infinity</td></tr>
<tr><td>-inf</td><td>Negative infinity</td></tr>
<tr><td>nan</td><td>Not a number</td></tr>
</table>

<h3>4. Float Comparisons</h3>
<pre><code>import math
math.isclose(0.1 + 0.2, 0.3)</code></pre>

<h3>5. Decimal for Precision</h3>
<pre><code>from decimal import Decimal
Decimal('0.1') + Decimal('0.2')</code></pre>

<hr>

<h2 id="llm-foundations">4. Core Foundations of Generative AI</h2>

<h3>What is an LLM?</h3>
<p>
A Large Language Model predicts the next token based on context.
It is trained on massive text datasets.
</p>

<h3>GPT Architecture</h3>
<ul>
    <li>Tokenizer</li>
    <li>Embedding layer</li>
    <li>Transformer blocks</li>
    <li>Output layer</li>
</ul>

<h3>How LLMs Work</h3>
<ol>
    <li>Text → tokens</li>
    <li>Tokens’ → embeddings</li>
    <li>Pass through transformer layers</li>
    <li>Predict next token</li>
</ol>

<h3>Tokenization</h3>
<pre><code>"playing" → ["play", "ing"]</code></pre>

<h3>Embeddings</h3>
<p>Words are converted into numerical vectors.</p>

<h3>Transformer Breakthrough</h3>
<p>
Transformers use attention instead of sequential processing,
allowing better context understanding.
</p>

<h3>Positional Encoding</h3>
<p>
Adds position information to tokens so the model knows word order.
</p>

<h3>Multi-Head Attention</h3>
<p>
Multiple attention heads capture different relationships in the text.
</p>

<hr>

<h2 id="prompt-engineering">5. Advanced Prompt Engineering</h2>

<h3>Prompt Fundamentals</h3>
<p>A prompt is the instruction given to the model.</p>

<h3>Prompting Types</h3>
<table>
<tr><th>Type</th><th>Description</th></tr>
<tr><td>Zero-shot</td><td>No examples</td></tr>
<tr><td>One-shot</td><td>One example</td></tr>
<tr><td>Few-shot</td><td>Multiple examples</td></tr>
</table>

<h3>One-Shot Prompting</h3>
<p>Uses one example to guide output.</p>

<h3>Few-Shot Prompting</h3>
<p>Uses multiple examples for pattern learning.</p>

<h3>Structured Outputs</h3>
<pre><code>Text: John is 25 years old.
Output: {"name": "John", "age": 25}</code></pre>

<h3>Chain-of-Thought (CoT)</h3>
<p>
Encourages the model to reason step by step,
improving accuracy in complex problems.
</p>

<h3>Auto-CoT</h3>
<p>
Automatically generates reasoning examples for prompts.
</p>

<h3>Persona-Based Prompting</h3>
<pre><code>You are a senior data scientist.
Explain overfitting.</code></pre>

<hr>

<h2 id="key-takeaways">Key Takeaways</h2>
<ul>
    <li>LLMs work by predicting the next token using transformers.</li>
    <li>Text is converted into tokens and embeddings.</li>
    <li>Attention enables context understanding.</li>
    <li>Prompt engineering improves reasoning and output.</li>
    <li>Python dominates data science due to its ecosystem.</li>
</ul>

</body>
</html>
