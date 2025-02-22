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
            st.success("✅ Great response! Here is some feedback on how you can improve your academic style and clarity:")
            st.write(similarity_feedback["improvement_suggestions"])
            
            st.subheader("Final Comparison with Model Answer")
            st.markdown(f"**Model Answer:** *{model_answer}*")
        else:
            st.warning("Your response could be improved. Let’s go step by step.")
            
            # Provide First Section of Text for Scaffolding
            st.subheader("Re-read This Section")
            st.markdown("*Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.*")
            
            # Concept Checking for Understanding the Section
            intelligence_mcq = st.radio("What does this text say about intelligence?",
                                       ["Everyone has the same intelligence", "Everyone has different intelligence", "Everyone has different intelligence but the government tries to make it equal"],
                                       key="intelligence_mcq", index=None)
            
            beauty_mcq = st.radio("What does this text say about beauty?",
                                 ["Everyone is equally beautiful", "Some people are naturally more beautiful but the government makes them wear masks", "Everyone is naturally ugly"],
                                 key="beauty_mcq", index=None)
            
            strength_mcq = st.radio("What does this text say about strength?",
                                    ["Everyone is equally strong", "Some people are naturally stronger but the government weakens them", "Strength doesn't matter in this society"],
                                    key="strength_mcq", index=None)
            
            # Step 2: Summarizing the "Nobody was..." Section
            st.subheader("Summarize This Section")
            st.text_area("Use this sentence starter to summarize: In this society, the government made sure that everyone...", key="summary_nobody_was")
            
            # Step 3: Concept Checking - Mental Radio First
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
                    
                    # Once Mental Radio Questions Are Done, Show Dancer Questions
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
                            
                            # Step 4: Structured Answer Construction
                            st.subheader("Now, let's build your answer:")
                            structured_answer_key = "Q1_structured_answer"
                            st.text_area("Complete these sentences:", 
                                         "George's father wears a mental radio to...\n"
                                         "The dancers wear... so that...", key=structured_answer_key)
                            
                            # Final Rewrite Based on Everything Learned
                            final_answer_key = "Q1_final_answer"
                            st.text_area("Now, rewrite your full answer using what you've learned:", key=final_answer_key)
                            
                            # Final Model Answer Comparison
                            st.subheader("Final Comparison with Model Answer")
                            st.markdown(f"**Model Answer:** *{model_answer}*")
                            st.write("Compare your final answer with the model and think about what you included and what was missing.")
    
if __name__ == "__main__":
    main()
