# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "There are instances where multiple rules may apply to the same data point."
    answers["(b) explain"] = "There are scenarios where none of the rules apply"
    answers["(c) explain"] = "The rules are evaluated sequentially and the outcome of the classification may depend on order."
    answers["(d) explain"] = "Since there are instances where none of the rules apply, having a default class ensures that all cases are accounted for."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "yes"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "There are instances where multiple rules apply to the same data point."
    answers["(b) example"] = "Each rule covers a specific combination of atrributes, ensuring that every possible scenario is accounted for."
    answers["(c) example"] = "The rules should be evaluated in a specific order to avoid conflicts and ensure correct classification."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = False
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = True #change justification

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Since the weights at level k+1 are updated BEFORE the weights at level k are updated, the gradients of weights at the k+1th layer cannot be computed using the gradients of weights at the kth layer."
    answers["(b) explain"] = "For forward phase of back-propogation the outputs of the neurons at level k are computed prior to computing prior to computing the outputs at level k+1"
    answers["(c) explain"] = "Vanishing gradient problem occurs when the gradients become very small during backpropagation."
    answers["(d) explain"] = "The gradients of loss with repsect to weights at all layers will not necessarily be zero."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}


    # float
    answers["(a) P(X_1 = 1 | +)"] = None
    answers["(a) P(X_1 = 1 | -)"] = None
    answers["(a) P(X_2 = 1 | +)"] = None
    answers["(a) P(X_2 = 1 | -)"] = None
    answers["(a) P(X_3 = 1 | +)"] = None
    answers["(a) P(X_3 = 1 | -)"] = None

    # string
    answers["(b) label"] = None

    # float
    answers["(c) P(X_1=1)"] = None
    answers["(c) P(X_2=1)"] = None
    answers["(c) P(X_1=1,X_2=1)"] = None

    # string: "dependent" or "independent"
    answers["(c) Relationship between X_1 and X_2"] = None

    # float
    answers["(d) P(A=1)"] = None
    answers["(e) P(X_1=1, X_2=1|Class=+)"] = None
    answers["(e) P(X_1=1|Class=+)"] = None
    answers["(e) P(X_2=1|Class=+)"] = None

    # string: "yes" or "no"
    answers["(e) A and B conditionally independent?"] = None

    # float
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Since the points are closely clustered and have distinct regions, using k=1 will allow the model to capture the local structure more accurately."
    answers["(b) explain"] = "Since the data points are more spread out and there is no clear separation between classes, using k=5 will help smooth out the decision boundary and reduce the imapct of noise."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None  # WRONG
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
