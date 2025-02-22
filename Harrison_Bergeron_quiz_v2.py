import streamlit as st

def main():
    st.title("Harrison Bergeron - Understanding & Analysis Quiz")
    
    # Provide text access
    with st.expander("Read this part of the story"):
        st.markdown("""
        **Harrison Bergeron** is a story about a world where everyone is forced to be equal.
        """)
    
    st.header("Answer the Question Below")
    
    # Define model answer
    model_answer = ("The handicaps in Harrison Bergeron are designed to enforce absolute equality by suppressing any "
                    "natural advantages individuals may have. For instance, those with above-average intelligence, like "
                    "George Bergeron, must wear mental handicap radios that emit disruptive noises, preventing them from "
                    "thinking deeply. Physically strong individuals, such as Harrison himself, carry immense weights to limit "
                    "their strength, while the beautiful must wear grotesque masks to obscure their attractiveness. These "
                    "handicaps ensure that no one is superior to another in any way, reflecting an extreme and oppressive "
                    "interpretation of equality.")
    
    # Step 1: Open-ended Question
    response_key = "Q1_response"
    if response_key not in st.session_state:
        st.session_state[response_key] = ""
    response = st.text_area("What is the purpose of the handicaps used in the society of Harrison Bergeron? Give examples of different types of handicaps used:", key=response_key)
    
    if response:
        # Check if the answer is similar to the model answer
        similarity_feedback = compare_answers(response, model_answer)
        
        if similarity_feedback["match"]:
            st.success("✅ Great response! Here is the model answer for comparison:")
            st.markdown(f"**Model Answer:** *{model_answer}*")
            st.write("Suggestions for improvement:")
            st.write(similarity_feedback["improvement_suggestions"])
        else:
            st.warning("Your response could be improved. Let’s go step by step.")
            
            # Step 2: Providing Examples of Handicaps (Scaffolding if needed)
            st.subheader("Examples of Government Handicaps")
            st.markdown("*Now, let's look at how the government enforces equality.*")
            
            mcq1_key = "Q1_mcq1"
            mcq1 = st.radio("What does George have to wear on his head?", 
                            ["A crown", "A mental radio", "A headband"], key=mcq1_key, index=None)
            
            if mcq1 == "A mental radio":
                st.success("✅ Correct! The mental radio disrupts his thoughts to prevent deep thinking.")
                
                # Concept Checking for Purpose
                mcq1_purpose_key = "Q1_mcq1_purpose"
                mcq1_purpose = st.radio("What is the purpose of the mental radio?", 
                            ["For George’s entertainment - he really likes music", 
                             "To prevent him from thinking too long", 
                             "To help him solve long problems, like using Google!"], 
                            key=mcq1_purpose_key, index=None)
                
                if mcq1_purpose == "To prevent him from thinking too long":
                    st.success("✅ Correct! The government limits intelligence by disrupting thoughts.")
                elif mcq1_purpose:
                    st.error("❌ Try again. Think about why intelligence needs to be controlled.")
            elif mcq1:
                st.error("❌ Try again. Think about how intelligence is controlled.")
            
            mcq2_key = "Q1_mcq2"
            mcq2 = st.radio("What do the dancers wear to make them equal?", 
                            ["Heavy weights", "Light shoes", "Glasses"], key=mcq2_key, index=None)
            
            if mcq2 == "Heavy weights":
                st.success("✅ Correct! The dancers wear weights to prevent them from moving gracefully.")
                
                # Concept Checking for Purpose
                mcq2_purpose_key = "Q1_mcq2_purpose"
                mcq2_purpose = st.radio("What is the purpose of the heavy weights?", 
                            ["To help them move more freely", 
                             "To make dancing harder so no one is better", 
                             "To train them to be better athletes"], 
                            key=mcq2_purpose_key, index=None)
                
                if mcq2_purpose == "To make dancing harder so no one is better":
                    st.success("✅ Correct! The weights ensure no one is naturally more skilled at dancing.")
                elif mcq2_purpose:
                    st.error("❌ Try again. Think about why physical ability needs to be controlled.")
            elif mcq2:
                st.error("❌ Try again. Think about how physical ability is controlled.")
    
    # Step 3: Model Answer and Final Comparison
    st.subheader("Final Comparison with Model Answer")
    st.markdown(f"**Model Answer:** *{model_answer}*")
    
    st.write("Compare your final answer with the model and think about what you included and what was missing.")
    

def compare_answers(student_answer, model_answer):
    student_words = set(student_answer.lower().split())
    model_words = set(model_answer.lower().split())
    correct_words = student_words.intersection(model_words)
    missing_words = model_words - student_words
    
    match = len(correct_words) / len(model_words) > 0.7  # If at least 70% match
    improvement_suggestions = f"✅ Words you included: {', '.join(correct_words)}\n❌ Words you missed: {', '.join(missing_words)}"
    
    return {"match": match, "improvement_suggestions": improvement_suggestions}

if __name__ == "__main__":
    main()
