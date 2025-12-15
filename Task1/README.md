Dataset downloaded via <u>Kaggle API</u>  

HuggingFace model <u>"google/flan-t5-small"</u> used  

**Prompts**:

1. **Zero-Shot Prompt**:
A zero-shot prompt is a direct instruction or question given to a large language model (LLM) without providing any prior examples of the task.  
<u>Purpose</u>:  
Baseline performance  
<u>WHY</u>:  
Tests raw LLM capability  
Often weaker consistency and JSON errors

2. **Rubric-Guided Prompt**:  
A rubric-guided prompt is a prompt engineering technique where explicit evaluation criteria, "rubric", are included within the instructions given to a large language model (LLM).  
<u>Improvements</u>: Adds explicit criteria  
<u>WHY</u>:  
Improves rating alignment  
Reduces ambiguity  

3. **Reasoned Prompt**:  
A reasoned prompt is a specialized instruction for AI that encourages step-by-step logical thinking (reasoning) rather than just pattern matching.  
<u>Improvement</u>: Better reasoning consistency  
<u>WHY</u>:  
Encourages internal reasoning  
Often improves accuracy without verbose output  

**JSON Parser**:  
Returns data and validity, extracts numbers from reviews  

**Evaluate**:
Evaluates prompts and works on the dataset
Visible progress bars

**Result**:
Prompts are run and final table contains <u>Prompts</u>, <u>Accuracy</u>, <u>JSON Validity Rate</u> and <u>Consistency</u>
