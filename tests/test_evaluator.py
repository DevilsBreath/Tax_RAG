import pytest
from src.evaluator import Evaluator

def test_calculate_grounded_precision():
    evaluator = Evaluator()
    
    answer = "The standard deduction is 75000."
    context = [{"text": "Under section 115BAC, the standard deduction is 75000 for salaried individuals."}]
    
    precision = evaluator.calculate_grounded_precision(answer, context)
    assert precision > 0.5  # Words like 'standard', 'deduction', 'is', '75000' overlap

def test_calculate_grounded_precision_no_overlap():
    evaluator = Evaluator()
    
    answer = "Apples are red."
    context = [{"text": "The standard deduction is 75000."}]
    
    precision = evaluator.calculate_grounded_precision(answer, context)
    assert precision == 0.0
