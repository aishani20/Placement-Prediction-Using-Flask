import numpy as np
import pickle
import json
import sys
import os

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'trained_model 1.sav')

# loading the saved model
loaded_model = pickle.load(open(file_path, 'rb'))

# creating a function for Prediction
def make_prediction(Branch, Gender, tenth_percentage, twelfth_percentage, CGPA_Till_sixth, sixth_Sem_SGPA, Internship, Skills):
    # convert inputs to appropriate data types
    tenth_percentage = float(tenth_percentage)
    twelfth_percentage = float(twelfth_percentage)
    CGPA_Till_sixth = float(CGPA_Till_sixth)
    sixth_Sem_SGPA = float(sixth_Sem_SGPA)

    # convert categorical inputs to one-hot encoding
    branches = ['Bio-Medical Engineering', 'Civil Engineering', 'Computer Science & Engineering','Electrical Engineering', 'Electronics & Communication Engineering','Electronics & Instrumentation Engineering', 'Mechanical Engineering', 'Petro Chemical']
    genders = ['Male', 'Female']
    internships = ['Yes', 'No']
    skills = ['Machine Learning/AI', 'Python', 'Data Science', 'java', 'C++/C', 'DSA', 'SQL', 'MS-Office/MS-Word','UI/UX', 'IOT', 'Computer Vision', 'Cloud Computing', 'Graphic Designing', 'Web Development ']

    branch_idx = branches.index(Branch)
    gender_idx = genders.index(Gender)
    internship_idx = internships.index(Internship)
    
    skills_one_hot = np.zeros(len(skills))

    for skill in Skills:
        try:
            skills_one_hot[skills.index(skill)] = 1
        except ValueError:
            pass

    # create input array
    input_data = np.array([branch_idx, gender_idx, tenth_percentage, twelfth_percentage,
                           CGPA_Till_sixth, sixth_Sem_SGPA, internship_idx, *skills_one_hot])
    input_data = input_data.reshape(1, -1)

    # make prediction and return result
    prediction = loaded_model.predict(input_data)
    # print("This is prediction",prediction)

    return prediction[0]
       
        
# if __name__ == '__main__':
#     # Receive input data from the command line
#     input_data = json.loads(sys.argv[1])

#     # Make a prediction
#     #prediction = make_prediction(input_data["Branch"], input_data["Gender"], input_data["tenth_percentage"], input_data["twelfth_percentage"], input_data["CGPA_Till_sixth"], input_data["sixth_Sem_SGPA"], input_data["Internship"], input_data["Skills"])

#     # Output the prediction as a JSON string
#     print(json.dumps({"prediction": prediction}))