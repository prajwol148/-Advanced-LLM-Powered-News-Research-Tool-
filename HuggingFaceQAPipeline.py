from typing import Dict
from transformers import pipeline


class HuggingFaceQAPipeline:
    def __init__(self, model_name: str):
        self.model = pipeline("question-answering", model=model_name)

    def __call__(self, inputs: Dict[str, str]) -> Dict[str, str]:
        question = inputs["question"]
        context = inputs["context"]
        result = self.model(question=question, context=context)
        return {"answer": result["answer"]}


qa_model = HuggingFaceQAPipeline(model_name="deepset/roberta-base-squad2")
