import random
class NakliLLM:
    def __init__(self):
        print('LLM created')
    def predict(self,prompt):
        response_list=[
            'A','B','C'
        ]    
        return {'response':random.choice(response_list)}
llm=NakliLLM()
print(llm.predict('What is the capital of india'))
class NakliPrompt:
    def __init__(self,template,input_variable):
        self.template=template
        self.input_variable=input_variable
    def fromat(self,input_dict):
        return self.template.format(**input_dict)
        
     