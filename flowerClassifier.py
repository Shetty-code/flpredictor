import joblib
import streamlit as st


model = joblib.load('flowerClassifier.pkl')
st.title('My App')

st.write('Enter flower measurement to predict iris species')


sepal_length = st.number_input('enter sepal length')


sepal_width = st.number_input('enter sepal width')


petal_length = st.number_input('enter petal length')


petal_width = st.number_input('enter petal width')

if st.button('predict'):
    newData = [[sepal_length,sepal_width,petal_length,petal_width]]
    prediction = model.predict(newData)
    st.write(prediction)

    if prediction == 0:
        st.success('the predicted class is setosa')
    elif pred == 1:
            st.success('the predicted class is versicolor')
    else:
        st.success('the predicted class is vaginica')
